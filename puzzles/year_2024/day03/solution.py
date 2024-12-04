import os
import re


def read_input(file_name: str) -> list[str]:
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, "r") as f:
        return f.read()


def parse_input(file_name):
    inputs = read_input(file_name)
    return inputs


def extract_numbers_from_mul(string):
    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, string)
    return matches


def extract_operations(string):
    pattern = r"(mul\(\d+,\d+\))|(do\(\))|(don't\(\))"
    matches = re.findall(pattern, string)
    results = []
    for match in matches:
        if match[0]:
            numbers = extract_numbers_from_mul(match[0])
            results.append((int(numbers[0][0]), int(numbers[0][1])))
            # results.append((int(numbers[0][0]), int(numbers[0][1]))
        elif match[1]:
            results.append(match[1])
        elif match[2]:
            results.append(match[2])
    return results


def get_mul_operations(string):
    "GIven a string, give me list of all instances of `mul(X,Y)`, where X and Y are integers of 1-3 digits numbers using regular expression"
    import re

    return re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", string)


def solve_part1(inputs):
    multiplication_results = 0
    for line in inputs:
        all_operations = get_mul_operations(line)
        for op in all_operations:
            x, y = map(int, op)
            multiplication_results += x * y
    print(multiplication_results)
    return multiplication_results


def solve_part2(inputs):
    multiplication_results = 0
    all_operations = extract_operations(inputs)
    should_multiply = True
    for operation in all_operations:
        if operation in ["do()", "don't()"]:
            if operation == "don't()":
                should_multiply = False
            else:
                should_multiply = True
        if operation not in ["do()", "don't()"]:
            if should_multiply:
                print(operation)
                multiplication_results += int(operation[0]) * int(operation[1])

    return multiplication_results


def solve(file_name, part=1):
    inputs = parse_input(file_name)
    if part == 1:
        return solve_part1(inputs)

    return solve_part2(inputs)


if __name__ == "__main__":
    solve("input.txt", part=2)
