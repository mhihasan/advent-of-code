import math
from functools import cmp_to_key

from day13.file_parser import parse_input


def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left == right:
            return 0

        return -1 if left < right else 1

    if isinstance(left, list) and isinstance(right, int):
        right = [right]
    if isinstance(right, list) and isinstance(left, int):
        left = [left]

    i, j = 0, 0
    l_len, r_len = len(left), len(right)

    while i < l_len and j < r_len:
        res = compare(left[i], right[j])
        if res:
            return res

        i += 1
        j += 1

    if i == l_len and j == r_len:
        return 0

    return -1 if i == l_len and j < r_len else 1


def solve_part1(pairs):
    indices = set()
    for i, pair in enumerate(pairs):
        r = compare(pair[0], pair[1])
        if r == -1:
            indices.add(i + 1)

    return sum(indices)


def solve_part2(pairs, divider_packets=None):
    packets = []
    for pair in pairs:
        packets.extend(pair)

    if divider_packets is None:
        divider_packets = [[[2]], [[6]]]

    packets.extend(divider_packets)
    sorted_packets = sorted(packets, key=cmp_to_key(compare))

    return math.prod([sorted_packets.index(p) + 1 for p in divider_packets])


def solve(file_name, part=1):
    pairs = parse_input(file_name)

    if part == 1:
        return solve_part1(pairs)

    return solve_part2(pairs)


if __name__ == "__main__":
    solve("demo_input.txt", part=2)
    # solve("input.txt", part=2)

    # index = 29
    # pairs = parse_input("input.txt")
    # v = is_right_side(pairs[index - 1][0], pairs[index - 1][1])
    # print(v)
