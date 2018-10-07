from .sokoban_env import SokobanEnv
from .sokoban_env_fixed_targets import FixedTargetsSokobanEnv
from .sokoban_env_pull import PushAndPullSokobanEnv


class SokobanEnv1(SokobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array'],
    }

    def __init__(self):
        super(SokobanEnv1, self).__init__(
            num_boxes=3, max_steps=200
        )


class SokobanEnv2(SokobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array'],
    }

    def __init__(self):
        super(SokobanEnv2, self).__init__(
            num_boxes=5, max_steps=200, num_gen_steps=40
        )


class SokobanEnv_Small0(SokobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array'],
    }

    def __init__(self):
        super(SokobanEnv_Small0, self).__init__(
            dim_room=(7, 7), max_steps=200, num_boxes=2
        )


class SokobanEnv_Small1(SokobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array'],
    }

    def __init__(self):
        super(SokobanEnv_Small1, self).__init__(
            dim_room=(7, 7), max_steps=200, num_boxes=3
        )


class SokobanEnv_Large0(SokobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array'],
    }

    def __init__(self):
        super(SokobanEnv_Large0, self).__init__(
            dim_room=(13, 11), max_steps=300, num_boxes=3,
            num_gen_steps=43
        )


class SokobanEnv_Large1(SokobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array'],
    }

    def __init__(self):
        super(SokobanEnv_Large1, self).__init__(
            dim_room=(13, 11), max_steps=300, num_boxes=4,
            num_gen_steps=43
        )


class SokobanEnv_Large1(SokobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array'],
    }

    def __init__(self):
        super(SokobanEnv_Large1, self).__init__(
            dim_room=(13, 11), max_steps=300, num_boxes=5,
            num_gen_steps=43
        )


class SokobanEnv_Huge0(SokobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array'],
    }

    def __init__(self):
        super(SokobanEnv_Huge0, self).__init__(
            dim_room=(13, 13), max_steps=300, num_boxes=5,
            num_gen_steps=50
        )


class FixedTargets_Env_v0(FixedTargetsSokobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array'],
    }

    def __init__(self):
        super(FixedTargets_Env_v0, self).__init__(
            dim_room=(10, 10), max_steps=150, num_boxes=3,
            num_gen_steps=50
        )


class FixedTargets_Env_v1(FixedTargetsSokobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array'],
    }

    def __init__(self):
        super(FixedTargets_Env_v1, self).__init__(
            dim_room=(10, 10), max_steps=150, num_boxes=4,
            num_gen_steps=50
        )


class FixedTargets_Env_v2(FixedTargetsSokobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array'],
    }

    def __init__(self):
        super(FixedTargets_Env_v2, self).__init__(
            dim_room=(7, 7), max_steps=150, num_boxes=2,
            num_gen_steps=50
        )


class FixedTargets_Env_v3(FixedTargetsSokobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array'],
    }

    def __init__(self):
        super(FixedTargets_Env_v3, self).__init__(
            dim_room=(7, 7), max_steps=150, num_boxes=3,
            num_gen_steps=50
        )


class PushAndPull_Env_v0(PushAndPullSokobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array'],
    }

    def __init__(self):
        super(PushAndPull_Env_v0, self).__init__(
            dim_room=(10, 10), max_steps=150, num_boxes=3,
            num_gen_steps=50
        )


class PushAndPull_Env_v1(PushAndPullSokobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array'],
    }

    def __init__(self):
        super(PushAndPull_Env_v1, self).__init__(
            dim_room=(10, 10), max_steps=150, num_boxes=4,
            num_gen_steps=50
        )


class PushAndPull_Env_v2(PushAndPullSokobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array'],
    }

    def __init__(self):
        super(PushAndPull_Env_v2, self).__init__(
            dim_room=(7, 7), max_steps=150, num_boxes=2,
            num_gen_steps=50
        )


class PushAndPull_Env_v3(PushAndPullSokobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array'],
    }

    def __init__(self):
        super(PushAndPull_Env_v3, self).__init__(
            dim_room=(7, 7), max_steps=150, num_boxes=3,
            num_gen_steps=50
        )


class PushAndPull_Env_v4(PushAndPullSokobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array'],
    }

    def __init__(self):
        super(PushAndPull_Env_v4, self).__init__(
            dim_room=(13, 11), max_steps=300, num_boxes=4,
            num_gen_steps=50
        )


class PushAndPull_Env_v5(PushAndPullSokobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array'],
    }

    def __init__(self):
        super(PushAndPull_Env_v5, self).__init__(
            dim_room=(13, 11), max_steps=300, num_boxes=5,
            num_gen_steps=50
        )
