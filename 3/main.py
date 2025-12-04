from math import pow
from utils import get_input_lines

def find_largest_two_digits(bank: list[int]) -> int:
    tenth_magnitude : int = bank[0]
    first_magnitude : int = bank[1]
    
    for index in range(2, len(bank)):
        if first_magnitude > tenth_magnitude and index < len(bank):
            tenth_magnitude = first_magnitude
            first_magnitude = bank[index]
        if bank[index] > first_magnitude:
            first_magnitude = bank[index]

    return tenth_magnitude * 10 + first_magnitude

# Idea: what if you calculate the total the furthest the digit can be with constraint that we need twelve in a row?
# this means that if total length of the bank is 16 then the furthest position (index) the first bank can be for the bank is 4th (3 with count 0)
# then all the next ones are automatically set
# if your first stays there, the second one has a stretch of 4 to move. 
# So basically we just keep in check within the room to move and wiggle if there is anything bigger, as soon as we dont have wiggle room we know the rest 
def find_largest_x_digits(bank: list[int], total_batteries: int) -> int:
    wiggle_room : int = len(bank) - total_batteries
    index : int = 0
    magnitude : int = total_batteries
    largest_battery : int = 0

    while index < len(bank) and magnitude > 0:
        remaining_digits_needed = magnitude - 1
        max_lookahead = min(wiggle_room, len(bank) - index - remaining_digits_needed - 1)
        
        current_indexed = bank[index]
        added_index = 0
        
        if max_lookahead > 0:
            for i in range(1, max_lookahead + 1):
                if index + i < len(bank):
                    next_position = bank[index + i]
                    if next_position > current_indexed:
                        current_indexed = next_position
                        added_index = i
        
        wiggle_room -= added_index
        index += added_index + 1
        magnitude -= 1
        largest_battery += int(pow(10, magnitude)) * current_indexed
    
    return largest_battery


def main():
    banks : list[list[int]] = [
        list[int](map(int, list[str](line)))
        for line in get_input_lines("3/puzzle_input.txt").split('\n')
        if line.strip()  # only include non-empty lines (got an empty list)
    ]
    largest_two_digits : list[int] = [find_largest_x_digits(bank, 2) for bank in banks]
    largest_twelve_digits : list[int] = [find_largest_x_digits(bank, 12) for bank in banks]
    print(f"Part 1 (sum of largest two digits): {sum(largest_two_digits)}")
    print(f"Part 2 (sum of largest twelve digits): {sum(largest_twelve_digits)}")

if __name__ == "__main__":
    main()