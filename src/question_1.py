import copy


def neighbours(space, new_space):
    row_diff = abs(space[0] - new_space[0])
    column_diff = abs(space[1] - new_space[1])
    if row_diff + column_diff == 1:
        return True
    return False


def add_new_space(row_index, column_index, buildings_found):
    buildings_found_copy = copy.deepcopy(buildings_found)
    new_space = (row_index, column_index)
    for building in buildings_found_copy:
        for space in building:
            if neighbours(space, new_space):
                building_index = buildings_found.index(building)
                buildings_found[building_index].append(new_space)
                return buildings_found
    buildings_found.append([new_space])
    return buildings_found


def find_buildings(input_map):
    """
    This function will return the number of buildings found in a given input map.
    It adds found building spaces to a building list:
     - to an existing building if neighbours with a space from that building
     - to a new building if not neighbouring a found building already.

    :param input_map: 2D Array consisting of "B" and "E" values.
    :return: number of buildings found.
    """
    buildings_found = []
    for r_index, row in enumerate(input_map):
        for c_index, column in enumerate(row):
            value = input_map[r_index][c_index]
            if value == "B":
                buildings_found = add_new_space(r_index, c_index, buildings_found)
            elif not (value == "B" or value == "E"):
                return -1
    return len(buildings_found)
