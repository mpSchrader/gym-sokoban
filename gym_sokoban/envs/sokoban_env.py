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


def generate_level(dim=(13,13), p_change_directions=0.35, num_steps=10):
    level = room_topology_generation(dim, p_change_directions, num_steps)


def room_topology_generation(dim=(10, 10), p_change_directions=0.35, num_steps=15):
        dim_x, dim_y = dim

        masks = [
            [
                [0, 0, 0],
                [1, 1, 1],
                [0, 0, 0]
            ],
            [
                [0, 1, 0],
                [0, 1, 0],
                [0, 1, 0]
            ],
            [
                [0, 0, 0],
                [1, 1, 0],
                [0, 1, 0]
            ],
            [
                [0, 0, 0],
                [1, 1, 0],
                [1, 1, 0]
            ],
            [
                [0, 0, 0],
                [0, 1, 1],
                [0, 1, 0]
            ]
        ]

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        direction = random.sample(directions, 1)[0]

        position = np.array([
            random.randint(1, dim_x - 1),
            random.randint(1, dim_y - 1)]
        )

        level = np.zeros(dim, dtype=int)

        for s in range(num_steps):

            # Change direction randomly
            if random.random() < p_change_directions:
                direction = random.sample(directions, 1)[0]

            # Update position
            position = position + direction
            position[0] = max(min(position[0], dim_x - 2), 1)
            position[1] = max(min(position[1], dim_y - 2), 1)

            # Set mask
            mask = random.sample(masks, 1)[0]
            mask_start = position - 1
            level[mask_start[0]:mask_start[0] + 3, mask_start[1]:mask_start[1] + 3] += mask

        level[level > 0] = 1
        level[:, [0, dim_y - 1]] = 0
        level[[0, dim_x - 1], :] = 0

        return level
