from typing import Callable
from utils import get_input_lines

grid : list[list[str]] = [
    list[str](map(str, list[str](line)))
    for line in get_input_lines("4/puzzle_input.txt").split('\n')
    if line.strip()  # only include non-empty lines (got an empty list)
]

# Coordinates based on story below (column, row) / (x,y)
NEIGHBOURS = [
    (-1,-1),
    (0,-1),
    (1,-1),
    (-1,0),
    (1,0),
    (-1,1),
    (0,1),
    (1,1)
]

# To solve this I would think we need to keep track in each row the position and all the neighbours and check if that position has less than 4 adjacent rolls.
# The nice thing is we skip all "@" and only look at "." positions.
# We need to keep track of row and column position to calculate our neighbour squares.
# Also need to track the border indexes 
def forklift_access(grid: list[list[str]], amount_of_rolls: int, recursive: bool = False) -> int:
    MAX_GRID_HEIGHT: int = len(grid)
    MAX_GRID_LENGTH: int = len(grid[0])
    MIN_GRID: int = 0
    total_rolls: int = 0
    update_rolls: list[tuple[int,int]] = []

    for y in range(MAX_GRID_HEIGHT):
        for x in range(MAX_GRID_LENGTH):
            item = grid[y][x]
            if item == "@":
                toilet_rolls: list[tuple[int,int]] = []
                for neighbour in NEIGHBOURS:
                    new_x = x + neighbour[0]  # neighbour[0] is x (column)
                    new_y = y + neighbour[1]  # neighbour[1] is y (row)
                    if (new_y >= MIN_GRID and new_y < MAX_GRID_HEIGHT) and (new_x >= MIN_GRID and new_x < MAX_GRID_LENGTH):
                        neighbour_item = grid[new_y][new_x]
                        
                        if neighbour_item == "@":
                            toilet_rolls.append((new_y, new_x))

                if len(toilet_rolls) < amount_of_rolls:
                    # This roll is accessible, count it
                    total_rolls += 1
                    if recursive:
                        update_rolls.append((y, x))
    
    if recursive:
        for roll_pos in update_rolls:
            grid[roll_pos[0]][roll_pos[1]] = 'x'

    return total_rolls

def recursive_removal(fn: Callable[[list[list[str]], int, bool], int], grid: list[list[str]], amount_of_rolls: int) -> int:
    total_rolls: int = 0
    new_roll_removal: int = -1

    while new_roll_removal != 0:
        new_roll_removal = fn(grid, amount_of_rolls, True)
        total_rolls += new_roll_removal
    
    return total_rolls


def main():
    print("part one is:", forklift_access(grid, 4))
    print("part two is:", recursive_removal(forklift_access, grid, 4))

if __name__ == "__main__":
    main()