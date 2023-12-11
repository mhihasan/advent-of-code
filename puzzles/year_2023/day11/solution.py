"""
Using Manhattan distance, find the sum of the shortest paths between all pairs of galaxies.
"""
import os
from itertools import combinations


def read_input(file_name: str) -> list[str]:
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, "r") as f:
        return f.read().splitlines()


def parse_input(file_name):
    return read_input(file_name)


def calculate_shortest_path(start, end, expansion_times, empty_rows, empty_cols):
    row_min, row_max = min(start[0], end[0]), max(start[0], end[0])
    col_min, col_max = min(start[1], end[1]), max(start[1], end[1])
    manhattan_distance = abs(start[0] - end[0]) + abs(start[1] - end[1])

    vertical_expansion = [expansion_times - 1 for r_index in range(row_min, row_max) if r_index in empty_rows]
    horizontal_expansion = [expansion_times - 1 for c_index in range(col_min, col_max) if c_index in empty_cols]

    return manhattan_distance + sum(vertical_expansion) + sum(horizontal_expansion)


def sum_of_shortest_paths(grid, expansion_times=2):
    galaxy_positions = [(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == "#"]
    empty_rows = [r for r, row in enumerate(grid) if "#" not in row]
    empty_cols = [c for c, col in enumerate(zip(*grid)) if "#" not in col]

    all_pair_shortest_paths = {
        pair: calculate_shortest_path(pair[0], pair[1], expansion_times, empty_rows, empty_cols)
        for pair in combinations(galaxy_positions, 2)
    }

    return sum(all_pair_shortest_paths.values())


def solve_part1(inputs):
    return sum_of_shortest_paths(inputs, expansion_times=2)


def solve_part2(inputs):
    return sum_of_shortest_paths(inputs, expansion_times=1000000)


def solve(file_name, part=1):
    inputs = parse_input(file_name)
    if part == 1:
        return solve_part1(inputs)

    return solve_part2(inputs)


if __name__ == "__main__":
    r = solve("input.txt", part=2)
