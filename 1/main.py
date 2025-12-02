from utils import get_input_lines, split_string_by_delimiter

# moves in direction and gives the new position back given the range of positions the dial can be in. (0-99)
def next_position(direction: str, distance: int, current_position: int) -> int:
    if direction == "R":
        return (current_position + distance) % 100
    return (current_position - distance) % 100


def zero_visits_during_rotation(direction: str, distance: int, current_position: int) -> int:
    if direction == "R":
        return (current_position + distance - 1) // 100
    return (distance - (current_position or 100) + 99) // 100

def main():
    current_position : int = 50
    counter_zero_landings : int = 0
    counter_total_zero_visits : int = 0
    rotations : list[tuple[str, int]] = [(line[0], int(line[1:])) for line in split_string_by_delimiter(get_input_lines("1/puzzle_input.txt"), "\n")]
    for direction, distance in rotations:
        during_rotation_visits = zero_visits_during_rotation(direction, distance, current_position)
        current_position = next_position(direction, distance, current_position)
        
        landed_at_zero = current_position == 0
        if landed_at_zero:
            counter_zero_landings += 1
        
        # Part 2: total = intermediate visits during rotation + being at 0
        counter_total_zero_visits += during_rotation_visits + (1 if landed_at_zero else 0)
    
    print(f"Part 1 (landings at 0): {counter_zero_landings}")
    print(f"Part 2 (total visits to 0): {counter_total_zero_visits}")

if __name__ == "__main__":
    main()