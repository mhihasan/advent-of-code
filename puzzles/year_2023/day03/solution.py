import os
from collections import defaultdict


def read_input(file_name: str) -> list[str]:
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, "r") as f:
        return f.read().splitlines()


def _is_adjacent_to_symbol(inputs, line, row, col):
    left = col - 1
    right = col + 1
    top = row - 1
    bottom = row + 1
    DIRECTIONS = [
        (top, left),
        (top, col),
        (top, right),
        (row, left),
        (row, right),
        (bottom, left),
        (bottom, col),
        (bottom, right),
    ]
    for r, c in DIRECTIONS:
        if r < 0 or c < 0 or r >= len(inputs) or c >= len(line):
            continue
        if inputs[r][c] == "." or inputs[r][c].isdigit():
            continue

        return True

    # if left >= 0 and not inputs[row][left].isdigit() and inputs[row][left] != ".":
    #     return True
    # if right < len(line) and not inputs[row][right].isdigit() and inputs[row][right] != ".":
    #     return True
    # if top >= 0 and not inputs[top][col].isdigit() and inputs[top][col] != ".":
    #     return True
    # if bottom < len(inputs) and not inputs[bottom][col].isdigit() and inputs[bottom][col] != ".":
    #     return True


def _find_part_numbers(inputs, line, line_row):
    col = 0
    numbers = []
    line = list(line)
    part_numbers = []
    while col < len(line):
        adjacent = line[col].isdigit() and _is_adjacent_to_symbol(inputs, line, line_row, col)
        if adjacent:
            digits = []
            while numbers:
                digit = numbers.pop()
                if digit.isdigit():
                    digits.append(digit)
                else:
                    break
            digits.reverse()

            while col < len(line) and line[col].isdigit():
                digits.append(line[col])
                col += 1

            part_number = int("".join(digits))
            part_numbers.append(part_number)
        else:
            numbers.append(line[col])
            col += 1

    return part_numbers


def _is_adjacent_to_digit(inputs, line, directions):
    for r, c in directions:
        if r < 0 or c < 0 or r >= len(inputs) or c >= len(line):
            continue
        if inputs[r][c].isdigit():
            return {"row": r, "col": c}


def _collect_number(inputs, row, col, visited):
    line = inputs[row]
    temp_col = col
    digits = []
    while temp_col - 1 >= 0 and line[temp_col - 1].isdigit():
        digits.append(line[temp_col - 1])
        visited.add((row, temp_col - 1))
        temp_col -= 1
    digits.reverse()

    while col < len(line) and line[col].isdigit():
        digits.append(line[col])
        visited.add((row, col))
        col += 1

    return int("".join(digits)), visited


def _find_part_numbers_near_symbol(inputs, line, line_row, calculate_gear_ratios=False):
    numbers = []
    col = 0
    gear_ratios = []
    symbol_numbers = defaultdict(list)
    while col < len(line):
        if line[col].isdigit() or line[col] == ".":
            col += 1
            continue

        UP_DIRECTIONS = [(line_row - 1, col - 1), (line_row - 1, col), (line_row - 1, col + 1)]
        DOWN_DIRECTIONS = [(line_row + 1, col - 1), (line_row + 1, col), (line_row + 1, col + 1)]
        LEFT_DIRECTIONS = [(line_row, col - 1)]
        RIGHT_DIRECTIONS = [(line_row, col + 1)]

        visited = set()

        for direction in UP_DIRECTIONS + DOWN_DIRECTIONS + LEFT_DIRECTIONS + RIGHT_DIRECTIONS:
            if direction in visited:
                continue
            if direction[0] < 0 or direction[1] < 0 or direction[0] >= len(inputs) or direction[1] >= len(line):
                continue
            if inputs[direction[0]][direction[1]].isdigit():
                location = {"row": direction[0], "col": direction[1]}
                number, visited = _collect_number(inputs, location["row"], location["col"], visited)
                if calculate_gear_ratios and line[col] == "*":
                    symbol_numbers[(line_row, col)].append(number)
                else:
                    symbol_numbers[(line_row, col)].append(number)

        col += 1

    numbers = []
    for symbol, symbol_numbers in symbol_numbers.items():
        if calculate_gear_ratios and len(symbol_numbers) == 2:
            gear_ratios.append(symbol_numbers[0] * symbol_numbers[1])
        else:
            numbers.extend(symbol_numbers)

    return gear_ratios if calculate_gear_ratios else numbers


def solve_part1(inputs):
    sum_of_parts = 0
    for line_row, line in enumerate(inputs):
        # part_numbers = _find_part_numbers(inputs, line, line_row)
        part_numbers = _find_part_numbers_near_symbol(inputs, line, line_row, calculate_gear_ratios=False)
        sum_of_parts += sum(part_numbers)
    return sum_of_parts


def solve_part2(inputs):
    total = 0
    for line_row, line in enumerate(inputs):
        part_numbers = _find_part_numbers_near_symbol(inputs, line, line_row, calculate_gear_ratios=True)
        total += sum(part_numbers)
    return total


def solve(file_name, part=1):
    inputs = read_input(file_name)
    if part == 1:
        return solve_part1(inputs)

    return solve_part2(inputs)


if __name__ == "__main__":
    r = solve("input.txt", part=1)
    # r = solve("input.txt", part=1)
    print(r)
