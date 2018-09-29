from .sokoban_env import SokobanEnv
from .render_utils import room_to_rgb_FT
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


    def step(self, action):

        observation, self.reward_last, done, info = super(FixedTargetsSokobanEnv, self).step(action)

        return observation, self.reward_last, done, info


ACTION_LOOKUP = {
    0: 'pull up',
    1: 'pull down',
    2: 'pull left',
    3: 'pull right',
    4: 'move up',
    5: 'move down',
    6: 'move left',
    7: 'move right',
    8: 'push up',
    9: 'push down',
    10: 'push left',
    11: 'push right',
}

