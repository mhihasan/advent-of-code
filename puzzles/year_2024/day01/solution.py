import os
import re
from collections import Counter


def read_input(file_name: str) -> list[str]:
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, "r") as f:
        return f.read().splitlines()


def parse_input(file_name):
    inputs = read_input(file_name)
    return inputs


def read_lists(inputs):
    list_a = []
    list_b = []

    pattern = re.compile(r"\s*(\d+)\s+(\d+)\s*")

    for line in inputs:
        match = pattern.match(line)
        item_a, item_b = match.groups()
        list_a.append(int(item_a))
        list_b.append(int(item_b))
    return list_a, list_b


def solve_part1(inputs):
    list_a, list_b = read_lists(inputs)
    sorted_list_a = sorted(list_a)
    sorted_list_b = sorted(list_b)
    distance = 0
    for i in range(len(sorted_list_a)):
        distance += abs(sorted_list_a[i] - sorted_list_b[i])
    return distance


def solve_part2(inputs):
    similarity_score = 0
    list_a, list_b = read_lists(inputs)
    list_b_counts_by_items = Counter(list_b)
    for item in list_a:
        count_in_list_b = list_b_counts_by_items[item]
        similarity_score += count_in_list_b * item
    return similarity_score


def solve(file_name, part=1):
    inputs = parse_input(file_name)
    if part == 1:
        return solve_part1(inputs)

    return solve_part2(inputs)


if __name__ == "__main__":
    solve("input.txt", part=2)
