import random
import numpy as np
import pkg_resources
import marshal
from scipy import misc


def room_to_rgb(room, room_structure=None):
    """
    Creates an RGB image of the room.
    :param room:
    :param room_structure:
    :return:
    """
    resource_package = __name__

    room = np.array(room)
    if not room_structure is None:
        # Change the ID of a player on a target
        room[(room == 5) & (room_structure == 2)] = 6

    # Load images, representing the corresponding situation
    box_filename = pkg_resources.resource_filename(resource_package, '/'.join(('surface', 'box.png')))
    box = misc.imread(box_filename)

    box_on_target_filename = pkg_resources.resource_filename(resource_package,
                                                             '/'.join(('surface', 'box_on_target.png')))
    box_on_target = misc.imread(box_on_target_filename)

    box_target_filename = pkg_resources.resource_filename(resource_package, '/'.join(('surface', 'box_target.png')))
    box_target = misc.imread(box_target_filename)

    floor_filename = pkg_resources.resource_filename(resource_package, '/'.join(('surface', 'floor.png')))
    floor = misc.imread(floor_filename)

    player_filename = pkg_resources.resource_filename(resource_package, '/'.join(('surface', 'player.png')))
    player = misc.imread(player_filename)

    player_on_target_filename = pkg_resources.resource_filename(resource_package,
                                                                '/'.join(('surface', 'player_on_target.png')))
    player_on_target = misc.imread(player_on_target_filename)

    wall_filename = pkg_resources.resource_filename(resource_package, '/'.join(('surface', 'wall.png')))
    wall = misc.imread(wall_filename)

    surfaces = [wall, floor, box_target, box_on_target, box, player, player_on_target]

    # Assemble the new rgb_room, with all loaded images
    room_rgb = np.zeros(shape=(room.shape[0] * 16, room.shape[1] * 16, 3), dtype=np.uint8)
    for i in range(room.shape[0]):
        x_i = i * 16

        for j in range(room.shape[1]):
            y_j = j * 16
            surfaces_id = room[i, j]

            room_rgb[x_i:(x_i + 16), y_j:(y_j + 16), :] = surfaces[surfaces_id]

    return room_rgb


def room_to_tiny_world_rgb(room, room_structure=None, scale=1):

    room = np.array(room)
    if not room_structure is None:
        # Change the ID of a player on a target
        room[(room == 5) & (room_structure == 2)] = 6

    wall = [0, 0, 0]
    floor = [243, 248, 238]
    box_target = [254, 126, 125]
    box_on_target = [254, 95, 56]
    box = [142, 121, 56]
    player = [160, 212, 56]
    player_on_target = [219, 212, 56]

    surfaces = [wall, floor, box_target, box_on_target, box, player, player_on_target]

    # Assemble the new rgb_room, with all loaded images
    room_small_rgb = np.zeros(shape=(room.shape[0]*scale, room.shape[1]*scale, 3), dtype=np.uint8)
    for i in range(room.shape[0]):
        x_i = i * scale
        for j in range(room.shape[1]):
            y_j = j * scale
            surfaces_id = int(room[i, j])
            room_small_rgb[x_i:(x_i+scale), y_j:(y_j+scale), :] = np.array(surfaces[surfaces_id])

    return room_small_rgb


def room_to_rgb_FT(room, box_mapping, room_structure=None):
    """
    Creates an RGB image of the room.
    :param room:
    :param room_structure:
    :return:
    """
    resource_package = __name__

    room = np.array(room)
    if not room_structure is None:
        # Change the ID of a player on a target
        room[(room == 5) & (room_structure == 2)] = 6

    # Load images, representing the corresponding situation
    box_filename = pkg_resources.resource_filename(resource_package, '/'.join(('surface', 'box.png')))
    box = misc.imread(box_filename)

    box_on_target_filename = pkg_resources.resource_filename(resource_package,
                                                             '/'.join(('surface', 'box_on_target.png')))
    box_on_target = misc.imread(box_on_target_filename)

    box_target_filename = pkg_resources.resource_filename(resource_package, '/'.join(('surface', 'box_target.png')))
    box_target = misc.imread(box_target_filename)

    floor_filename = pkg_resources.resource_filename(resource_package, '/'.join(('surface', 'floor.png')))
    floor = misc.imread(floor_filename)

    player_filename = pkg_resources.resource_filename(resource_package, '/'.join(('surface', 'player.png')))
    player = misc.imread(player_filename)

    player_on_target_filename = pkg_resources.resource_filename(resource_package,
                                                                '/'.join(('surface', 'player_on_target.png')))
    player_on_target = misc.imread(player_on_target_filename)

    wall_filename = pkg_resources.resource_filename(resource_package, '/'.join(('surface', 'wall.png')))
    wall = misc.imread(wall_filename)

    surfaces = [wall, floor, box_target, box_on_target, box, player, player_on_target]

    # Assemble the new rgb_room, with all loaded images
    room_rgb = np.zeros(shape=(room.shape[0] * 16, room.shape[1] * 16, 3), dtype=np.uint8)
    for i in range(room.shape[0]):
        x_i = i * 16

        for j in range(room.shape[1]):
            y_j = j * 16

            surfaces_id = room[i, j]
            surface = surfaces[surfaces_id]
            if 1 < surfaces_id < 5:
                try:
                    surface = get_proper_box_surface(surfaces_id, box_mapping, i, j)
                except:
                    pass
            room_rgb[x_i:(x_i + 16), y_j:(y_j + 16), :] = surface

    return room_rgb


def get_proper_box_surface(surfaces_id, box_mapping, i, j):
    names = ["wall", "floor", "box_target", "box_on_target", "box", "player", "player_on_target"]
    print(names[surfaces_id])
    box_id = 0
    situation = ''

    if surfaces_id == 2:
        situation = '_target'
        box_id = list(box_mapping.keys()).index((i, j))
    elif surfaces_id == 3:
        box_id = list(box_mapping.values()).index((i, j))
        box_key = list(box_mapping.keys())[box_id]
        if box_key == (i, j):
            situation = '_on_target'
        else:
            situation = '_on_wrong_target'
        pass
    elif surfaces_id == 4:
        box_id = list(box_mapping.values()).index((i, j))

    surface_name = 'box{}{}.png'.format(box_id, situation)
    resource_package = __name__
    filename = pkg_resources.resource_filename(resource_package, '/'.join(('surface', 'multibox', surface_name)))
    surface = misc.imread(filename)

    return surface

TYPE_LOOKUP = {
    0: 'wall',
    1: 'empty space',
    2: 'box target',
    3: 'box on target',
    4: 'box not on target',
    5: 'player'
}

ACTION_LOOKUP = {
    0: 'push up',
    1: 'push down',
    2: 'push left',
    3: 'push right',
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
