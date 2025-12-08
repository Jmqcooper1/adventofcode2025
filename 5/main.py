from utils import get_input_lines

def parse_ranges(lines: list[str]) -> list[tuple[int, int]]:
    ranges: list[tuple[int, int]] = []
    for line in lines:
        if not line.strip():
            continue
        start, end = map(int, line.split("-"))
        ranges.append((start, end))
    return ranges

def parse_ids(lines: list[str]) -> list[int]:
    ids: list[int] = []
    for line in lines:
        if line.strip():
            ids.append(int(line.strip()))
    return ids

def is_in_ranges(value: int, ranges: list[tuple[int, int]]) -> bool:
    return any(start <= value <= end for start, end in ranges)

def count_fresh_in_inventory(ids: list[int], ranges: list[tuple[int, int]]) -> int:
    return sum(1 for id_val in ids if is_in_ranges(id_val, ranges))

def count_total_fresh_ids(ranges: list[tuple[int, int]]) -> int:
    if not ranges:
        return 0
    
    sorted_ranges = sorted(ranges)
    merged: list[tuple[int, int]] = [sorted_ranges[0]]
    
    for start, end in sorted_ranges[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end + 1:
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))
    
    return sum(end - start + 1 for start, end in merged)

def main():
    input_lines: list[str] = get_input_lines("5/puzzle_input.txt").split('\n\n')
    fresh_ingredients: list[tuple[int, int]] = parse_ranges(input_lines[0].split('\n'))
    inventory_ids: list[int] = parse_ids(input_lines[1].split('\n'))
    
    part1_fresh = count_fresh_in_inventory(inventory_ids, fresh_ingredients)
    part2_total_fresh = count_total_fresh_ids(fresh_ingredients)
    
    print(f"Part 1 - Fresh IDs in inventory: {part1_fresh}")
    print(f"Part 2 - Total fresh IDs possible: {part2_total_fresh}")

if __name__ == "__main__":
    main()