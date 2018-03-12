import numpy as np
import random

def generate_room(dim=(13,13), p_change_directions=0.35, num_steps=10, num_boxes=3):
    """
    Generates a Sokoban room, represented by an integer matrix. The elements are encoded as follows:
    wall = 0
    empty space = 1
    box target = 2
    box not on target = 3
    box on target = 4
    player = 5
    :param dim:
    :param p_change_directions:
    :param num_steps:
    :return:
    """
    room = room_topology_generation(dim, p_change_directions, num_steps)
    room = place_boxes_and_player(room, num_boxes=num_boxes)


def room_topology_generation(dim=(10, 10), p_change_directions=0.35, num_steps=15):
        dim_x, dim_y = dim

        masks = [
            [
                [0, 0, 0],
                [1, 1, 1],
                [0, 0, 0]
            ],
            [
                [0, 1, 0],
                [0, 1, 0],
                [0, 1, 0]
            ],
            [
                [0, 0, 0],
                [1, 1, 0],
                [0, 1, 0]
            ],
            [
                [0, 0, 0],
                [1, 1, 0],
                [1, 1, 0]
            ],
            [
                [0, 0, 0],
                [0, 1, 1],
                [0, 1, 0]
            ]
        ]

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        direction = random.sample(directions, 1)[0]

        position = np.array([
            random.randint(1, dim_x - 1),
            random.randint(1, dim_y - 1)]
        )

        level = np.zeros(dim, dtype=int)

        for s in range(num_steps):

            # Change direction randomly
            if random.random() < p_change_directions:
                direction = random.sample(directions, 1)[0]

            # Update position
            position = position + direction
            position[0] = max(min(position[0], dim_x - 2), 1)
            position[1] = max(min(position[1], dim_y - 2), 1)

            # Set mask
            mask = random.sample(masks, 1)[0]
            mask_start = position - 1
            level[mask_start[0]:mask_start[0] + 3, mask_start[1]:mask_start[1] + 3] += mask

        level[level > 0] = 1
        level[:, [0, dim_y - 1]] = 0
        level[[0, dim_x - 1], :] = 0

        return level


def place_boxes_and_player(room, num_boxes=3):
    # Position Player
    possible_positions = np.where(room == 1)
    ind = np.random.randint(possible_positions[0].shape[0])
    player_position = possible_positions[0][ind], possible_positions[1][ind]
    room[player_position] = 5

    for n in range(num_boxes):
        possible_positions = np.where(room == 1)
        ind = np.random.randint(possible_positions[0].shape[0])
        box_position = possible_positions[0][ind], possible_positions[1][ind]
        room[box_position] = 4

    return room