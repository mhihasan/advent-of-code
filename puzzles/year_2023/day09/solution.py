import os
from itertools import pairwise


def read_input(file_name: str) -> list[str]:
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, "r") as f:
        return f.read().splitlines()


def parse_input(file_name):
    inputs = read_input(file_name)
    data = []
    for line in inputs:
        data.append([int(i) for i in line.split(" ")])
    return data


def extrapolate_forward_value(sequences):
    last_val = 0
    s = len(sequences) - 2
    while s > -1:
        last_val = sequences[s][-1] + last_val
        s -= 1

    return last_val


def extrapolate_backward_value(sequences):
    last_val = 0
    s = len(sequences) - 2
    while s > -1:
        last_val = sequences[s][0] - last_val
        s -= 1

    return last_val


def deal_with_line(line, func):
    a = [line]
    while True:
        i = 0

        inner = []
        while i < len(line) - 1:
            v = line[i + 1] - line[i]
            inner.append(v)
            i += 1

        line = inner
        a.append(line)

        if all([i == 0 for i in line]):
            break

    return func(a)


def extrapolate(lst, direction="forward"):
    if all([i == 0 for i in lst]):
        return 0

    diff = [b - a for a, b in pairwise(lst)]

    if direction == "backward":
        return lst[0] - extrapolate(diff, direction="backward")

    return lst[-1] + extrapolate(diff, direction="forward")


def solve_part1(inputs):
    s = 0
    for line in inputs:
        # s += deal_with_line(line, func=extrapolate_forward_value)
        s += extrapolate(line, direction="forward")
    return s


def solve_part2(inputs):
    s = 0
    for line in inputs:
        # s += deal_with_line(line, func=extrapolate_backward_value)
        s += extrapolate(line, direction="backward")
    return s


def solve(file_name, part=1):
    inputs = parse_input(file_name)
    if part == 1:
        return solve_part1(inputs)

    return solve_part2(inputs)


if __name__ == "__main__":
    solve("demo_input.txt", part=1)
