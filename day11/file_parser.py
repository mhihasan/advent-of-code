import os
import re
from collections import deque


def read_input(file_name: str) -> list[str]:
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, "r") as f:
        return f.read().splitlines()


def parse_starting_items(monkey_str):
    matches = re.search(r"Starting items: (\d+.*)", monkey_str).group(1).split(",")
    return [int(item) for item in matches]


def parse_operation(monkey_str):
    matches = re.search(r"Operation: new = (old|\d+) ([\+|\-|\*|\/]) (old|\d+)", monkey_str)

    return {
        "left_operand": matches.group(1) == "old" and "old" or int(matches.group(1)),
        "operator": matches.group(2),
        "right_operand": matches.group(3) == "old" and "old" or int(matches.group(3)),
    }


def parse_test(monkey_str):
    return {
        "divisible_by": int(re.search(r"Test: divisible by (\d+)", monkey_str).group(1)),
        "true": int(re.search(r"If true: throw to monkey (\d+)", monkey_str).group(1)),
        "false": int(re.search(r"If false: throw to monkey (\d+)", monkey_str).group(1)),
    }


def parse_monkey_no(monkey_str):
    return int(re.search(r"Monkey (\d+)", monkey_str).group(1))


def parse_input(file_name: str):
    lines = read_input(file_name)
    monkey_str_line_length = 6

    monkey_operations = {}

    for i in range(0, len(lines), monkey_str_line_length + 1):
        monkey_str = "\n".join(lines[i : i + monkey_str_line_length])
        monkey_no = parse_monkey_no(monkey_str)
        items = parse_starting_items(monkey_str)
        operation = parse_operation(monkey_str)
        test = parse_test(monkey_str)

        monkey_operations[monkey_no] = {
            "items": deque(items),
            "operation": operation,
            "test": test,
        }

    for m_no, ops in monkey_operations.items():
        print(f"<<<<<<<<<<<<< Monkey no: {m_no} >>>>>>>>>>>>>>>>>>>>")
        print(ops)
    return monkey_operations


if __name__ == "__main__":
    parse_input("demo_input.txt")
