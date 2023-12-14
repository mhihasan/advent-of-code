import os


def read_input(file_name: str) -> list[str]:
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, "r") as f:
        return f.read().splitlines()


def parse_input(file_name):
    inputs = read_input(file_name)
    return inputs


UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)


def tilt_common(grid, i, j, direction):
    new_i = i
    new_j = j
    while True:
        new_i_1 = new_i + direction[0]
        new_j_1 = new_j + direction[1]

        if not (0 <= new_i_1 < len(grid) and 0 <= new_j_1 < len(grid[0])):
            break

        if grid[new_i_1][new_j_1] != ".":
            break

        grid[new_i_1][new_j_1] = "O"
        grid[new_i][new_j] = "."

        new_i = new_i_1
        new_j = new_j_1

    return grid


def tilt(grid, direction):
    if direction in [UP, LEFT]:
        for i, line in enumerate(grid):
            for j, c in enumerate(line):
                if c != "O":
                    continue

                grid = tilt_common(grid, i, j, direction)

    else:
        for i in range(len(grid) - 1, -1, -1):
            for j in range(len(grid[0]) - 1, -1, -1):
                if grid[i][j] != "O":
                    continue

                grid = tilt_common(grid, i, j, direction)

    return grid


def calculate_total(grid):
    total = 0
    length = len(grid)
    for i, line in enumerate(grid):
        count_0 = len([c for c in line if c == "O"])
        if count_0:
            total += count_0 * (length - i)
    return total


def solve_part1(grid):
    grid = tilt([list(line) for line in grid], UP)
    return calculate_total(grid)


def print_grid(grid):
    print("_____________________________________")
    for line in grid:
        print(line)

    print("_____________________________________\n")


def run_cycle(grid):
    grid = tilt(grid, UP)
    # print_grid(grid)
    grid = tilt(grid, LEFT)
    # print_grid(grid)

    grid = tilt(grid, DOWN)
    # print_grid(grid)
    grid = tilt(grid, RIGHT)
    # print_grid(grid)
    return grid


def solve_part2(inputs):
    grid = [list(line) for line in inputs]
    cycle_count = 1000000000
    for i in range(cycle_count):
        grid = run_cycle(grid)

    return calculate_total(grid)


def solve(file_name, part=1):
    inputs = parse_input(file_name)
    if part == 1:
        return solve_part1(inputs)

    return solve_part2(inputs)


if __name__ == "__main__":
    # fn(['.', '#', '.', 'O', '.', '#', 'O', '.', '.', '.'])
    r = solve("demo_input.txt", part=2)
    print("result", r)
