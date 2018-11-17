from .sokoban_env import SokobanEnv
from .render_utils import room_to_rgb_FT, room_to_tiny_world_rgb_FT
from gym.spaces import Box


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

    # def render(self, mode='human', close=None):
    #     img = room_to_rgb_FT(self.room_state, self.box_mapping, self.room_fixed)
    #
    #     if mode == 'rgb_array':
    #         return img
    #     elif mode is 'human':
    #         from gym.envs.classic_control import rendering
    #         if self.viewer is None:
    #             self.viewer = rendering.SimpleImageViewer()
    #         self.viewer.imshow(img)
    #         return self.viewer.isopen
    #     else:
    #         super(FixedTargetsSokobanEnv, self).render(mode=mode)

    def get_image(self, mode):

        if mode.startswith('tiny_'):
            img = room_to_tiny_world_rgb_FT(self.room_state, self.box_mapping, self.room_fixed, scale=16)
        else:
            img = room_to_rgb_FT(self.room_state, self.box_mapping, self.room_fixed)

        return img

    def step(self, action):

        observation, self.reward_last, done, info = super(FixedTargetsSokobanEnv, self).step(action)

        return observation, self.reward_last, done, info

    def _calc_reward(self):
        self._update_box_mapping()

        # Every step a small penalty is given, This ensures
        # that short solutions have a higher reward.
        self.reward_last = self.penalty_for_step

        for b in range(len(self.boxes_are_on_target)):

            previous_state = self.boxes_are_on_target[b]

            # Calculate new state
            box_id = list(self.box_mapping.keys())[b]
            new_state = self.box_mapping[box_id] == box_id

            if previous_state and not new_state:
                # Box was pushed of its target
                self.reward_last += self.penalty_box_off_target
            elif not previous_state and new_state:
                # box was pushed on its target
                self.reward_last += self.reward_box_on_target

            self.boxes_are_on_target[b] = new_state

    def _update_box_mapping(self):
        if self.new_box_position is not None:
            box_index = list(self.box_mapping.values()).index(self.old_box_position)
            box_id = list(self.box_mapping.keys())[box_index]
            self.box_mapping[box_id] = self.new_box_position

    def _check_if_all_boxes_on_target(self):

        for key in self.box_mapping.keys():
            if not key == self.box_mapping[key]:
                return False

        return True
