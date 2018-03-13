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

        # Initialize Room
        self.reset()

        room_to_rgb(self.room_state)

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def step(self, action):
        # TODO
        self.reward_last = 0
        self.num_env_steps += 1

        if action < 4:
            self._push(action)
        else:
            self._move(action % 4)

        done = False
        if np.where(self.room_state == 4)[0].shape[0] == 0 or self.max_steps == self.num_env_steps:
            done = True
            self.reward_last += self.reward_finished

        return self.room_state, self.reward_last, done, {}

    def _push(self, action):
        # TODO
        return action

    def _move(self, action):
        # TODO
        return action

    def reset(self):
        self.room_fixed, self.room_state = generate_room(dim=self.dim_room, num_steps=self.num_gen_steps)
        self.player_position = np.argwhere(self.room_state == 5)[0]
        self.num_env_steps = 0
        self.reward_last = 0


    def render(self, mode='human', close=None):
        if mode == 'rgb_array':
            # TODO
            return np.zeros((self.dim_room[0], self.dim_room[1], 3))  # return RGB frame suitable for video
        elif mode is 'human':
            pass
            return [0]
            # TODO
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
    0: (0, 1),
    1: (0, -1),
    2: (-1, 0),
    3: (1, 0)
}
