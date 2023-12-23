import os
from collections import deque, defaultdict


def read_input(file_name: str) -> list[str]:
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, "r") as f:
        return f.read().splitlines()


def parse_input(file_name):
    inputs = read_input(file_name)
    start = None
    for r, line in enumerate(inputs):
        for c, char in enumerate(line):
            if char == "S":
                start = (r, c)
                break

    assert start is not None
    return {
        "grid": inputs,
        "start": start,
    }


UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)


def get_neighbours(grid, pos):
    neighbours = []
    for direction in [UP, DOWN, LEFT, RIGHT]:
        new_pos = (pos[0] + direction[0], pos[1] + direction[1])
        is_valid = 0 <= new_pos[0] < len(grid) and 0 <= new_pos[1] < len(grid[0])

        if is_valid and grid[new_pos[0]][new_pos[1]] != "#":
            neighbours.append(new_pos)

    return neighbours


def print_grid(grid, visited):
    for r, line in enumerate(grid):
        for c, char in enumerate(line):
            if (r, c) in visited:
                print("0", end="")
            else:
                print(char, end="")
        print()


def bfs(grid, start, depth_allowed=64):
    queue = deque([(start, 0)])
    distances = {start: 0}
    depth_nodes = defaultdict(list)

    while queue:
        pos, depth = queue.popleft()

        if depth == depth_allowed:
            print("total", len(depth_nodes[depth]))
            break

        neighbours = get_neighbours(grid, pos)
        for neighbour in neighbours:
            if neighbour not in depth_nodes[depth + 1]:
                # visited.add(neighbour)
                depth_nodes[depth + 1].append(neighbour)
                distances[neighbour] = distances[pos] + 1
                queue.append((neighbour, depth + 1))
        # print_grid(grid, visited)

    # for k, v in depth_nodes.items():
    #     print(k, len(v))
    #     print_grid(grid, v)

    # nodes= set([(k) for k, v in distances.items() if v==7])
    # print(len(nodes))
    # print(len(visited))
    return distances


def solve_part1(inputs):
    return bfs(inputs["grid"], inputs["start"])


def solve_part2(inputs):
    pass


def solve(file_name, part=1):
    inputs = parse_input(file_name)
    if part == 1:
        return solve_part1(inputs)

    return solve_part2(inputs)


if __name__ == "__main__":
    solve("input.txt", part=1)
