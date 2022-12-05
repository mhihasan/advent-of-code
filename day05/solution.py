import os
import re
from collections import deque


def read_input(file_name: str) -> list[str]:
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, "r") as f:
        return f.read().splitlines()


def map_stacks_to_items(line_str):
    stack_no_mapping = {}
    for i in range(0, len(line_str), 4):
        item = line_str[i : i + 3]
        idx = i // 4
        if not re.findall("[A-Z]", item):
            continue

        stack_no_mapping[idx] = item[1]

    return stack_no_mapping


def append_left_to_stacks(all_stacks, item_mapping):
    for stack_no, item in item_mapping.items():
        all_stacks[stack_no].appendleft(item)

    return all_stacks


def move_items(stacks, from_stack_idx, to_stack_idx, num_moves, keep_ordering=False):
    items_to_move = [stacks[from_stack_idx - 1].pop() for i in range(num_moves)]
    if keep_ordering:
        items_to_move = items_to_move[::-1]

    for item in items_to_move:
        stacks[to_stack_idx - 1].append(item)

    return stacks


def total_stacks(inputs):
    stack_counts = []
    for inp in inputs:
        if "1" in inp:
            break
        line_items = [c for c in inp.split(" ") if c]

        stack_counts.append(len(line_items))

    return max(stack_counts)


def populate_stacks(inputs, stacks_count):
    all_stacks = [deque() for _ in range(stacks_count)]
    for inp in inputs:
        if "1" in inp:
            break
        maps = map_stacks_to_items(inp)
        append_left_to_stacks(all_stacks, maps)

    return all_stacks


def populate_moves(inputs):
    moves = []

    for inp in inputs:
        if not inp.startswith("move"):
            continue

        values = re.findall(r"\d+", inp)
        moves.append({"num_moves": int(values[0]), "from_stack_idx": int(values[1]), "to_stack_idx": int(values[2])})

    return moves


def rearrange_stacks(stacks, moves, keep_ordering=False):
    for move in moves:
        move_items(stacks, **move, keep_ordering=keep_ordering)

    return "".join([s.pop() for s in stacks])


def parse_input(inputs):
    stacks_count = total_stacks(inputs)
    return {"stacks": populate_stacks(inputs, stacks_count), "moves": populate_moves(inputs)}


def solve(file_name, part=1):
    inputs = read_input(file_name)
    data = parse_input(inputs)

    return rearrange_stacks(data["stacks"], data["moves"], keep_ordering=part == 2)
