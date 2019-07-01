from setuptools import setup

setup(
      name='gym_sokoban',
      version='0.2.0',
      description='Sokoban environment for OpenAI Gym',
      install_requires=['gym>=0.2.3', 'numpy>=1.14.1', 'tqdm>=4.32.1', 'imageio>=2.5.0', 'requests>=2.22.0']
)
