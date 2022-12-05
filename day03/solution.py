import os
from collections import defaultdict
import string


PRIORITIES = {}


for i, ch in enumerate(string.ascii_lowercase + string.ascii_uppercase):
    PRIORITIES[ch] = i + 1

print(PRIORITIES)


def read_input(file_name: str) -> list[str]:
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, "r") as f:
        return f.read().splitlines()


def get_item_type_occurrence(compartment_item_types):
    occurrences = defaultdict(
        int,
    )
    for ch in compartment_item_types:
        occurrences[ch] += 1

    return occurrences


def _is_common_type(group_occurrences: list[dict[str, int]], item_type: str) -> bool:
    times_appeared = 0
    for group in group_occurrences:
        if group.get(item_type, 0) > 0:
            times_appeared += 1
    return times_appeared == len(group_occurrences)


def find_common_item_types(rucksack_items: list[str]) -> set[str]:
    item_types_occurrences = [get_item_type_occurrence(items) for items in rucksack_items]

    group1_occurrences = item_types_occurrences[0]

    common_types = set()
    for item_type, occurrence in group1_occurrences.items():
        if occurrence > 0 and _is_common_type(item_types_occurrences[1:], item_type):
            common_types.add(item_type)

    return common_types


def _aggregate_priority_score(item_types):
    return sum([PRIORITIES[item_type] for item_type in item_types])


def calculate_sum_of_rucksack_items_priorities(all_rucksack_items):
    priority_sum = 0
    for rucksack_items in all_rucksack_items:
        compartment1_items = rucksack_items[: len(rucksack_items) // 2]
        compartment2_items = rucksack_items[len(rucksack_items) // 2 :]
        common_types = find_common_item_types([compartment1_items, compartment2_items])
        priority_sum += _aggregate_priority_score(common_types)
    return priority_sum


def _chunkify(arr, n):
    for i in range(0, len(arr), n):
        yield arr[i : i + n]


def calculate_sum_of_group_priorities(all_rucksack_items, group_size=3):
    priorities_sum = 0
    for chunk in _chunkify(all_rucksack_items, group_size):
        common_types = find_common_item_types(chunk)
        priorities_sum += _aggregate_priority_score(common_types)
    return priorities_sum


def solve(file_name, part=1):
    items = read_input(file_name)
    if part == 1:
        return calculate_sum_of_rucksack_items_priorities(items)

    return calculate_sum_of_group_priorities(items)


if __name__ == "__main__":
    c = solve("demo_input.txt")
    print(c)
