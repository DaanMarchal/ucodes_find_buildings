def neighbours(space, new_space):
    row_diff = abs(space[0] - new_space[0])
    column_diff = abs(space[1] - new_space[1])
    if row_diff + column_diff == 1:
        return True
    return False


def reconsider(new_space, newly_extended_building, buildings_found):
    """
    Given a new_space (part of newly_extended_building),
    check whether it is also part of any other buildings.
    In that case we merge them into one and return the new list.

    we check
    :param new_space: Space which was found to be part of building newly_extended_building.
    :param newly_extended_building: Building which just had a new space added to it.
    :param buildings_found: Buildings found up until now.
    :return: Updated list of buildings.
    """
    neighbouring_buildings = []
    for index, building in enumerate(buildings_found):
        if not (building == newly_extended_building):
            for space in building:
                if neighbours(space, new_space):
                    neighbouring_buildings.append(building)
                    break
    if neighbouring_buildings:
        for neighbouring_building in neighbouring_buildings:
            for space in neighbouring_building:
                newly_extended_building.append(space)
            buildings_found.remove(neighbouring_building)
    return buildings_found


def add_new_space(new_space, buildings_found):
    for building in buildings_found:
        for space in building:
            if neighbours(space, new_space):
                building.append(new_space)
                # New space could be neighbour of more than one existing building
                return reconsider(new_space, building, buildings_found)
    buildings_found.append([new_space])
    return buildings_found


def find_buildings(input_map):
    """
    This function will return the number of buildings found in a given input map.
    It adds found building spaces to a building list:
     A: to an existing building if neighbours with a space from that building
     B: to a new building if not neighbouring a found building already.

    If A, we also check whether any of the spaces in the other buildings is a neighbour of the new space as well.
    In that case we can 'merge' the two buildings together.

    :param input_map: 2D Array consisting of "B" and "E" values.
    :return: number of buildings found (-1 if invalid input)
    """
    buildings_found = []
    for r_index, row in enumerate(input_map):
        for c_index, column in enumerate(row):
            value = input_map[r_index][c_index]
            if value == "B":
                buildings_found = add_new_space((r_index, c_index), buildings_found)
            elif not (value == "B" or value == "E"):
                return -1
    return len(buildings_found)
