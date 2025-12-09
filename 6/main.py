from utils import get_input_lines
from math import prod
from collections.abc import Callable

def calculate_cephalopod_math(inputs: list[int], operator: str) -> int:
    if operator == "*":
        return prod(inputs)
    return sum(inputs)

def parse_input(input_lines: list[str], column_reader: Callable[[list[str]], tuple[list[list[int]], list[str]]] | None = None) -> tuple[list[list[int]], list[str]]:
    if column_reader:
        return column_reader(input_lines)
    
    # Default: horizontal parsing (space-separated numbers)
    inputs: list[list[int]] = [
        [int(num) for num in line.strip().split() if num]
        for line in input_lines[:-1]
        if line.strip()
    ]
    operators: list[str] = [
        op for op in input_lines[-1].strip().split() if op
    ]
    return inputs, operators

def read_columns_vertically(input_lines: list[str]) -> tuple[list[list[int]], list[str]]:
    number_lines = [line for line in input_lines[:-1] if line.strip()]
    operator_line = input_lines[-1]
    max_len = max(len(line) for line in number_lines + [operator_line])
    padded = [line.ljust(max_len) for line in number_lines]
    operator_line = operator_line.ljust(max_len)
    
    columns = [''.join(row[i] for row in padded) for i in range(max_len)]
    
    problems, operators, current = [], [], []
    for i, col in enumerate(columns):
        digits = col.replace(' ', '')
        if digits:
            current.append(int(digits))
        elif current:
            problems.append(current)
            current = []
        if operator_line[i] in '*+':
            operators.append(operator_line[i])
    
    if current:
        problems.append(current)
    
    return problems, operators

def main():
    input_lines: list[str] = get_input_lines("6/puzzle_input.txt").split('\n')
    
    inputs, operators = parse_input(input_lines)
    total_sum_part_1 = sum(
        calculate_cephalopod_math([row[i] for row in inputs], operators[i])
        for i in range(len(operators))
    )
    print(total_sum_part_1)
    
    inputs, operators = parse_input(input_lines, read_columns_vertically)
    total_sum_part_2 = sum(
        calculate_cephalopod_math(group, operators[i])
        for i, group in enumerate(inputs)
    )
    print(total_sum_part_2)

if __name__ == "__main__":
    main()