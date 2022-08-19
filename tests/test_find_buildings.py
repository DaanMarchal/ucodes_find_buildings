import pytest

from question_1 import find_buildings, neighbours


@pytest.mark.parametrize(
    "space, new_space, expected_result",
    [
        ((1, 1), (0, 1), True),
        ((1, 1), (1, 0), True),
        ((1, 1), (2, 1), True),
        ((1, 1), (1, 2), True),
        ((1, 1), (0, 0), False),
        ((1, 1), (2, 2), False),
        ((1, 1), (2, 0), False),
        ((1, 1), (0, 2), False),
    ],
)
def test_neighbours(space, new_space, expected_result):
    assert neighbours(space, new_space) == expected_result


@pytest.mark.parametrize(
    "input_map, expected_result",
    [
        ([["B"]], 1),
        ([["E"]], 0),
        ([["B", "E"], ["E", "B"]], 2),
        ([["B", "B"], ["B", "B"]], 1),
        (
            [
                ["B", "B", "B"],
                ["B", "E", "B"],
                ["E", "B", "B"],
            ],
            1,
        ),
        (
            [
                ["B", "B", "B"],
                ["B", "E", "B"],
                ["E", "E", "E"],
                ["E", "E", "B"],
                ["B", "E", "B"],
            ],
            3,
        ),
        ([["B", "A"], ["E", "B"]], -1),
    ],
)
def test_find_buildings(input_map, expected_result):
    assert expected_result == find_buildings(input_map)
