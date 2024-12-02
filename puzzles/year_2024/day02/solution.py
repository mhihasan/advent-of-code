import os


def read_input(file_name: str) -> list[str]:
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, "r") as f:
        return f.read().splitlines()


def parse_input(file_name):
    inputs = read_input(file_name)
    return inputs


def is_sorted(lst):
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1)) or all(
        lst[i] >= lst[i + 1] for i in range(len(lst) - 1)
    )


def are_levels_valid(levels):
    if not is_sorted(levels):
        return False

    for i in range(1, len(levels)):
        difference = levels[i] - levels[i - 1]
        valid_difference = 1 <= abs(difference) <= 3
        if not valid_difference:
            return False

    return True


def is_report_safe(report_levels, tolerate_bad_reports=False):
    is_valid = are_levels_valid(report_levels)
    if not is_valid and tolerate_bad_reports:
        for i in range(len(report_levels)):
            new_levels = report_levels.copy()
            new_levels.pop(i)
            is_valid = are_levels_valid(new_levels)

            if is_valid:
                is_valid = True
                break

    return is_valid


def solve_part1(inputs):
    total_safe_reports = 0
    for line in inputs:
        report_levels = list(map(int, line.split()))
        if is_report_safe(report_levels):
            total_safe_reports += 1
    return total_safe_reports


def solve_part2(inputs):
    total_safe_reports = 0
    for line in inputs:
        report_levels = list(map(int, line.split()))
        if is_report_safe(report_levels, tolerate_bad_reports=True):
            total_safe_reports += 1
    return total_safe_reports


def solve(file_name, part=1):
    inputs = parse_input(file_name)
    if part == 1:
        return solve_part1(inputs)

    return solve_part2(inputs)


if __name__ == "__main__":
    solve("input.txt", part=1)
