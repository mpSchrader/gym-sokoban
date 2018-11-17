# Variation: Two Player

| Example Game 1 | Example Game 2 | Example Game 3 |
| :---: | :---: | :---: 
| ![Game 1](/docs/Animations/TwoPlayer_solved_0.gif?raw=true) | ![Game 2](/docs/Animations/TwoPlayer_solved_1.gif?raw=true) | ![Game 3](/docs/Animations/TwoPlayer_solved_2.gif?raw=true) |


## 1. Idea
This variation contains two different players in the room, which both can be moved like a regular single player.


## 2. Rules
Every round the user can choose which avatar (player) should be used. 
The player is chosen by the action number. 
All actions in the range from 0 to 7 are for player 1, the green avatar.
The remaining actions relate to player 2, the blue avatar.

 | Action (Player 1) | ID    |  | Action (Player 2) | ID    | 
 | ----------------- | :---: |--| ----------------- | :---: | 
 | P1: Push Up       |  0    |  | P2: Push Up       |  8    |  
 | P1: Push Down     |  1    |  | P2: Push Down     |  9    | 
 | P1: Push Left     |  2    |  | P2: Push Left     |  10   |  
 | P1: Push Right    |  3    |  | P2: Push Right    |  11   |    
 | P1: Move Up       |  4    |  | P2: Move Up       |  12   | 
 | P1: Move Down     |  5    |  | P2: Move Down     |  13   |
 | P1: Move Left     |  6    |  | P2: Move Left     |  14   |
 | P1: Move Right    |  7    |  | P2: Move Right    |  15   |


The game ending rules as well as the reward are similar to regular game. 

## 3. Room Configurations
Similar to the regular Sokoban there exist multiple room configurations. 
Of course all configurations can be rendered as TinyWorld.

| Room Id | Grid-Size | Pixels | #Boxes | Example | 
| ---     | :---:      | :---: | :---:   | :---: | 
| FixedTarget-Sokoban-v0 |  7x7  | 160x160 | 2 | ![TwoPlayer-Sokoban-v0](/docs/rooms/TwoPlayer-Sokoban-v0.png)  | 
| FixedTarget-Sokoban-v1 |  7x7  | 160x160 | 3 | ![TwoPlayer-Sokoban-v1](/docs/rooms/TwoPlayer-Sokoban-v1.png)   | 
| FixedTarget-Sokoban-v2 | 10x10 | 112x112 | 3 | ![TwoPlayer-Sokoban-v2](/docs/rooms/TwoPlayer-Sokoban-v2.png)  |
| FixedTarget-Sokoban-v3 | 10x10 | 112x112 | 4 | ![TwoPlayer-Sokoban-v3](/docs/rooms/TwoPlayer-Sokoban-v3.png)  |
| FixedTarget-Sokoban-v4 | 13x11 | 160x160 | 3 | ![TwoPlayer-Sokoban-v4](/docs/rooms/TwoPlayer-Sokoban-v4.png)  | 
| FixedTarget-Sokoban-v5 | 13x11 | 160x160 | 4 | ![TwoPlayer-Sokoban-v5](/docs/rooms/TwoPlayer-Sokoban-v5.png)   | 
