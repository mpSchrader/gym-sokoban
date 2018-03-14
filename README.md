# gym-sokoban 
**(WORK IN PROGRESS)**<br>
The repository implements the game Sokoban based on the rules presented [DeepMind's]() paper [Imagination Augmented Agents for Deep Reinforcement Learning](https://papers.nips.cc/paper/7152-imagination-augmented-agents-for-deep-reinforcement-learning). 
The room generation is random and therefor will allow to train Deep Neural Networks without overfitting on a set of predefined rooms.

## Game Enviroment
### Actions
The game provides 8 actions to interact with the environment. 
Push and Move actions into the directions Up, Down, Left and Right.
The mapping of the action numbers to the actual actions looks as follows

 | Action     | ID    | 
 | --------   | :---: | 
 | Push Up    | 0     |  
 | Push Down  | 1     | 
 | Push Left  | 2     |   
 | Push Right | 3     |   
 | Move Up    | 4     |
 | Move Down  | 5     |
 | Move Left  | 6     |
 | Move Right | 7     |
 
**Move** simply moves if there is a free field in the direction, which means no block or wall.
**Push** push tries to move an adjacent box, if the next field behind the box is free.
This means no chain pushing of boxes is possible.

### Rewards
Finishing the game by pushing all on the targets gives a reward of 10 in the last step. 
Also pushing a box on or off a target gives a reward of 1 respectively of -1. 
In addition a reward of -0.1 is given for every step, this penalizes solutions with many steps.

| Reason                    | Reward |
| ------------------------- | ----   |
| Performe Step             | -0.1   |
| Push Box on Target        |    1   |
| Push Box off Target       |   -1   |
| Push all boxes on targets |   10   |

### Level Generation

## Installation

```bash
cd gym-sokoban
pip install -e .
```
