import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

register(
    id='Sokoban-v0',
    entry_point='gym_sokoban.envs:SokobanEnv',
    max_episode_steps=200,
    reward_threshold=195.0,
)


