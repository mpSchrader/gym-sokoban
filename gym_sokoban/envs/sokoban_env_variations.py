from .sokoban_env import SokobanEnv
from .sokoban_env_fixed_targets import FixedTargetsSokobanEnv
from .sokoban_env_pull import PushAndPullSokobanEnv
from .sokoban_env_two_player import TwoPlayerSokobanEnv
from .boxoban_env import BoxobanEnv
from .boxoban_env_pull import PushAndPullBoxobanEnv


class SokobanEnv1(SokobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array'],
    }

    def __init__(self):
        super(SokobanEnv1, self).__init__(
            num_boxes=3, max_steps=200
        )


class SokobanEnv2(SokobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array'],
    }

    def __init__(self):
        super(SokobanEnv2, self).__init__(
            num_boxes=5, max_steps=200, num_gen_steps=40
        )


class SokobanEnv_Small0(SokobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array'],
    }

    def __init__(self):
        super(SokobanEnv_Small0, self).__init__(
            dim_room=(7, 7), max_steps=200, num_boxes=2
        )


class SokobanEnv_Small1(SokobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array'],
    }

    def __init__(self):
        super(SokobanEnv_Small1, self).__init__(
            dim_room=(7, 7), max_steps=200, num_boxes=3
        )


class SokobanEnv_Large0(SokobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array'],
    }

    def __init__(self):
        super(SokobanEnv_Large0, self).__init__(
            dim_room=(13, 11), max_steps=300, num_boxes=3,
            num_gen_steps=43
        )


class SokobanEnv_Large1(SokobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array'],
    }

    def __init__(self):
        super(SokobanEnv_Large1, self).__init__(
            dim_room=(13, 11), max_steps=300, num_boxes=4,
            num_gen_steps=43
        )


class SokobanEnv_Large1(SokobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array'],
    }

    def __init__(self):
        super(SokobanEnv_Large1, self).__init__(
            dim_room=(13, 11), max_steps=300, num_boxes=5,
            num_gen_steps=43
        )


class SokobanEnv_Huge0(SokobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array'],
    }

    def __init__(self):
        super(SokobanEnv_Huge0, self).__init__(
            dim_room=(13, 13), max_steps=300, num_boxes=5,
            num_gen_steps=50
        )


class FixedTargets_Env_v0(FixedTargetsSokobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array'],
    }

    def __init__(self):
        super(FixedTargets_Env_v0, self).__init__(
            dim_room=(10, 10), max_steps=150, num_boxes=3,
            num_gen_steps=50
        )


class FixedTargets_Env_v1(FixedTargetsSokobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array'],
    }

    def __init__(self):
        super(FixedTargets_Env_v1, self).__init__(
            dim_room=(10, 10), max_steps=150, num_boxes=4,
            num_gen_steps=50
        )


class FixedTargets_Env_v2(FixedTargetsSokobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array'],
    }

    def __init__(self):
        super(FixedTargets_Env_v2, self).__init__(
            dim_room=(7, 7), max_steps=150, num_boxes=2,
            num_gen_steps=50
        )


class FixedTargets_Env_v3(FixedTargetsSokobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array'],
    }

    def __init__(self):
        super(FixedTargets_Env_v3, self).__init__(
            dim_room=(7, 7), max_steps=150, num_boxes=3,
            num_gen_steps=50
        )


class PushAndPull_Env_v0(PushAndPullSokobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array'],
    }

    def __init__(self):
        super(PushAndPull_Env_v0, self).__init__(
            dim_room=(10, 10), max_steps=150, num_boxes=3,
            num_gen_steps=50
        )


class PushAndPull_Env_v1(PushAndPullSokobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array'],
    }

    def __init__(self):
        super(PushAndPull_Env_v1, self).__init__(
            dim_room=(10, 10), max_steps=150, num_boxes=4,
            num_gen_steps=50
        )


class PushAndPull_Env_v2(PushAndPullSokobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array'],
    }

    def __init__(self):
        super(PushAndPull_Env_v2, self).__init__(
            dim_room=(7, 7), max_steps=150, num_boxes=2,
            num_gen_steps=50
        )


