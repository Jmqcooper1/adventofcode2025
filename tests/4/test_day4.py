import pytest
from conftest import import_day

main = import_day(4)
forklift_access = main.forklift_access
recursive_removal = main.recursive_removal

@pytest.fixture
def test_grid():
    """Fixture providing test grid data as plain text with \\n on each line."""
    return "..@@.@@@@.\n@@@.@.@.@@\n@@@@@.@.@@\n@.@@@@..@.\n@@.@@@@.@@\n.@@@@@@@.@\n.@.@.@.@@@\n@.@@@.@@@@\n.@@@@@@@@.\n@.@.@@@.@.\n"

def grid(test_grid):
    grid: list[list[str]] = [
        list[str](map(str, list[str](line)))
        for line in test_grid.split('\n')
        if line.strip() 
    ]
    return grid


def test_grid_parsing(test_grid):
    expected_grid: list[list[str]] = [
        list("..@@.@@@@."),
        list("@@@.@.@.@@"),
        list("@@@@@.@.@@"),
        list("@.@@@@..@."),
        list("@@.@@@@.@@"),
        list(".@@@@@@@.@"),
        list(".@.@.@.@@@"),
        list("@.@@@.@@@@"),
        list(".@@@@@@@@."),
        list("@.@.@@@.@."),
    ]
    assert grid(test_grid) == expected_grid

def test_part_one(test_grid):
    assert isinstance(grid(test_grid), list) == True
    assert forklift_access(grid(test_grid), 4) == 13

def test_part_two(test_grid):
    assert recursive_removal(forklift_access, grid(test_grid), 4) == 43

