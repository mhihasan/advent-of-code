import os
from collections import deque


def read_input(file_name: str) -> list[str]:
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, "r") as f:
        return f.read().splitlines()


def parse_input(file_name):
    inputs = read_input(file_name)
    return inputs


DOWN = (1, 0)
UP = (-1, 0)
RIGHT = (0, 1)
LEFT = (0, -1)


def is_valid(grid, x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])


def get_directions(tile, current_direction):
    if tile == ".":
        return current_direction
    elif tile == "-":
        if current_direction in (UP, DOWN):
            return [LEFT, RIGHT]
        else:
            return current_direction
    elif tile == "|":
        if current_direction in (LEFT, RIGHT):
            return [UP, DOWN]
        else:
            return current_direction
    elif tile == "/":
        return {RIGHT: UP, LEFT: DOWN, UP: RIGHT, DOWN: LEFT}[current_direction]
    elif tile == "\\":
        return {RIGHT: DOWN, LEFT: UP, UP: LEFT, DOWN: RIGHT}[current_direction]

    raise Exception("Unknown tile", tile)


def get_next_moves(grid, x, y, current_direction):
    moves = []
    split = False
    directions = get_directions(grid[x][y], current_direction)
    if isinstance(directions, list):
        for d in directions:
            new_x = x + d[0]
            new_y = y + d[1]
            if not is_valid(grid, new_x, new_y):
                continue

            split = True
            moves.append(((new_x, new_y), d))
    else:
        # GO to same direction
        new_x = x + directions[0]
        new_y = y + directions[1]
        if is_valid(grid, new_x, new_y):
            moves.append(((new_x, new_y), directions))

    return {"moves": moves, "split": split}


def print_grid(grid, visited):
    visited = {pos for pos, _ in visited}
    total = 0
    grid_copy = [list(row) for row in grid]
    for x, y in visited:
        if is_valid(grid, x, y):
            grid_copy[x][y] = "#"
            total += 1
    for row in grid_copy:
        print("".join(row))


def traverse(grid, start_pos, current_direction=RIGHT):
    q = deque([(start_pos, current_direction)])
    visited = set()

    while q:
        pos, current_direction = q.popleft()
        x, y = pos
        visited.add((pos, current_direction))
        # print("VISITING", x, y, grid[x][y])

        moves = get_next_moves(grid, x, y, current_direction=current_direction)
        for move in moves["moves"]:
            if (move[0], move[1]) in visited:
                continue

            visited.add((move[0], move[1]))
            q.append((move[0], move[1]))

    visited = {pos for pos, _ in visited}
    return len(visited)


def solve_part1(grid):
    return traverse(grid, start_pos=(0, 0), current_direction=RIGHT)


def solve_part2(grid):
    tiles_energized = {}

    for top_tile in [(0, i) for i in range(len(grid[0]))]:
        energized = traverse(grid, start_pos=top_tile, current_direction=DOWN)
        tiles_energized[top_tile] = energized

    for bottom_tile in [(len(grid) - 1, i) for i in range(len(grid[0]))]:
        energized = traverse(grid, start_pos=bottom_tile, current_direction=UP)
        tiles_energized[bottom_tile] = energized

    for left_tile in [(i, 0) for i in range(len(grid))]:
        energized = traverse(grid, start_pos=left_tile, current_direction=RIGHT)
        tiles_energized[left_tile] = energized

    for right_tile in [(i, len(grid[0]) - 1) for i in range(len(grid))]:
        energized = traverse(grid, start_pos=right_tile, current_direction=LEFT)
        tiles_energized[right_tile] = energized

    return max(tiles_energized.values())


def solve(file_name, part=1):
    inputs = parse_input(file_name)
    if part == 1:
        return solve_part1(inputs)

    return solve_part2(inputs)


if __name__ == "__main__":
    r = solve("input.txt", part=2)
    print(r)
    # solve("input.txt", part=1)
