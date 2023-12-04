import math
import os
import re


def read_input(file_name: str) -> list[str]:
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, "r") as f:
        return f.read().splitlines()


def parse_input(inputs):
    cards = {}
    for line in inputs:
        print(line)
        card, numbers = line.split(": ")
        card_no = int(re.findall(r"\d+", card)[0])
        winning_numbers, numbers_having = numbers.split(" | ")
        winning_numbers = [int(n) for n in winning_numbers.split(" ") if n]
        numbers_having = [int(n) for n in numbers_having.split(" ") if n]
        cards[card_no] = {
            "winning_numbers": winning_numbers,
            "numbers_having": numbers_having,
            "matching_numbers": set(winning_numbers).intersection(set(numbers_having)),
            "copies": 0,
        }

    return cards


def solve_part1(inputs):
    total_points = 0
    for card_no, numbers in inputs.items():
        if numbers["matching_numbers"]:
            total_points += int(math.pow(2, len(numbers["matching_numbers"]) - 1))
    return total_points


def solve_part2(inputs):
    for card_no, numbers in inputs.items():
        matching_numbers = numbers["matching_numbers"]
        copies = numbers["copies"]
        next_card = card_no + 1

        i = 0
        while i < len(matching_numbers):
            inputs[next_card]["copies"] += copies + 1
            next_card += 1
            i += 1

    total_cards = sum([card["copies"] + 1 for card in inputs.values()])
    return total_cards


def solve(file_name, part=1):
    inputs = read_input(file_name)
    inputs = parse_input(inputs)

    if part == 1:
        return solve_part1(inputs)

    return solve_part2(inputs)


if __name__ == "__main__":
    r = solve("input.txt", part=1)
    print(r)
