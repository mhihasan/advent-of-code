import operator
import os
import re


def read_input(file_name: str) -> list[str]:
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, "r") as f:
        return f.read().splitlines()


def parse_number(monkey_str):
    try:
        return int(monkey_str)
    except Exception:
        return None


def parse_operation(monkey_str):
    op = re.search(r"([\+|\-|\*|\/])", monkey_str).group(1)
    left, right = monkey_str.split(f" {op} ")
    return {
        "left_operand": left,
        "operator": {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}.get(op),
        "right_operand": right,
    }


def parse_input(file_name: str):
    lines = read_input(file_name)
    d = {}
    for line in lines:
        monkey, monkey_str = line.split(": ")
        val = parse_number(monkey_str)
        if val:
            d[monkey] = val
        else:
            d[monkey] = parse_operation(monkey_str)

        print(d[monkey])
    return d
