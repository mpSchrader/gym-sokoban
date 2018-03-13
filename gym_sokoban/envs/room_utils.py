import random

import numpy as np
import pkg_resources
from scipy import misc
from scipy.misc import toimage


def generate_room(dim=(13, 13), p_change_directions=0.35, num_steps=25, num_boxes=3, tries=4):
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
    room_state = np.zeros(shape=dim)
    room_structure = np.zeros(shape=dim)
    room = 0
    for t in range(tries):
        room = room_topology_generation(dim, p_change_directions, num_steps)
        room = place_boxes_and_player(room, num_boxes=num_boxes)

        # Room fixed represents all not movable parts of the room
        room_structure = np.copy(room)
        room_structure[room_structure == 5] = 1

        # Room structure represents the current state of the room including movable parts
        room_state = room.copy()
        room_state[room_state == 2] = 4

        room_state, score = reverse_playing(room_state, room_structure)
        room_state[room_state == 3] = 4

        if score > 0:
            break

    toimage(room_to_rgb(room, room_structure)).show(title='Before play')
    toimage(room_to_rgb(room_state, room_structure)).show(title='After play')

    return room_structure, room_state


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
    num_possible_positions = possible_positions[0].shape[0]

    if num_possible_positions <= num_boxes + 1:
        raise RuntimeError('Not enough free spots (#{}) to place 1 player and {} boxes.'.format(
            num_possible_positions,
            num_boxes)
        )

    ind = np.random.randint(num_possible_positions)
    player_position = possible_positions[0][ind], possible_positions[1][ind]
    room[player_position] = 5

    for n in range(num_boxes):
        possible_positions = np.where(room == 1)
        num_possible_positions = possible_positions[0].shape[0]

        ind = np.random.randint(num_possible_positions)
        box_position = possible_positions[0][ind], possible_positions[1][ind]
        room[box_position] = 2

    return room


explored_states = {}
num_boxes = 0


def reverse_playing(room_state, room_structure, search_depth=100):
    global explored_states, num_boxes

    actions = list(ACTION_LOOKUP.keys())

    box_mapping = {}
    box_locations = np.where(room_structure == 2)
    num_boxes = len(box_locations[0])
    for l in range(num_boxes):
        box = (box_locations[0][l], box_locations[1][l])
        box_mapping[box] = box

    # explored_states stores all room states found during search
    # key: matrix as string
    # values: room_score
    explored_states = {}
    depth_first_search(room_state, room_structure, box_mapping, box_swaps=0, last_pull=(-1, -1), ttl=200)

    max_score = 0
    for state in explored_states:
        score = explored_states[state]
        if score > max_score:
            max_score = score
            room_state = np.fromstring(state, dtype=int).reshape(room_structure.shape)

    return room_state, max_score


def depth_first_search(room_state, room_structure, box_mapping, box_swaps=0, last_pull=(-1, -1), ttl=300):
    global explored_states, num_boxes

    ttl -= 1
    if ttl <= 0:
        return

    state_string = room_state.tostring()
    if not (state_string in explored_states):
        room_score = box_swaps * box_displacement_score(box_mapping)
        if np.where(room_state == 2)[0].shape[0] != num_boxes:
            room_score = 0
            pass
        explored_states[state_string] = room_score

        for action in ACTION_LOOKUP.keys():
            room_state_next = room_state.copy()
            box_mapping_next = box_mapping.copy()
            room_state_next, box_mapping_next, last_pull_next = \
                    reverse_move(room_state_next, room_structure, box_mapping_next, last_pull, action)
            box_swaps_next = box_swaps
            if last_pull_next != last_pull:
                box_swaps_next += 1

            depth_first_search(room_state_next, room_structure, box_mapping_next, box_swaps_next, last_pull, ttl)

    pass


def reverse_move(room_state, room_structure, box_mapping, last_pull, action):
    player_position = np.where(room_state == 5)
    player_position = np.array([player_position[0][0], player_position[1][0]])

    change = CHANGE_COORDINATES[action % 4]
    next_position = player_position + change

    # Move possible
    if room_state[next_position[0], next_position[1]] in [1, 2]:
        # Move player
        room_state[player_position[0], player_position[1]] = room_structure[player_position[0], player_position[1]]
        room_state[next_position[0], next_position[1]] = 5

        # Perform pull
        if action < 4:
            possible_box_location = change[0] * -1, change[1] * -1
            possible_box_location += player_position

            if room_state[possible_box_location[0], possible_box_location[1]] in [3, 4]:
                room_state[player_position[0], player_position[1]] = 3
                room_state[possible_box_location[0], possible_box_location[1]] = room_structure[
                    possible_box_location[0], possible_box_location[1]]

                for k in box_mapping.keys():
                    if box_mapping[k] == (possible_box_location[0], possible_box_location[1]):
                        box_mapping[k] = (player_position[0], player_position[1])
                        last_pull = k
                        pass

    return room_state, box_mapping, last_pull


def box_displacement_score(box_mapping):
    score = 0

    for box_target in box_mapping.keys():
        box_location = np.array(box_mapping[box_target])
        box_target = np.array(box_target)
        dist = np.sum(np.abs(box_location - box_target))
        score += dist

    return score


def room_to_rgb(room, room_structure=None):
    resource_package = __name__

    room = np.array(room)
    if room_structure is None:
      print("ROOM IS NONE")

    room_rgb = np.zeros(shape=(room.shape[0] * 16, room.shape[1] * 16, 3), dtype=np.uint8)

    # Load images
    box_filename = pkg_resources.resource_filename(resource_package, '/'.join(('surface', 'box.png')))
    box = misc.imread(box_filename)

    box_on_target_filename = pkg_resources.resource_filename(resource_package, '/'.join(('surface', 'box_on_target.png')))
    box_on_target = misc.imread(box_on_target_filename)

    box_target_filename = pkg_resources.resource_filename(resource_package, '/'.join(('surface', 'box_target.png')))
    box_target = misc.imread(box_target_filename)

    floor_filename = pkg_resources.resource_filename(resource_package, '/'.join(('surface', 'floor.png')))
    floor = misc.imread(floor_filename)

    player_filename = pkg_resources.resource_filename(resource_package, '/'.join(('surface', 'player.png')))
    player = misc.imread(player_filename)

    player_on_target_filename = pkg_resources.resource_filename(resource_package, '/'.join(('surface', 'player_on_target.png')))
    player_on_target = misc.imread(player_on_target_filename)

    wall_filename = pkg_resources.resource_filename(resource_package, '/'.join(('surface', 'wall.png')))
    wall = misc.imread(wall_filename)

    surfaces = [wall, floor, box_target, box_on_target, box, player, player_on_target]

    for i in range(room.shape[0]):
        x_i = i * 16
        for j in range(room.shape[1]):
            y_j = j * 16
            surfaces_id = room[i, j]
            room_rgb[x_i:(x_i + 16), y_j:(y_j + 16), :] = surfaces[surfaces_id]

    return room_rgb


TYPE_LOOKUP = {
    0: 'wall',
    1: 'empty space',
    2: 'box target',
    3: 'box on target',
    4: 'box not on target',
    5: 'player'
}

ACTION_LOOKUP = {
    0: 'pull up',
    1: 'pull down',
    2: 'pull left',
    3: 'pull right',
    4: 'move up',
    5: 'move down',
    6: 'move left',
    7: 'move right',
}

# Moves are mapped to coordinate changes as follows
# 0: Move up
# 1: Move down
# 2: Move left
# 3: Move right
CHANGE_COORDINATES = {
    0: (-1, 0),
    1: (1, 0),
    2: (0, -1),
    3: (0, 1)
}
