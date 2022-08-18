def is_top_left_corner(row_index, column_index, input_map):
    left = (row_index - 1, column_index)
    top = (row_index, column_index - 1)
    for neighbour in [left, top]:
        if neighbour[0] in range(len(input_map)) and neighbour[1] in range(
            len(input_map[0])
        ):
            value = input_map[neighbour[0]][neighbour[1]]
            if value == "B":
                return False
    return True


def find_buildings(input_map):
    """
    This function will return the number of buildings found in a given input map.
    Its counting strategy is based on the idea that each building only has one top left corner.

    :param input_map: 2D Array consisting of "B" and "E" values.
    :return: number of buildings found.
    """
    number_of_buildings = 0
    for r_index, row in enumerate(input_map):
        for c_index, column in enumerate(row):
            value = input_map[r_index][c_index]
            if value == "B" and is_top_left_corner(r_index, c_index, input_map):
                number_of_buildings += 1
            elif not (value == "B" or value == "E"):
                return -1
    return number_of_buildings
