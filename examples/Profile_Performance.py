import cProfile
import gym
import gym_sokoban
import time
cProfile.run('gym.make("Sokoban-v1")', sort='time')

env = gym.make("Sokoban-v1")

start = time.time()
n = 200
for i in range(n):
    print('Reset {}/{}'.format(i+1, n))
    env.reset()

end = time.time()
delta = end-start
hours, remainder = divmod(delta, 3600)
minutes, seconds = divmod(remainder, 60)
print('Done.\nReset {} times in {}:{}:{}'.format(n, int(hours), int(minutes), int(seconds)))
hours, remainder = divmod(delta*1.0/n, 3600)
minutes, seconds = divmod(remainder, 60)
print('Avg {}:{}:{}'.format(int(hours), int(minutes), seconds))
