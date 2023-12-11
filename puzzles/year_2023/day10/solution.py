import os
import re
from collections import deque

DOWN = (1, 0)
UP = (-1, 0)
RIGHT = (0, 1)
LEFT = (0, -1)

PIPES = {
    "|": [UP, DOWN],
    "-": [LEFT, RIGHT],
    "L": [UP, RIGHT],
    "J": [UP, LEFT],
    "7": [DOWN, LEFT],
    "F": [DOWN, RIGHT],
    ".": [],
}


def read_input(file_name: str) -> list[str]:
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, "r") as f:
        return f.read().splitlines()


def find_possible_source_alternative_value(grid, src_r, src_c):
    possible_s_values = set(PIPES) - {"."}
    if src_r == 0 or DOWN not in PIPES[grid[src_r - 1][src_c]]:
        possible_s_values -= set("|LJ")
    if src_r == len(grid) - 1 or UP not in PIPES[grid[src_r + 1][src_c]]:
        possible_s_values -= set("|7F")
    if src_c == 0 or RIGHT not in PIPES[grid[src_r][src_c - 1]]:
        possible_s_values -= set("-J7")
    if src_c == len(grid[0]) - 1 or LEFT not in PIPES[grid[src_r][src_c + 1]]:
        possible_s_values -= set("-LF")

    return possible_s_values.pop()


def parse_input(file_name):
    inputs = read_input(file_name)
    for row, line in enumerate(inputs):
        if "S" in line:
            col = line.index("S")
            break

    src_r, src_c = row, col
    s_value = find_possible_source_alternative_value(inputs, src_r, src_c)

    return {
        "grid": [line.replace("S", s_value) for line in inputs],
        "start_pos": (src_r, src_c),
    }


def get_neighbours(tile, pos, grid_size, grid):
    """
    | is a vertical pipe connecting north and south.
    - is a horizontal pipe connecting east and west.
    L is a 90-degree bend connecting north and east.
    J is a 90-degree bend connecting north and west.
    7 is a 90-degree bend connecting south and west.
    F is a 90-degree bend connecting south and east.
    . is ground; there is no pipe in this tile.
    S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
    """
    row, col = pos
    neighbours = []
    for r, c in PIPES[tile]:
        if 0 <= row + r <= grid_size[0] and 0 <= col + c <= grid_size[1]:
            new_pos = (row + r, col + c)
            neighbours.append(new_pos)

    return neighbours


def bfs(grid, start):
    queue = deque([start])
    visited = {start}
    grid_size = (len(grid), len(grid[0]))
    distances = {start: 0}
    total_dots = set()

    while queue:
        current = queue.popleft()
        neighbours = get_neighbours(grid[current[0]][current[1]], current, grid_size, grid)
        for neighbour in neighbours:
            if grid[neighbour[0]][neighbour[1]] == ".":
                total_dots.add(neighbour)
                continue

            if neighbour in visited:
                continue

            visited.add(neighbour)
            queue.append(neighbour)
            distances[neighbour] = distances[current] + 1

    return len(visited) // 2, visited


def solve_part1(inputs):
    total, visited = bfs(inputs["grid"], inputs["start_pos"])
    return total


def solve_part2(inputs):
    total, visited = bfs(inputs["grid"], inputs["start_pos"])
    enclosed_tiles = set()
    grid = []
    for i, line in enumerate(inputs["grid"]):
        row = []
        for j, tile in enumerate(line):
            if (i, j) in visited:
                row.append(tile)
            else:
                row.append(".")
        grid.append("".join(row))

    for i, line in enumerate(grid):
        line = re.sub("L-*J|F-*7", "", line)
        within = False
        for j, tile in enumerate(line):
            if tile in "|FL":
                within = not within

            if within and tile == ".":
                enclosed_tiles.add((i, j))

    return len(enclosed_tiles)


def solve(file_name, part=1):
    inputs = parse_input(file_name)
    if part == 1:
        return solve_part1(inputs)

    return solve_part2(inputs)


if __name__ == "__main__":
    assert solve("example1_part2.txt", part=2) == 4
    assert solve("example2_part2.txt", part=2) == 8
    assert solve("example3_part2.txt", part=2) == 10
    assert solve("input.txt", part=2) == 579
