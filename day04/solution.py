import os


def read_input(file_name: str) -> list[str]:
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, "r") as f:
        return f.read().splitlines()


def does_fully_contain(range1, range2):
    range1_low, range1_high = range1
    range2_low, range2_high = range2

    return range1_low <= range2_low <= range1_high and range1_low <= range2_high <= range1_high


def does_overlap(range1, range2):
    range1_low, range1_high = range1
    range2_low, range2_high = range2

    return range1_low <= range2_low <= range1_high or range1_low <= range2_high <= range1_high


def to_list(r):
    return [int(v) for v in r.split("-")]


def calculate_fully_contained_pairs_count(assignment_pairs):
    fully_contained_pairs_count = 0
    for pair in assignment_pairs:
        range1, range2 = pair.split(",")
        range1_list, range2_list = to_list(range1), to_list(range2)
        if does_fully_contain(range1_list, range2_list) or does_fully_contain(range2_list, range1_list):
            fully_contained_pairs_count += 1

    return fully_contained_pairs_count


def calculate_overlap_pairs_count(assignment_pairs):
    overlapped_pairs_count = 0
    for pair in assignment_pairs:
        range1, range2 = pair.split(",")
        range1_list, range2_list = to_list(range1), to_list(range2)
        if does_overlap(range1_list, range2_list) or does_overlap(range2_list, range1_list):
            overlapped_pairs_count += 1

    return overlapped_pairs_count


def solve(file_name, part=1):
    inputs = read_input(file_name)
    if part == 1:
        return calculate_fully_contained_pairs_count(inputs)

    return calculate_overlap_pairs_count(inputs)
