import gym
import gym_sokoban
from gym_sokoban.envs.room_utils import ACTION_LOOKUP
import time
import cv2

ts = time.time()
env = gym.make('FixedTarget-Sokoban-v0')
#env = gym.make('TinyWorld-Sokoban-small-v0')


def print_avilable_actions():
    """
    Prints all available actions nicely formatted..
    :return:
    """
    available_actions_list = []
    for i in range(len(ACTION_LOOKUP)):
        available_actions_list.append(
            'Key: {} - Action: {}'.format(i, ACTION_LOOKUP[i])
        )
    display_actions = '\n'.join(available_actions_list)
    print()
    print('Action out of Range!')
    print('Available Actions:\n{}'.format(display_actions))
    print()


for i_episode in range(4):
    print('Starting new game!')
    observation = env.reset()

    for t in range(300):
        env.render()

        action = input('Select action: ')
        try:
            action = int(action)

            if not action in range(len(ACTION_LOOKUP)):
                raise ValueError

        except ValueError:
            print_avilable_actions()
            continue

        observation, reward, done, info = env.step(action)
        print(ACTION_LOOKUP[action], reward, done, info)
        cv2.imwrite('messigray.png', observation)

        if done:
            print("Episode finished after {} timesteps".format(t+1))
            env.render()
            break


time.sleep(10)
