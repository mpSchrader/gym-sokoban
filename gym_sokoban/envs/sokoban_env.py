import gym
from gym.utils import seeding
from gym.spaces.discrete import Discrete
from gym.spaces import Box
from .room_utils import generate_room, room_to_rgb
import numpy as np


class SokobanEnv(gym.Env):
    metadata = {
        'render.modes': ['human', 'rgb_array']
    }

    def __init__(self,
                 dim_room=(10, 10),
                 max_steps=120,
                 num_boxes=4,
                 num_gen_steps=None):

        # General Configuration
        self.dim_room = dim_room
        if num_gen_steps == None:
            self.num_gen_steps = int(1.7 * (dim_room[0] + dim_room[1]))
        else:
            self.num_gen_steps = num_gen_steps

        self.num_boxes = num_boxes
        self.boxes_on_target = 0

        # Penalties and Rewards
        self.penalty_for_step = -0.1
        self.penalty_box_off_target = -1
        self.reward_box_on_target = 1
        self.reward_finished = 10
        self.reward_last = 0

        # Other Settings
        self.viewer = None
        self.max_steps = max_steps
        self.action_space = Discrete(len(ACTION_LOOKUP))
        screen_height, screen_width = (dim_room[0] * 16, dim_room[1] * 16)
        self.observation_space = Box(low=0, high=255, shape=(screen_height, screen_width, 3), dtype=np.uint8)

        # Initialize Room
        self.reset()

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def step(self, action):
        assert action in ACTION_LOOKUP

        # Every step a small penalty is given, This ensures
        # that short solutions have a higher reward.
        self.reward_last = self.penalty_for_step
        self.num_env_steps += 1

        # All push actions are in the range of [0, 3]
        if action < 4:
            self._push(action)

            # Calculate reward for push off or on the target
            empty_targets = self.room_state == 2
            player_on_target = (self.room_fixed == 2) & (self.room_state == 5)
            total_targets = empty_targets | player_on_target

            current_boxes_on_target = self.num_boxes - \
                                      np.where(total_targets)[0].shape[0]

            # Add a reward if a box is pushed on the target and give a
            # penalty if a box is pushed off the target.
            if current_boxes_on_target > self.boxes_on_target:
                self.reward_last += self.reward_box_on_target
            elif current_boxes_on_target < self.boxes_on_target:
                self.reward_last += self.penalty_box_off_target

            self.boxes_on_target = current_boxes_on_target

        else:
            self._move(action)

        # Check if the game is over either through reaching the maximum number
        # of available steps or by pushing all boxes on the targets.
        done = (self.max_steps == self.num_env_steps)
        empty_targets = self.room_state == 2
        player_on_target = (self.room_fixed == 2) & (self.room_state == 5)

        if np.where(empty_targets | player_on_target)[0].shape[0] == 0:
            done = True
            self.reward_last += self.reward_finished

        # Convert the observation to RGB frame
        observation = room_to_rgb(self.room_state)

        return observation, self.reward_last, done, {}

    def _push(self, action):
        """
        Perform a push, if a box is adjacent in the right direction.
        If no box, can be pushed, try to move.
        :param action:
        :return: Boolean, indicating a change of the room's state
        """
        change = CHANGE_COORDINATES[action % 4]
        new_position = self.player_position + change
        current_position = self.player_position.copy()

        # No push, if the push would get the box out of the room's grid
        new_box_position = new_position + change
        if new_box_position[0] >= self.room_state.shape[0] \
                or new_box_position[1] >= self.room_state.shape[1]:
            return False

        can_push_box = self.room_state[new_position[0], new_position[1]] in [3, 4]
        can_push_box &= self.room_state[new_box_position[0], new_box_position[1]] in [1, 2]
        if can_push_box:
            # Move Player
            self.player_position = new_position
            self.room_state[(new_position[0], new_position[1])] = 5
            self.room_state[current_position[0], current_position[1]] = \
                self.room_fixed[current_position[0], current_position[1]]

            # Move Box
            box_type = 4
            if self.room_fixed[new_box_position[0], new_box_position[1]] == 2:
                box_type = 3
            self.room_state[new_box_position[0], new_box_position[1]] = box_type
            return True

        # Try to move if no box to push, available
        else:
            return self._move(action)

    def _move(self, action):
        """
        Moves the player to the next field, if it is not occupied.
        :param action:
        :return: Boolean, indicating a change of the room's state
        """
        change = CHANGE_COORDINATES[action % 4]
        new_position = self.player_position + change
        current_position = self.player_position.copy()

        # Move player if the field in the moving direction is either
        # an empty field or an empty box target.
        if self.room_state[new_position[0], new_position[1]] in [1, 2]:
            self.player_position = new_position
            self.room_state[(new_position[0], new_position[1])] = 5
            self.room_state[current_position[0], current_position[1]] = \
                self.room_fixed[current_position[0], current_position[1]]

            return True

        return False

    def reset(self):
        self.room_fixed, self.room_state = generate_room(
            dim=self.dim_room,
            num_steps=self.num_gen_steps,
            num_boxes=self.num_boxes
        )
        self.player_position = np.argwhere(self.room_state == 5)[0]
        self.num_env_steps = 0
        self.reward_last = 0
        self.boxes_on_target = 0

        starting_observation = room_to_rgb(self.room_state, self.room_fixed)
        return starting_observation

    def render(self, mode='human', close=None):
        img = room_to_rgb(self.room_state, self.room_fixed)

        if mode == 'rgb_array':
            return img
        elif mode is 'human':
            from gym.envs.classic_control import rendering
            if self.viewer is None:
                self.viewer = rendering.SimpleImageViewer()
            self.viewer.imshow(img)
            return self.viewer.isopen
        else:
            super(SokobanEnv, self).render(mode=mode)  # just raise an exception

    def close(self):
        if self.viewer is not None:
            self.viewer.close()


ACTION_LOOKUP = {
    0: 'pull up',
    1: 'pull down',
    2: 'pull left',
    3: 'pull right',
    4: 'move up',
    5: 'move down',
    6: 'move left',
    7: 'move right',
}

# Moves are mapped to coordinate changes as follows
# 0: Move up
# 1: Move down
# 2: Move left
# 3: Move right
CHANGE_COORDINATES = {
    0: (-1, 0),
    1: (1, 0),
    2: (0, -1),
    3: (0, 1)
}
