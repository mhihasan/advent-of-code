import os
from collections import defaultdict, deque


def read_input(file_name: str) -> list[str]:
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, "r") as f:
        return f.read().splitlines()


def parse_input(file_name):
    lines = read_input(file_name)
    source = (0, lines[0].index("."))
    destination = (len(lines) - 1, lines[-1].index("."))
    return {
        "grid": lines,
        "source": source,
        "destination": destination,
    }


UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

DIRECTIONS = {
    ">": [RIGHT],
    "<": [LEFT],
    "^": [UP],
    "v": [DOWN],
    ".": [UP, DOWN, LEFT, RIGHT],
}


def is_valid(pos, total_rows, total_cols):
    return 0 <= pos[0] < total_rows and 0 <= pos[1] < total_cols


def get_neighbours(grid, pos):
    neighbours = []
    total_rows = len(grid)
    total_cols = len(grid[0])

    for direction in DIRECTIONS[grid[pos[0]][pos[1]]]:
        new_pos = (pos[0] + direction[0], pos[1] + direction[1])
        if not is_valid(new_pos, total_rows, total_cols) or grid[new_pos[0]][new_pos[1]] == "#":
            continue

        neighbours.append(new_pos)

    return neighbours


def find_checkpoints(grid, start, end):
    checkpoints = [start, end]
    for r, line in enumerate(grid):
        for c, char in enumerate(line):
            if char == "#":
                continue
            neighbours = get_neighbours(grid, (r, c))
            if len(neighbours) > 2:
                checkpoints.append((r, c))

    return checkpoints


def build_compressed_graph(grid, checkpoints):
    """Builds a graph with checkpoints as nodes and distance between them as edges"""

    graph = defaultdict(dict)
    # Contract the paths between checkpoints using BFS
    for checkpoint in checkpoints:
        queue = deque([(checkpoint, 0)])
        visited = {checkpoint}
        while queue:
            pos, distance = queue.popleft()

            if pos != checkpoint and pos in checkpoints:
                graph[checkpoint][pos] = distance
                continue

            neighbours = get_neighbours(grid, pos)
            for neighbour in neighbours:
                if neighbour in visited:
                    continue

                visited.add(neighbour)
                queue.append((neighbour, distance + 1))

    return graph


visited_global = set()


def dfs(graph, node, target):
    """Finds the longest distance between node and target using DFS
    Returns -inf if target is not found
    Distance to target is 0 if node == target
    Distance to target is -inf if target is not found
    distance = max(distance, dfs(neighbour, target) + graph[node][neighbour])
    """
    if node == target:
        return 0

    max_distance = -1
    visited_global.add(node)

    for neighbour in graph[node]:
        if neighbour in visited_global:
            continue

        max_distance = max(max_distance, dfs(graph, neighbour, target) + graph[node][neighbour])

    visited_global.remove(node)  # backtrack

    return max_distance


def find_longest_distance(graph, source, destination):
    """Finds the longest distance between source and destination using DFS"""
    return dfs(graph, source, destination)


def solve_part1(inputs):
    checkpoints = find_checkpoints(inputs["grid"], start=inputs["source"], end=inputs["destination"])
    graph = build_compressed_graph(inputs["grid"], checkpoints)
    return find_longest_distance(graph, inputs["source"], inputs["destination"])


def solve_part2(inputs):
    pass


def solve(file_name, part=1):
    inputs = parse_input(file_name)
    if part == 1:
        return solve_part1(inputs)

    return solve_part2(inputs)


if __name__ == "__main__":
    # solve("demo_input.txt", part=1)
    solve("input.txt", part=1)
