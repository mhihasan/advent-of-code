import os
from collections import defaultdict


def read_input(file_name: str) -> list[str]:
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, "r") as f:
        return f.read()


def parse_input(file_name):
    return read_input(file_name).split(",")


def find_hash(s):
    current_val = 0
    for c in s:
        current_val += ord(c)
        current_val *= 17
        current_val %= 256
    return current_val


def solve_part1(inputs):
    s = 0
    for sequence in inputs:
        s += find_hash(sequence)
    return s


def calculate_focusing_power(boxes):
    total_focusing_power = 0
    for k, v in boxes.items():
        for i, label in enumerate(v["slots"]):
            val = (k + 1) * (i + 1) * int(v["focal_lengths"][label])
            total_focusing_power += val
    return total_focusing_power


def solve_part2(inputs):
    boxes = defaultdict(lambda: {"slots": [], "focal_lengths": {}})

    for sequence in inputs:
        focal_length = None
        if "=" in sequence:
            label, focal_length = sequence.split("=")
        else:
            label, _ = sequence[: len(sequence) - 1], sequence[-1]

        box_number = find_hash(label)
        box = boxes[box_number]
        if focal_length:
            if label in box["focal_lengths"]:
                box["focal_lengths"][label] = focal_length
            else:
                box["slots"].append(label)
                box["focal_lengths"][label] = focal_length

        else:
            if label in box["focal_lengths"]:
                idx = box["slots"].index(label)
                box["slots"].pop(idx)
                box["focal_lengths"].pop(label)

    return calculate_focusing_power(boxes)


def solve(file_name, part=1):
    inputs = parse_input(file_name)
    if part == 1:
        return solve_part1(inputs)

    return solve_part2(inputs)


if __name__ == "__main__":
    solve("input.txt", part=2)
