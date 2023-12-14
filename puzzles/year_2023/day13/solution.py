# TODO: Revisit

import os


def read_input(file_name: str) -> list[str]:
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, "r") as f:
        return f.read()


def parse_input(file_name):
    inputs = read_input(file_name).split("\n\n")
    patterns = [i.split("\n") for i in inputs]
    return patterns


def find_smudge(pattern):
    # Consider i as mirror line and check whether left and right side as symmetric
    for mirror_line in range(1, len(pattern)):
        above_part = pattern[:mirror_line][::-1]
        below_part = pattern[mirror_line:]

        zipped = zip(above_part, below_part)
        total_mismatch = 0
        for abo, bel in zipped:
            for a_c, b_c in zip(abo, bel):
                if a_c != b_c:
                    total_mismatch += 1

        if total_mismatch == 1:
            return mirror_line


def is_mirror(pattern, s, e):
    while s < e:
        if pattern[s] != pattern[e]:
            return 0
        s += 1
        e -= 1
    return s if s != e else 0


def find_reflection_line(pattern):
    s = 0
    e = len(pattern) - 1
    index = None
    while s < e:
        mirror_index = is_mirror(pattern, s, e)
        if mirror_index:
            index = mirror_index
            break

        s += 1

    if index is None:
        s = 0
        e = len(pattern) - 1
        while s < e:
            mirror_index = is_mirror(pattern, s, e)
            if mirror_index:
                index = mirror_index
                break

            e -= 1

    if index:
        return index

    return index


def find_val(pattern):
    reflection_row = find_reflection_line(pattern)
    if reflection_row:
        return 100 * reflection_row

    reflection_col = find_reflection_line(
        list(zip(*pattern)),
    )

    if reflection_col:
        return reflection_col

    raise Exception("No reflection point found")


def solve_part1(inputs):
    total = 0
    for i, line in enumerate(inputs):
        val = find_val(line)
        total += val

    return total


def find_val2(pattern):
    reflection_row = find_smudge(pattern)
    if reflection_row:
        return 100 * reflection_row

    reflection_col = find_smudge(
        list(zip(*pattern)),
    )

    if reflection_col:
        return reflection_col

    raise Exception("No reflection point found")


def solve_part2(inputs):
    total = 0
    for i, line in enumerate(inputs):
        val = find_val2(line)
        total += val

    return total


def solve(file_name, part=1):
    inputs = parse_input(file_name)
    if part == 1:
        return solve_part1(inputs)

    return solve_part2(inputs)


if __name__ == "__main__":
    solve("input.txt", part=1)
