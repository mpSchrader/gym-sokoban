import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

register(
    id='Sokoban-v0',
    entry_point='gym_sokoban.envs:SokobanEnv1',
    max_episode_steps=200
)

register(
    id='Sokoban-v1',
    entry_point='gym_sokoban.envs:SokobanEnv',
    max_episode_steps=250
)

register(
    id='Sokoban-v2',
    entry_point='gym_sokoban.envs:SokobanEnv2',
    max_episode_steps=250
)

register(
    id='Sokoban-small-v0',
    entry_point='gym_sokoban.envs:SokobanEnv_Small0',
    max_episode_steps=100
)

register(
    id='Sokoban-small-v1',
    entry_point='gym_sokoban.envs:SokobanEnv_Small1',
    max_episode_steps=100
)

register(
    id='Sokoban-large-v0',
    entry_point='gym_sokoban.envs:SokobanEnv_Large0',
    max_episode_steps=100
)

register(
    id='Sokoban-large-v1',
    entry_point='gym_sokoban.envs:SokobanEnv_Large1',
    max_episode_steps=250
)

register(
    id='Sokoban-large-v2',
    entry_point='gym_sokoban.envs:SokobanEnv_Large2',
    max_episode_steps=250
)

register(
    id='Sokoban-huge-v0',
    entry_point='gym_sokoban.envs:SokobanEnv_Huge0',
    max_episode_steps=200
)

register(
    id='TinyWorld-Sokoban-v0',
    entry_point='gym_sokoban.envs:TW_SokobanEnv0',
    max_episode_steps=200
)

register(
    id='TinyWorld-Sokoban-v1',
    entry_point='gym_sokoban.envs:TW_SokobanEnv1',
    max_episode_steps=200
)

register(
    id='TinyWorld-Sokoban-v2',
    entry_point='gym_sokoban.envs:TW_SokobanEnv2',
    max_episode_steps=200
)

register(
    id='TinyWorld-Sokoban-small-v0',
    entry_point='gym_sokoban.envs:TW_SokobanEnv_Small0',
    max_episode_steps=200
)

register(
    id='TinyWorld-Sokoban-small-v1',
    entry_point='gym_sokoban.envs:TW_SokobanEnv_Small1',
    max_episode_steps=200
)

register(
    id='TinyWorld-Sokoban-large-v0',
    entry_point='gym_sokoban.envs:TW_SokobanEnv_Large0',
    max_episode_steps=200
)

register(
    id='TinyWorld-Sokoban-large-v1',
    entry_point='gym_sokoban.envs:TW_SokobanEnv_Large1',
    max_episode_steps=200
)


register(
    id='TinyWorld-Sokoban-large-v2',
    entry_point='gym_sokoban.envs:TW_SokobanEnv_Large2',
    max_episode_steps=200
)


register(
    id='TinyWorld-Sokoban-huge-v0',
    entry_point='gym_sokoban.envs:TW_SokobanEnv_Huge0',
    max_episode_steps=200
)
