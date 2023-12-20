import heapq
import os
from collections import defaultdict


def read_input(file_name: str) -> list[str]:
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, "r") as f:
        return f.read().splitlines()


def parse_input(file_name):
    inputs = read_input(file_name)
    grid = []
    for line in inputs:
        grid.append([int(x) for x in line])
    return grid


DOWN = (1, 0)
UP = (-1, 0)
RIGHT = (0, 1)
LEFT = (0, -1)


def is_valid(grid, x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])


def get_neighbours(grid, x, y, current_direction, cells_with_same_direction):
    neighbours = []
    for dx, dy in [UP, DOWN, LEFT, RIGHT]:
        if current_direction and cells_with_same_direction < 4:
            continue

        if current_direction != (dx, dy) and current_direction != (-dx, -dy):
            new_x = x + dx
            new_y = y + dy
            if is_valid(grid, new_x, new_y):
                neighbours.append(((new_x, new_y), (dx, dy)))

    if cells_with_same_direction < 10 and current_direction:
        new_x = x + current_direction[0]
        new_y = y + current_direction[1]
        if is_valid(grid, new_x, new_y):
            neighbours.append(((new_x, new_y), current_direction))

    return neighbours


def get_paths(predecessors, v1):
    paths = []
    print("v1", v1)
    paths.append(v1)
    while v1 in predecessors:
        v1, direction = predecessors[v1]

        paths.append(v1)

    paths.reverse()
    return paths


def can_move_forward(predecessors, cell, current_direction):
    i = 0
    same_direction_cells = 0
    while i < 2 and cell in predecessors:
        cell, direction = predecessors[cell]
        if direction != current_direction:
            return same_direction_cells

        same_direction_cells += 1

        i += 1

    return same_direction_cells


def dijkstra(grid, src, dest):
    queue, visited = [(0, src, None, 0)], set()
    dist = defaultdict(lambda: float("inf"))
    dist[src] = grid[0][0]
    final_cost = 0

    while queue:
        cost, v1, direction, cells_in_same_direction = heapq.heappop(queue)
        if v1 == dest:
            final_cost = cost
            break

        if (v1, direction, cells_in_same_direction) in visited:
            continue

        visited.add((v1, direction, cells_in_same_direction))
        neighbours = get_neighbours(grid, v1[0], v1[1], direction, cells_in_same_direction)

        for v2, dir in neighbours:
            new_cost = cost + grid[v2[0]][v2[1]]
            # if new_cost < dist[v2]:
            #     dist[v2] = new_cost
            #     predecessors[v2] = (v1, dir)
            if direction == dir:
                heapq.heappush(queue, (new_cost, v2, dir, cells_in_same_direction + 1))
            else:
                heapq.heappush(queue, (new_cost, v2, dir, 1))

    print("d", final_cost)
    return final_cost


def solve_part1(grid):
    return dijkstra(grid, (0, 0), (len(grid) - 1, len(grid[0]) - 1))
    # print(distances)
    # d = distances[-1][-1]
    # print(d)


def solve_part2(grid):
    return dijkstra(grid, (0, 0), (len(grid) - 1, len(grid[0]) - 1))


def solve(file_name, part=1):
    inputs = parse_input(file_name)
    if part == 1:
        return solve_part1(inputs)

    return solve_part2(inputs)


if __name__ == "__main__":
    solve("input.txt", part=2)
    # solve("test2.txt", part=1)
