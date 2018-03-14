# gym-sokoban 
The repository implements the game Sokoban based on the rules presented [DeepMind's]() paper [Imagination Augmented Agents for Deep Reinforcement Learning](https://papers.nips.cc/paper/7152-imagination-augmented-agents-for-deep-reinforcement-learning). 
The room generation is random and therefor will allow to train Deep Neural Networks without overfitting on a set of predefined rooms.

| Example Game 1 | Example Game 2 | Example Game 3 |
| :---: | :---: | :---: 
| ![Game 1](/docs/Animations/solved_3.gif?raw=true) | ![Game 2](/docs/Animations/solved_4.gif?raw=true) | ![Game 3](/docs/Animations/solved_5.gif?raw=true) |


## 1 Installation

```bash
cd gym-sokoban
pip install -e .
```

## 2 Game Environment

### 2.1 Room Elements
Every room consists of five main elements: walls, floor, boxes, box targets, and a player.They might have different states whether they overlap or not.

| Type       | State      | Graphic |
| ---        | -----      | :---: |
| Wall       | Static     | ![Wall](/gym_sokoban/envs/surface/wall.png "Wall") |
| Floor      | Empty      | ![Floor](/gym_sokoban/envs/surface/floor.png "Floor") |
| Box Target | Empty      | ![BoxTarget](/gym_sokoban/envs/surface/box_target.png "Box Target") |
| Box        | Off Target | ![BoxOffTarget](/gym_sokoban/envs/surface/box.png "Box") |
| Box        | On Target  | ![BoxOnTarget](/gym_sokoban/envs/surface/box_on_target.png "Box") |
| Player     | Off Target | ![PlayerOffTarget](/gym_sokoban/envs/surface/player.png "Player") |
| Player     | On Target  | ![PlayerOnTarget](/gym_sokoban/envs/surface/player_on_target.png "Player") |

### 2.2 Actions
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
In case there is no box at adjacent field, the player stays where he is.

### 2.3 Rewards
Finishing the game by pushing all on the targets gives a reward of 10 in the last step. 
Also pushing a box on or off a target gives a reward of 1 respectively of -1. 
In addition a reward of -0.1 is given for every step, this penalizes solutions with many steps.

| Reason                    | Reward |
| ------------------------- | ----:  |
| Performe Step             | -0.1   |
| Push Box on Target        |  1.0   |
| Push Box off Target       | -1.0   |
| Push all boxes on targets | 10.0   |

### 2.4 Level Generation
Every time a Sokoban environment is loaded or reset a new room is randomly generated.
The generation consists of 3 phases: Topology Generation, Placement of Targets and Players, and Reverse Playing.
#### 2.4.1 Topology Generation
To generate the basic topology of the room, consisting of walls and empty floor, is based on a random walk, which changes its direction at probability 0.35.
At every step centered at the current position a pattern of fields is set to empty spaces.
The patterns used can be found in [Figure 2](#topologyMask).
<div style="padding:20%">
  <p align="center">
    <img src="/docs/masks.png?raw=true">
  </p>
  <p align="center" id="topologyMask">
    Figure 2: Mask for creating topology
  </p>
</div>


#### 2.4.2 Placement of Targets
During this phase the player including all n box targets are placed on randomly chosen empty spaces.

#### 2.4.3 Reverse Playing
This is the crucial phase to  ensure a solvable room.
Now Sokoban is played in a reverse fashion, where a player can move and pull boxes.
The goal of this phase is to find the room state, with the highest room score, with a [Depth First Search](https://en.wikipedia.org/wiki/Depth-first_search).
For every room explored during the search is a room score is calculated with the equation shown below.
The equation is a heuristic approach to evaluate the difficulty of the room.
BoxSwaps counts the number of times a player changes the box to pull.
BoxDisplacement is the [Manhattan Distance](https://en.wikipedia.org/wiki/Manhattan_distance) between a specific box and it origin box target. 
As long as at least one box is on a target the RoomScore is always 0.
<div style="padding:10%">
  <p align="center">
   <img src="https://latex.codecogs.com/svg.latex?\Large&space;RoomScore&space;=&space;BoxSwaps&space;\times&space;\sum_{i&space;\in&space;Boxes}_{BoxDisplacement_{i}}" title="Room Score" />
  </p>
</div>

### 2.5 Room Configuration
The following room configurations are available:

| Room Id | With | Height | #Boxes | Example |
| --- | :---: | :---: | :---: | :---: |
| Sokoban-v0 | 10 | 10 | 3 | ![Sokoban-v0](/docs/rooms/Sokoban-v0.png)  |
| Sokoban-v1 | 10 | 10 | 4 | ![Sokoban-v1](/docs/rooms/Sokoban-v1.png) |
| Sokoban-v2 | 10 | 10 | 5 | ![Sokoban-v2](/docs/rooms/Sokoban-v2.png) |
| Sokoban-small-v0 | 7 | 7 | 2 |  ![Sokoban-small-v0](/docs/rooms/Sokoban-small-v0.png) |
| Sokoban-small-v1 | 7 | 7 | 3 | ![Sokoban-small-v1](/docs/rooms/Sokoban-small-v1.png) |
| Sokoban-large-v0 | 13 | 11 | 3 | ![Sokoban-large-v0](/docs/rooms/Sokoban-large-v0.png)
| Sokoban-large-v1 | 13 | 11 | 4 | ![Sokoban-large-v1](/docs/rooms/Sokoban-large-v1.png) |
| Sokoban-large-v2 | 13 | 11 | 5 | ![Sokoban-large-v2](/docs/rooms/Sokoban-large-v2.png) | 
| Sokoban-huge-v0 | 13 | 13 | 5 | ![Sokoban-huge-v0](/docs/rooms/Sokoban-huge-v0.png)

Please note that the larger rooms might take some time to be created, especially on a laptop.


## 3 Connect
Feel free to get in touch with me to talk about this or other projects. 
Either by creating an [issue](https://github.com/mpSchrader/gym-sokoban/issues) or mail me on [LinkedIn](https://www.linkedin.com/in/max-philipp-schrader/).
