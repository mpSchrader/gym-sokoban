# Variation: Boxoban

| Example Game 1 | Example Game 2 | Example Game 3 |
| :---: | :---: | :---: 
| ![Game 1](/docs/Animations/pushAndPull_solved_0.gif?raw=true) | ![Game 2](/docs/Animations/pushAndPull_solved_1.gif?raw=true) | ![Game 3](/docs/Animations/pushAndPull_solved_2.gif?raw=true) |

## 1. Idea
Instead of generating a new level on every reset operation, a pregenerated level is choosen randomly. When Boxoban is run for the first time the levels are downloaded from DeepMinds [Github repository](https://github.com/deepmind/boxoban-levels) and stored in the folder _.sokoban_cache_.


## 2. Rules
Same rules as the regular Sokoban game.

## 3. Room Configurations
Through the API we provide access to 'unfiltered' and 'medium' levels. The unflitered levels are split into a train, test, and validation set. Whereas the medium levels are only split into train and validation. For more details see DeepMind's [README.md](https://github.com/deepmind/boxoban-levels/blob/master/README.md).
Of course all configurations can be rendered as TinyWorld.

| Room Id | Grid-Size| Grid-Size | Pixels | #Boxes |  
| ---     | :---: | :---:      | :---: | :---:   |
| Boxoban-Train-v0      | unfiltered | 10x10 | 112x112 | 4 | ![Boxoban-v0](/docs/rooms/TwoPlayer-Sokoban-v3.png) |
| Boxoban-Test-v0 | unfiltered | 10x10 | 112x112 | 4 | ![Boxoban-v0](/docs/rooms/TwoPlayer-Sokoban-v3.png) |
| Boxoban-Val-v0  | unfiltered | 10x10 | 112x112 | 4 | ![Boxoban-v0](/docs/rooms/TwoPlayer-Sokoban-v3.png) |
| Boxoban-Train-v1      | medium     | 10x10 | 112x112 | 4 | ![Boxoban-v1](/docs/rooms/TwoPlayer-Sokoban-v3.png) |
| Boxoban-Val-v1  | medium     | 10x10 | 112x112 | 4 | ![Boxoban-v1](/docs/rooms/TwoPlayer-Sokoban-v3.png) |
