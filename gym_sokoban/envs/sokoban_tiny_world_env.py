from .sokoban_env import SokobanEnv
from .room_utils import room_to_tiny_world_rgb
from gym.spaces import Box
import numpy as np


class TinyWorldSokobanEnv(SokobanEnv):

    def __init__(self,
             dim_room=(10, 10),
             max_steps=120,
             num_boxes=4,
             num_gen_steps=None):

        super(TinyWorldSokobanEnv, self).__init__(dim_room, max_steps, num_boxes, num_gen_steps)
        screen_height, screen_width = (dim_room[0] * 16, dim_room[1] * 16)
        self.observation_space = Box(low=0, high=255, shape=(screen_height, screen_width, 3))

    def reset(self):
        super(TinyWorldSokobanEnv, self).reset()
        observation = room_to_tiny_world_rgb(self.room_state, self.room_fixed)

        return observation

    def step(self, action):
        _, reward, done, info = super(TinyWorldSokobanEnv, self).step(action)
        observation = room_to_tiny_world_rgb(self.room_state, self.room_fixed)

        return observation, reward, done, info

    def render(self, mode='human', close=None):
        img = room_to_tiny_world_rgb(self.room_state, self.room_fixed, scale=16)

        if mode == 'rgb_array':
            return img
        elif mode is 'human':
            from gym.envs.classic_control import rendering
            if self.viewer is None:
                self.viewer = rendering.SimpleImageViewer()
            self.viewer.imshow(img)
            return self.viewer.isopen
        else:
            super(TinyWorldSokobanEnv, self).render(mode=mode)  # just raise an exception
