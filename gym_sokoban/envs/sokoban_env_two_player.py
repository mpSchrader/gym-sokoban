from .sokoban_env import SokobanEnv, CHANGE_COORDINATES
from gym.spaces import Box
from gym.spaces.discrete import Discrete
from .render_utils import room_to_rgb, room_to_tiny_world_rgb, color_player_two, color_tiny_player_two
import numpy as np


class TwoPlayerSokobanEnv(SokobanEnv):

    def __init__(self,
             dim_room=(10, 10),
             max_steps=120,
             num_boxes=3,
             num_gen_steps=None):

        super(TwoPlayerSokobanEnv, self).__init__(dim_room, max_steps, num_boxes, num_gen_steps)
        screen_height, screen_width = (dim_room[0] * 16, dim_room[1] * 16)
        self.observation_space = Box(low=0, high=255, shape=(screen_height, screen_width, 3))
        self.boxes_are_on_target = [False] * num_boxes
        self.action_space = Discrete(len(ACTION_LOOKUP))

        self.player_position = []
        self.player_positions = {}

        pass

    def reset(self):
        super(TwoPlayerSokobanEnv, self).reset(second_player=True)

        self.player_positions = {
            0: np.argwhere(self.room_state == 5)[0],
            1: np.argwhere(self.room_state == 5)[1]
        }

        return self.render(mode="rgb_array")

    def step(self, action):
        assert action in ACTION_LOOKUP

        self.num_env_steps += 1

        self.new_box_position = None
        self.old_box_position = None

        active_player = 0
        if action > 7:
            active_player = 1

        self.player_position = self.player_positions[active_player]

        player_action = action % 8

        moved_player = False
        moved_box = False
        # All push actions are in the range of [0, 3]
        if player_action < 4:
            moved_player, moved_box = self._push(player_action)

        elif player_action < 8:
            moved_player = self._move(player_action)

        self.player_positions[active_player] = self.player_position

        self._calc_reward()

        done = self._check_if_done()

        # Convert the observation to RGB frame
        observation = self.render(mode='rgb_array')

        info = {
            "action.name": ACTION_LOOKUP[action],
            "action.moved_player": moved_player,
            "action.moved_box": moved_box,
            "action,active_player": active_player
        }
        if done:
            info["maxsteps_used"] = self._check_if_maxsteps()
            info["all_boxes_on_target"] = self._check_if_all_boxes_on_target()

        return observation, self.reward_last, done, info

    def get_image(self, mode):

        if mode.startswith('tiny_'):
            scale = 16
            img = room_to_tiny_world_rgb(self.room_state, self.room_fixed, scale=scale)
            img = color_tiny_player_two(img, self.player_positions[1], self.room_fixed, scale=scale)
        else:
            img = room_to_rgb(self.room_state, self.room_fixed)
            img = color_player_two(img, self.player_positions[1], self.room_fixed)

        return img

    def get_action_lookup(self):
        return ACTION_LOOKUP

    def get_action_meanings(self):
        return ACTION_LOOKUP


ACTION_LOOKUP = {
    0: 'P1: push up',
    1: 'P1: push down',
    2: 'P1: push left',
    3: 'P1: push right',
    4: 'P1: move up',
    5: 'P1: move down',
    6: 'P1: move left',
    7: 'P1: move right',
    8: 'P2: push up',
    9: 'P2: push down',
    10: 'P2: push left',
    11: 'P2: push right',
    12: 'P2: move up',
    13: 'P2: move down',
    14: 'P2: move left',
    15: 'P2: move right'
}

