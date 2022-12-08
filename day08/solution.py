from day08.file_parser import read_input, parse_grid


def _is_valid_cell(i, j, n):
    return 0 <= i < n and 0 <= j < n


def is_visible(grid, val, row, col):
    n = len(grid)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for direction in directions:
        visible = True
        delta_i, delta_j = direction
        i, j = row, col

        while True:
            i += delta_i
            j += delta_j
            if not _is_valid_cell(i, j, n):
                break

            if grid[i][j] >= val:
                visible = False
                break

        if visible:
            return True

    return False


def cal_score(grid, val, row, col):
    n = len(grid)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    score = 1
    for direction in directions:
        delta_i, delta_j = direction
        i, j = row, col

        while True:
            i += delta_i
            j += delta_j
            if not _is_valid_cell(i, j, n):
                if i < 0:
                    i = 0
                elif i > n - 1:
                    i = n - 1
                if j < 0:
                    j = 0
                elif j > n - 1:
                    j = n - 1
                break

            if grid[i][j] >= val:
                print("huu", i, j)
                break
        score *= (abs(col - j) or 1) * (abs(row - i) or 1)

    return score


def solve_part1(grid):
    visible_cells = []

    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[i]) - 1):
            if is_visible(grid, grid[i][j], i, j):
                visible_cells.append({"value": grid[i][j], "row": i, "col": j})

    visible_from_edge = len(grid) * 2 + (len(grid[0]) - 2) * 2
    return len(visible_cells) + visible_from_edge


def solve_part2(grid):
    scores = []
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[i]) - 1):
            if is_visible(grid, grid[i][j], i, j):
                scores.append(cal_score(grid, grid[i][j], i, j))

    return max(scores)


def solve(file_name, part=1):
    inputs = read_input(file_name)
    grid = parse_grid(inputs)
    if part == 1:
        return solve_part1(grid)

    return solve_part2(grid)
