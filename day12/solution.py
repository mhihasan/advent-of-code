import math
import os
import string
from collections import defaultdict, deque
from typing import Optional


SOURCE_CELL = "S"
DEST_CELL = "E"

CELL_ELEVATIONS = {}

for i, ch in enumerate(string.ascii_lowercase):
    CELL_ELEVATIONS[ch] = i + 1

CELL_ELEVATIONS[SOURCE_CELL] = CELL_ELEVATIONS["a"]
CELL_ELEVATIONS[DEST_CELL] = CELL_ELEVATIONS["z"]


def read_input(file_name: str) -> list[str]:
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, "r") as f:
        return f.read().splitlines()


def find_predecessors(predecessor, target: str) -> str:
    """Finds predecessors of a node, returns "" for nodes in cycle"""
    path = []
    current: Optional[str] = target
    while current is not None:
        if current in path:
            return ""

        path.append(f"{current}")
        current = predecessor.get(current)

    return "|".join(path[::-1])


def get_neighbours(grid, current, total_row, total_col):
    neighbours = []
    for direction in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        adj_row, adj_col = current[0] + direction[0], current[1] + direction[1]
        if 0 <= adj_row < total_row and 0 <= adj_col < total_col:
            neighbours.append((adj_row, adj_col))

    current_val = grid[current[0]][current[1]]
    # if current_val == SOURCE_CELL:
    #     return neighbours

    current_elevation = CELL_ELEVATIONS[current_val]

    adj_cells = []
    for adj in neighbours:
        adj_val = grid[adj[0]][adj[1]]
        adj_elevation = CELL_ELEVATIONS[adj_val]
        if adj_elevation - current_elevation <= 1:
            adj_cells.append(adj)

    return adj_cells


def shortest_path(grid, source, destination):
    total_row = len(grid)
    total_col = len(grid[0])
    distance: defaultdict = defaultdict(lambda: math.inf)
    distance[source] = 0
    visited = defaultdict(bool)

    predecessor: defaultdict = defaultdict(lambda: None)

    queue = deque()
    queue.append(source)
    visited[source] = True

    while queue:
        current = queue.popleft()
        if current == destination:
            p = find_predecessors(predecessor, destination)
            print(p)
            return distance[current]

        for neighbour in get_neighbours(grid, current, total_row=total_row, total_col=total_col):
            if visited.get(neighbour):
                continue

            new_dist = distance[current] + 1
            # if new_dist < distance[neighbour]:
            distance[neighbour] = new_dist
            visited[neighbour] = True
            predecessor[neighbour] = current

            queue.append(neighbour)

    return -1


def solve_part1(grid):
    source = destination = None
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if source and destination:
                break

            if grid[i][j] == SOURCE_CELL and source is None:
                source = (i, j)
            if grid[i][j] == DEST_CELL and destination is None:
                destination = (i, j)

    print("source", source, grid[source[0]][source[1]])
    print("destination", destination, grid[destination[0]][destination[1]])

    res = shortest_path(grid, source, destination)

    print(res)
    return res


def solve(file_name, part=1):
    inputs = read_input(file_name)
    if part == 1:
        v = solve_part1(inputs)
        if v == -1:
            raise Exception("No path exists")

        print("v", v)
        return v
    # return solve_part2(inputs)


if __name__ == "__main__":
    solve("input.txt", part=1)
