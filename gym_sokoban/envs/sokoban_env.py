import gym
from gym.utils import seeding
from gym.spaces.discrete import Discrete
from gym.spaces.box import Box
from .room_utils import generate_room, room_to_rgb
import numpy as np


class SokobanEnv(gym.Env):
    metadata = {
        'render.modes': ['human', 'rgb_array'],
        'video.frames_per_second': 1
    }

    def __init__(self, dim_room=(10, 10), max_steps=120):
        # General Configuration
        self.dim_room = dim_room
        self.num_gen_steps = int(1.5 * (dim_room[0] + dim_room[1]))
        self.num_boxes = 3

        # Penalties and Rewards
        self.penalty_for_step = -0.1
        self.penalty_box_off_target = -1
        self.reward_box_on_target = 1
        self.reward_finished = 10

        # Other Settings
        self.max_steps = max_steps
        self.action_space = Discrete(len(ACTION_LOOKUP))
        self.observation_space = Box(low=0,
                                     high=6,
                                     shape=dim_room)
        self.viewer = None

        # Initialize Room
        self.reset()

        #room_to_rgb(self.room_state)

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def step(self, action):

        self.reward_last = self.penalty_for_step
        self.num_env_steps += 1
        room_to_rgb(self.room_state)
        if action < 4:
            self._push(action)

            # Calculate reward for push off or on the target
            current_boxes_on_target = self.num_boxes - np.where(self.room_state == 2)[0].shape[0]
            if current_boxes_on_target > self.boxes_on_target:
                self.reward_last += self.reward_box_on_target
            elif current_boxes_on_target < self.boxes_on_target:
                self.reward_last += self.reward_box_on_target
            self.boxes_on_target = current_boxes_on_target

        else:
            self._move(action)

        done = (self.max_steps == self.num_env_steps)
        if np.where(self.room_state == 2)[0].shape[0] == 0:
            done = True
            self.reward_last += self.reward_finished
        room_to_rgb(self.room_state)
        return self.room_state, self.reward_last, done, {}

    def _push(self, action):
        change = CHANGE_COORDINATES[action % 4]
        new_position = self.player_position + change
        current_position = self.player_position.copy()

        if self.room_state[new_position[0], new_position[1]] in [1, 2]:
            self.player_position = new_position
            self.room_state[(new_position[0], new_position[1])] = 5
            self.room_state[current_position[0], current_position[1]] = \
                self.room_fixed[current_position[0], current_position[1]]
            return

        new_box_position = new_position + change
        if new_box_position[0] >= self.room_state.shape[0] or new_box_position[1] >= self.room_state.shape[1]:
            return
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
            return

    def _move(self, action):
        change = CHANGE_COORDINATES[action % 4]
        new_position = self.player_position + change
        current_position = self.player_position.copy()

        if self.room_state[new_position[0], new_position[1]] in [1, 2]:
            self.player_position = new_position
            self.room_state[(new_position[0], new_position[1])] = 5
            self.room_state[current_position[0], current_position[1]] = \
                self.room_fixed[current_position[0], current_position[1]]

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
        # Nothing to clean up during close
        pass

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