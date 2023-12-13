import os
from functools import cache


def read_input(file_name: str) -> list[str]:
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, "r") as f:
        return f.read().splitlines()


def parse_input(file_name):
    inputs = read_input(file_name)
    return inputs


@cache
def count_arrangements(springs, groups):
    # No more springs or groups left, then it is a valid arrangement
    if len(springs) == 0:
        return len(groups) == 0

    # No more groups left, then check if there are no more damaged springs
    if len(groups) == 0:
        return "#" not in springs

    # If there are more springs than the sum of all groups, then no arrangement is possible
    if len(springs) < sum(groups):
        return 0

    # If the first spot is operational, then no arrangement is possible
    if springs[0] == ".":
        return count_arrangements(springs[1:], groups)

    # If the first spot is damaged, then check if it is the start of a new damaged spring group
    if springs[0] == "#":
        current_group_size = groups[0]
        # If any operational spring is found in the current group, then no arrangement is possible
        if "." in springs[:current_group_size]:
            return 0

        # If the spring after the current group is damaged, then no arrangement is possible
        if current_group_size < len(springs) and springs[current_group_size] == "#":
            return 0

        # Found a new damaged spring group, remove it and check remaining springs
        return count_arrangements(springs[current_group_size + 1 :], groups[1:])

    # If the first spring is unknown(?), count the arrangements assuming "#" and "." both
    return count_arrangements("#" + springs[1:], groups) + count_arrangements("." + springs[1:], groups)


def solve_part1(inputs):
    total = 0
    for line in inputs:
        springs, damaged_spring_groups = line.split(" ")
        damaged_spring_groups = tuple(int(i) for i in damaged_spring_groups.split(","))
        total += count_arrangements(springs, damaged_spring_groups)
    return total


def solve_part2(inputs):
    times = 5
    total = 0
    for line in inputs:
        springs, damaged_spring_groups = line.split(" ")
        springs = "?".join([springs] * times)
        damaged_spring_groups = tuple(int(i) for i in damaged_spring_groups.split(",")) * times
        total += count_arrangements(springs, damaged_spring_groups)
    return total


def solve(file_name, part=1):
    inputs = parse_input(file_name)
    if part == 1:
        return solve_part1(inputs)

    return solve_part2(inputs)


if __name__ == "__main__":
    solve("input.txt", part=1)
