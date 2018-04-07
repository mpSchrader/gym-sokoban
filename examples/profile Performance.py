import cProfile
import gym
import gym_sokoban
cProfile.run('gym.make("Sokoban-v1")', sort='time')