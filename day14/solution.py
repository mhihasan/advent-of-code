import os


def read_input(file_name: str) -> list[str]:
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, "r") as f:
        return f.read().splitlines()


def max_row_col(inputs):
    max_col = -1
    max_row = -1

    paths = []

    for line in inputs:
        path = [list(map(int, s.split(","))) for s in line.split(" -> ")]
        paths.append(path)
        for p in path:
            max_col = max(p[0], max_col)
            max_row = max(p[1], max_row)

    return paths, max_row, max_col


def _show_grid(grid):
    for row in grid:
        print("".join(row))


def _initialize_grid(inputs):
    paths, total_row, total_col = max_row_col(inputs)
    grid = [["." for x in range(total_col + 1)] for y in range(total_row + 1)]
    grid[0][500] = "+"

    for path in paths:
        i = 0
        while i < len(path) - 1:
            p1, p2 = path[i], path[i + 1]
            print("p1, p2", p1, p2)
            if p1[0] != p2[0]:
                col_min = min(p1[0], p2[0])
                col_max = max(p1[0], p2[0])

                while col_min <= col_max:
                    grid[p1[1]][col_min] = "#"
                    col_min += 1
            elif p1[1] != p2[1]:
                row_min = min(p1[1], p2[1])
                row_max = max(p1[1], p2[1])

                while row_min <= row_max:
                    grid[row_min][p1[0]] = "#"
                    row_min += 1
            i += 1

    return grid, total_row, total_col


DOWN = (1, 0)
DOWN_LEFT = (1, -1)
DOWN_RIGHT = (1, 1)
DIRECTIONS = [DOWN, DOWN_LEFT, DOWN_RIGHT]

ROCK = "#"
AIR = "."
SAND_AT_REST = "o"
SAND_SOURCE = "+"


def get_neighbours(current, total_row, total_col):
    neighbours = []
    for direction in [DOWN, DOWN_LEFT, DOWN_RIGHT]:
        adj_row, adj_col = current[0] + direction[0], current[1] + direction[1]
        if 0 <= adj_row < total_row and 0 <= adj_col < total_col:
            neighbours.append((adj_row, adj_col))
    return neighbours


def find_next_move(grid, sand_pos, total_row, total_col):
    selected_cell = None

    for adj in get_neighbours(sand_pos, total_row, total_col):
        if grid[adj[0]][adj[1]] == AIR:
            selected_cell = adj
            break

    return selected_cell


def is_going_to_abyss(grid, sand_pos, total_row, total_col):
    sand_row, sand_col = sand_pos[0], sand_pos[1]

    while sand_row < total_row and sand_col < total_col:
        next_move = find_next_move(grid, sand_pos, total_row, total_col)
        if next_move is None:
            return False

        sand_row, sand_col = next_move[0], next_move[1]

    return True


def solve_part1(inputs):
    grid, total_row, total_col = _initialize_grid(inputs)
    _show_grid(grid)

    come_to_rest_count = 0

    SAND_SOURCE_POS = (0, 500)

    while True:
        is_abyss = is_going_to_abyss(grid, SAND_SOURCE_POS, total_row, total_col)
        if is_abyss:
            break

        come_to_rest_count += 1

    print("come to rest", come_to_rest_count)


def solve_part2(inputs):
    pass


def solve(file_name, part=1):
    inputs = read_input(file_name)
    if part == 1:
        return solve_part1(inputs)

    return solve_part2(inputs)


if __name__ == "__main__":
    solve("demo_input.txt", part=1)
