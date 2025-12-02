from utils import get_input_lines, split_string_by_delimiter

def create_ids_from_file(file_path: str) -> list[int]:
    input_lines : list[str] = split_string_by_delimiter(get_input_lines(file_path), ",")
    ids : list[int] = []
    for line in input_lines:
        id_ranges : list[int] = list[int](range(int(line.split("-")[0]), int(line.split("-")[1]) + 1)) 
        ids.extend(id_ranges)
    return ids

# part one solution (later made into one function for part two)
# def check_invalid_id(id: str) -> bool:
#     # base case leading zeros are invalid
#     if id[0] == "0":
#         return True
    
#     # part 1: invalid ids are ids with same pattern of digits repeating, so even numbers
#     right_part : str = id[len(id) // 2:]
#     left_part : str = id[:len(id) // 2]
#     if left_part == right_part:
#         return True
    
#     return False

# part two suggests that invalid ids are ids that some sequence of digits repeats atleast twice. Instead of only twice.
def check_invalid_id(id: str, max_repeats: int = -1) -> bool:
    # leading zero is base case false
    if id[0] == "0":
        return True

    # check through the following logic:
    # atleast twice repeated means start from len(id) / 2 range. then we check bigger and bigger later on 
    # example is that length is 8, then we check sections of 4 first, then 3 (which is not possible), then 2, then 1 on repeated sequence throughout the whole string.
    # modulo is used to check if the sequence length is an integer.
    repeats = 2
    while repeats <= len(id) and (max_repeats == -1 or repeats <= max_repeats):
        if len(id) % repeats == 0:
            sequence_length = len(id) // repeats
            # print(f"current sequence length to check {sequence_length}, meaning it will repeat {repeats} times")
            sequences: list[str] = [id[i:i+sequence_length] for i in range(0, len(id), sequence_length)]
            if len(set[str](sequences)) == 1:
                return True
        repeats += 1

    return False

def main():
    ids : list[str] = create_ids_from_file("2/puzzle_input.txt")
    total_invalid_id_sum_part_one : int = 0
    total_invalid_id_sum_part_two : int = 0
    # ids = [11,22,99,111,999,1010,1188511885,222222,446446,38593859,565656,824824824,2121212121] # example cases in aoc
    for id in ids:
        if check_invalid_id(str(id), 2):
            total_invalid_id_sum_part_one += id
        if check_invalid_id(str(id)):
            total_invalid_id_sum_part_two += id
    print(f"Part 1 (total invalid id sum): {total_invalid_id_sum_part_one}")
    print(f"Part 2 (total invalid id sum): {total_invalid_id_sum_part_two}")

if __name__ == "__main__":
    main()