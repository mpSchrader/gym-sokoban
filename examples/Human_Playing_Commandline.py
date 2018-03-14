import gym
import gym_sokoban
from gym_sokoban.envs.room_utils import ACTION_LOOKUP
import time

ts = time.time()
env = gym.make('Sokoban-small-v1')

available_actions_list = []
for i in range(len(ACTION_LOOKUP)):
    available_actions_list.append(
        'Key: {} - Action: {}'.format(i, ACTION_LOOKUP[i])
    )
display_actions = '\n'.join(available_actions_list)

for i_episode in range(1):
    observation = env.reset()
    observation = env.render(mode='rgb_array')

    for t in range(300):
        env.render()

        action = input('Select action: ')
        try:
            action = int(action)
            if not action in range(len(ACTION_LOOKUP)):
                print()
                print('Action out of Range!')
                print('Available Actions:\n{}'.format(display_actions))
                print()
                continue
        except ValueError:
            print()
            print('No Integer entered!')
            print('Available Actions:\n{}'.format(display_actions))
            print()
            continue

        observation, reward, done, info = env.step(action)
        print(ACTION_LOOKUP[action], reward, done, info)

        if done:
            print("Episode finished after {} timesteps".format(t+1))
            env.render()
            time.sleep(10)
            break

