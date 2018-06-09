from .sokoban_env import SokobanEnv
from .render_utils import room_to_rgb_FT
from gym.spaces import Box
import numpy as np


class FixedTargetsSokobanEnv(SokobanEnv):

    def __init__(self,
             dim_room=(10, 10),
             max_steps=120,
             num_boxes=3,
             num_gen_steps=None):

        super(FixedTargetsSokobanEnv, self).__init__(dim_room, max_steps, num_boxes, num_gen_steps)
        screen_height, screen_width = (dim_room[0] * 16, dim_room[1] * 16)
        self.observation_space = Box(low=0, high=255, shape=(screen_height, screen_width, 3))
        self.boxes_are_on_target = [False] * num_boxes
        pass

    def render(self, mode='human', close=None):
        img = room_to_rgb_FT(self.room_state, self.box_mapping, self.room_fixed)

        if mode == 'rgb_array':
            return img
        elif mode is 'human':
            from gym.envs.classic_control import rendering
            if self.viewer is None:
                self.viewer = rendering.SimpleImageViewer()
            self.viewer.imshow(img)
            return self.viewer.isopen
        else:
            super(FixedTargetsSokobanEnv, self).render(mode=mode)

    def step(self, action):

        observation, self.reward_last, done, _ = super(FixedTargetsSokobanEnv, self).step(action)

        self._update_box_mapping()

        return observation, self.reward_last, done, {}

    def _calc_reward(self):
        pass

    def _update_box_mapping(self):
        if self.new_box_position is not None:
            box_index = list(self.box_mapping.values()).index(self.old_box_position)
            box_id = list(self.box_mapping.keys())[box_index]
            self.box_mapping[box_id] = self.new_box_position