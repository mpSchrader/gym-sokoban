import gym
import gym_sokoban
from gym_sokoban.envs.room_utils import ACTION_LOOKUP
import time

# Before you can make a Sokoban Environment you need to call:
# import gym_sokoban
# This import statement registers all Sokoban environments
# provided by this package
#env = gym.make('Sokoban-v0')
env = gym.make('FixedTarget-Sokoban-v0')

for i_episode in range(1):#20
    observation = env.reset()

    for t in range(100):#100
        env.render(mode='human')
        action = env.action_space.sample()

        # Sleep makes the actions visible for users
        time.sleep(1)
        observation, reward, done, info = env.step(action)

        print(ACTION_LOOKUP[action], reward, done, info)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            env.render()
            break

time.sleep(10)
