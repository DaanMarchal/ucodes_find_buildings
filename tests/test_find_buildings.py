import pytest

from question_1 import find_buildings


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
        ([["B", "A"], ["E", "B"]], -1),
    ],
)
def test_find_buildings(input_map, expected_result):
    assert expected_result == find_buildings(input_map)
