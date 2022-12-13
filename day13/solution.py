from day13.file_parser import parse_input


def is_right_side(left_arr, right_arr):
    i, j = 0, 0
    l_len = len(left_arr)
    r_len = len(right_arr)

    while i < l_len and j < r_len:
        l_val = left_arr[i]
        r_val = right_arr[j]

        if isinstance(l_val, int) and isinstance(r_val, int) and l_val != r_val:
            return l_val < r_val
        elif isinstance(l_val, list) and isinstance(r_val, list):
            return is_right_side(l_val, r_val)
        elif isinstance(l_val, list) and isinstance(r_val, int):
            return is_right_side(l_val, [r_val])
        elif isinstance(l_val, int) and isinstance(r_val, list):
            return is_right_side([l_val], r_val)

        i += 1
        j += 1

    if i >= l_len and j <= r_len:
        return True

    return False


def solve_part1(pairs):
    indices = set()
    for i, pair in enumerate(pairs):
        if is_right_side(pair[0], pair[1]):
            indices.add(i + 1)

    print(indices)
    print(sum(indices))
    return sum(indices)


def solve_part2(inputs):
    pass


def solve(file_name, part=1):
    pairs = parse_input(file_name)

    if part == 1:
        return solve_part1(pairs)

    return solve_part2(pairs)


if __name__ == "__main__":
    solve("demo_input.txt", part=1)
    solve("input.txt", part=1)

    # index = 29
    # pairs = parse_input("input.txt")
    # v = is_right_side(pairs[index - 1][0], pairs[index - 1][1])
    # print(v)
