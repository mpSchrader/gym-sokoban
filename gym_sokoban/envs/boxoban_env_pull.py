from .sokoban_env_pull import PushAndPullSokobanEnv
from .boxoban_env import BoxobanEnv


class PushAndPullBoxobanEnv(BoxobanEnv,PushAndPullSokobanEnv):
    def __init__(self,
        dim_room=(10, 10),
        max_steps=120,
        num_boxes=3,
        num_gen_steps=None,
        difficulty='unfiltered',
        split='train'):
        super().__init__(dim_room=dim_room,
                max_steps=max_steps,
                num_boxes=num_boxes,
                num_gen_steps=num_gen_steps,
                difficulty=difficulty,
                split=split)
