import heapq
import os
import string
from collections import defaultdict

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)
DIRECTIONS = [UP, DOWN, LEFT, RIGHT]
SOURCE_CELL = "S"
DEST_CELL = "E"

CELL_ELEVATIONS = {}
for i, ch in enumerate(string.ascii_lowercase):
    CELL_ELEVATIONS[ch] = i + 1


def read_input(file_name: str) -> list[str]:
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, "r") as f:
        return f.read().splitlines()


class Node:
    def __init__(self, row, col, value, elevation=0, dist=-1):
        self.row = row
        self.col = col
        self.value = value
        self.elevation = elevation
        self.dist = dist
        self.prev = None

    def __repr__(self):
        return f"({self.row}, {self.col}): {self.value}"


def is_valid_cell(current_row, current_col, total_row, total_col):
    return 0 <= current_row < total_row and 0 <= current_col < total_col


# def invalid_elevation(current, adjacent):
# return adjacent  > current + 1


def find_valid_neighbour_cells(current_node, grid, total_row, total_col):
    neighbours = []

    cell_val = grid[current_node.row][current_node.col]
    current_elevation = CELL_ELEVATIONS[grid[current_node.row][current_node.col].lower()]

    for direction in DIRECTIONS:
        adj_row, adj_col = current_node.row + direction[0], current_node.col + direction[1]

        if is_valid_cell(adj_row, adj_col, total_row, total_col):
            adj_cell = grid[adj_row][adj_col]
            adj_elevation = CELL_ELEVATIONS[adj_cell.lower()]
            print(f"adj elevation, {adj_row, adj_col}: {adj_elevation}")

            if 0 <= (adj_elevation - current_elevation) <= 1 or cell_val == SOURCE_CELL or adj_cell == DEST_CELL:
                # if not invalid_elevation(current_elevation, adj_elevation):
                neighbours.append(Node(row=adj_row, col=adj_col, value=adj_cell, elevation=adj_elevation, dist=1))

    return neighbours


def dijktra(grid, start, end):
    total_row = len(grid)
    total_col = len(grid[0])

    heap = [(0, start)]  # cost from start node,end node
    visited = defaultdict(bool)
    visited[start] = True

    while heap:
        (cost, u) = heapq.heappop(heap)

        if (u.row, u.col) == end:
            print("path", cost)
            return cost

        for cell in find_valid_neighbour_cells(u, grid, total_row, total_col):
            if visited[(cell.row, cell.col)]:
                continue

            visited[(cell.row, cell.col)] = True

            next_item = cost + cell.dist
            heapq.heappush(heap, (next_item, cell))


def solve_part1(grid):
    total_row = len(grid)
    total_col = len(grid[0])
    print(grid)
    source = Node(row=0, col=0, value=SOURCE_CELL, dist=0)
    dest = Node(0, 0, value=DEST_CELL, dist=-1)

    print("row", total_row, total_col)
    print(source)

    for row in range(total_row):
        for col in range(total_col):
            if grid[row][col] == SOURCE_CELL:
                source.row = row
                source.col = col
                source.elevation = CELL_ELEVATIONS[grid[row][col].lower()]
            elif grid[row][col] == DEST_CELL:
                dest.row = row
                dest.col = col

    queue = [source]
    visited = defaultdict(bool)
    prev = defaultdict(lambda: Node)

    path = 0
    while queue:
        current = queue.pop()

        if grid[current.row][current.col] == dest.value:
            print("Found", current.dist, path)
            return current.dist

        print("<<<<< Current Node : >>>>>>> ", (current, grid[current.row][current.col]))

        neighbour_cells = find_valid_neighbour_cells(current, grid, total_row, total_col)

        print("Valid adjacent cells: ", neighbour_cells)

        v = False
        for cell in neighbour_cells:
            if visited[(cell.row, cell.col)]:
                continue

            queue.append(cell)

            visited[(cell.row, cell.col)] = True
            prev[cell] = current
            v = True

        if v:
            path += 1

    return -1


def solve_part2(inputs):
    pass


def solve(file_name, part=1):
    inputs = read_input(file_name)
    if part == 1:
        v = solve_part1(inputs)
        if v == -1:
            raise Exception("No path exists")

        print("v", v)
        return v
    return solve_part2(inputs)


if __name__ == "__main__":
    solve("demo_input.txt", part=1)
