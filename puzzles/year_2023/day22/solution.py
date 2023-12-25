import os
from collections import defaultdict


def read_input(file_name: str) -> list[str]:
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, "r") as f:
        return f.read().splitlines()


def parse_input(file_name):
    inputs = read_input(file_name)
    bricks = []

    for line in inputs:
        first_end, second_end = line.split("~")
        first_end = [int(x) for x in first_end.split(",")]
        second_end = [int(x) for x in second_end.split(",")]
        bricks.append([first_end, second_end])
    bricks = list(sorted(bricks, key=lambda x: x[0][2]))

    return bricks


def does_brick_overlap_in_x_y_plane(brick1, brick2):
    brick1_start = brick1[0]
    brick1_end = brick1[1]
    brick2_start = brick2[0]
    brick2_end = brick2[1]

    return max(brick1_start[0], brick2_start[0]) <= min(brick1_end[0], brick2_end[0]) and max(
        brick1_start[1], brick2_start[1]
    ) <= min(brick1_end[1], brick2_end[1])


def find_max_depth_to_drop(bricks, brick):
    max_depth = 1
    for brick2 in bricks:
        if does_brick_overlap_in_x_y_plane(brick, brick2):
            max_depth = max(max_depth, brick2[1][2] + 1)
    return max_depth


def fall_bricks(bricks):
    for i, brick in enumerate(bricks):
        max_depth = find_max_depth_to_drop(bricks[:i], brick)
        brick[1][2] -= brick[0][2] - max_depth
        brick[0][2] = max_depth

    return list(sorted(bricks, key=lambda x: x[0][2]))


def find_supporting_bricks(bricks):
    supporting_bricks = defaultdict(set)
    supported_by_bricks = defaultdict(set)

    for up, upper_brick in enumerate(bricks):
        for below, lower_brick in enumerate(bricks[:up]):
            if does_brick_overlap_in_x_y_plane(upper_brick, lower_brick) and upper_brick[0][2] == lower_brick[1][2] + 1:
                supporting_bricks[below].add(up)
                supported_by_bricks[up].add(below)

    return supporting_bricks, supported_by_bricks


def find_disintegrated_bricks(bricks, supporting_bricks, supported_by_bricks):
    disintegrated_bricks = set()
    for i, brick in enumerate(bricks):
        supports = supporting_bricks[i]
        all_have_support = all(len(supported_by_bricks[support]) >= 2 for support in supports)
        if all_have_support:
            disintegrated_bricks.add(i)
    return disintegrated_bricks


def solve_part1(bricks):
    bricks = fall_bricks(bricks)
    supporting_bricks, supported_by_bricks = find_supporting_bricks(bricks)

    disintegrated_bricks = find_disintegrated_bricks(bricks, supporting_bricks, supported_by_bricks)
    return len(disintegrated_bricks)


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
