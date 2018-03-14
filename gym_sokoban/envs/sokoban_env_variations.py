from .sokoban_env import SokobanEnv

class SokobanEnv1(SokobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array'],
        'video.frames_per_second': 1
    }

    def __init__(self):
        super(SokobanEnv1, self).__init__(
            num_boxes=3
        )


class SokobanEnv2(SokobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array'],
        'video.frames_per_second': 1
    }

    def __init__(self):
        super(SokobanEnv2, self).__init__(
            num_boxes=5, num_gen_steps=40
        )

class SokobanEnv_Small0(SokobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array'],
        'video.frames_per_second': 1
    }

    def __init__(self):
        super(SokobanEnv_Small0, self).__init__(
            dim_room=(7, 7), max_steps=200, num_boxes=2
        )


class SokobanEnv_Small1(SokobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array'],
        'video.frames_per_second': 1
    }

    def __init__(self):
        super(SokobanEnv_Small1, self).__init__(
            dim_room=(7, 7), max_steps=200, num_boxes=3
        )


class SokobanEnv_Large0(SokobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array'],
        'video.frames_per_second': 1
    }

    def __init__(self):
        super(SokobanEnv_Large0, self).__init__(
            dim_room=(13, 11), max_steps=300, num_boxes=3,
            num_gen_steps=43
        )

class SokobanEnv_Large1(SokobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array'],
        'video.frames_per_second': 1
    }

    def __init__(self):
        super(SokobanEnv_Large1, self).__init__(
            dim_room=(13, 11), max_steps=300, num_boxes=4,
            num_gen_steps=43
        )

class SokobanEnv_Large1(SokobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array'],
        'video.frames_per_second': 1
    }

    def __init__(self):
        super(SokobanEnv_Large1, self).__init__(
            dim_room=(13, 11), max_steps=300, num_boxes=5,
            num_gen_steps=43
        )

class SokobanEnv_Huge0(SokobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array'],
        'video.frames_per_second': 1
    }

    def __init__(self):
        super(SokobanEnv_Huge0, self).__init__(
            dim_room=(13, 13), max_steps=300, num_boxes=5,
            num_gen_steps=50
        )

