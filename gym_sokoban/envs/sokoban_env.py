import gym
from gym.utils import seeding
import random
import numpy as np

class SokobanEnv(gym.Env):
    metadata = {
        'render.modes' : ['human', 'rgb_array'],
        'video.frames_per_second' : 30
    }

    def __init__(self):

        # Penalties and Rewards
        self.penalty_for_step = -0.1
        self.penalty_box_off_target = -1
        self.reward_box_on_target = 1
        self.reward_finished = 10

        # Other Settings
        self.max_steps = 120

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def step(self,u):
        pass

    def reset(self):
        pass

    def _get_obs(self):
        pass

    def render(self, mode='human'):
        pass

    def close(self):
        pass