class PushAndPull_Env_v3(PushAndPullSokobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array'],
    }

    def __init__(self):
        super(PushAndPull_Env_v3, self).__init__(
            dim_room=(7, 7), max_steps=150, num_boxes=3,
            num_gen_steps=50
        )


class PushAndPull_Env_v4(PushAndPullSokobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array'],
    }

    def __init__(self):
        super(PushAndPull_Env_v4, self).__init__(
            dim_room=(13, 11), max_steps=300, num_boxes=4,
            num_gen_steps=50
        )


class PushAndPull_Env_v5(PushAndPullSokobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array'],
    }

    def __init__(self):
        super(PushAndPull_Env_v5, self).__init__(
            dim_room=(13, 11), max_steps=300, num_boxes=5,
            num_gen_steps=50
        )


class TwoPlayer_Env0(TwoPlayerSokobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array'],
    }

    def __init__(self):
        super(TwoPlayer_Env0, self).__init__(
            num_boxes=2, max_steps=200,
            dim_room=(7, 7)
        )


class TwoPlayer_Env1(TwoPlayerSokobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array'],
    }

    def __init__(self):
        super(TwoPlayer_Env1, self).__init__(
            num_boxes=3, max_steps=200,
            dim_room=(7, 7)
        )


class TwoPlayer_Env2(TwoPlayerSokobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array'],
    }

    def __init__(self):
        super(TwoPlayer_Env2, self).__init__(
            num_boxes=3, max_steps=200,
            dim_room=(10, 10)
        )


class TwoPlayer_Env3(TwoPlayerSokobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array'],
    }

    def __init__(self):
        super(TwoPlayer_Env3, self).__init__(
            num_boxes=4, max_steps=200,
            dim_room=(10, 10)
        )


class TwoPlayer_Env4(TwoPlayerSokobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array'],
    }

    def __init__(self):
        super(TwoPlayer_Env4, self).__init__(
            num_boxes=3, max_steps=200,
            dim_room=(13, 11)
        )



class TwoPlayer_Env5(TwoPlayerSokobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array'],
    }

    def __init__(self):
        super(TwoPlayer_Env5, self).__init__(
            num_boxes=4, max_steps=200,
            dim_room=(13, 11)
        )


class Boxban_Env0(BoxobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array'],
    }

    def __init__(self):
        super(Boxban_Env0, self).__init__(max_steps=200, difficulty='unfiltered', split='train')

class Boxban_Env0_val(BoxobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array'],
    }

    def __init__(self):
        super(Boxban_Env0_val, self).__init__(max_steps=200, difficulty='unfiltered', split='valid')

class Boxban_Env0_test(BoxobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array'],
    }

    def __init__(self):
        super(Boxban_Env0_test, self).__init__(max_steps=200, difficulty='unfiltered', split='test')

class Boxban_Env1(BoxobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array'],
    }

    def __init__(self):
        super(Boxban_Env1, self).__init__(max_steps=200, difficulty='medium')

class Boxban_Env1_val(BoxobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array'],
    }

    def __init__(self):
        super(Boxban_Env1_val, self).__init__(max_steps=200, difficulty='medium', split='valid')

# Push and Pull classes
class PushAndPullBoxban_Env0(PushAndPullBoxobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array'],
    }

    def __init__(self):
        super().__init__(max_steps=200, difficulty='unfiltered', split='train')

class PushAndPullBoxban_Env0_val(PushAndPullBoxobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array'],
    }

    def __init__(self):
        super().__init__(max_steps=200, difficulty='unfiltered', split='valid')

class PushAndPullBoxban_Env0_test(PushAndPullBoxobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array'],
    }

    def __init__(self):
        super().__init__(max_steps=200, difficulty='unfiltered', split='test')

class PushAndPullBoxban_Env1(PushAndPullBoxobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array'],
    }

    def __init__(self):
        super().__init__(max_steps=200, difficulty='medium')

class PushAndPullBoxban_Env1_val(PushAndPullBoxobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array'],
    }

    def __init__(self):
        super().__init__(max_steps=200, difficulty='medium', split='valid')


