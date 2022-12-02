import argparse
from collections import defaultdict


def read_input(file_name):
    with open(file_name, "r") as f:
        return f.read().splitlines()


def get_elves_calories(calories: list[str]) -> list[list]:
    calories_iter = iter(calories)
    elf_number = 1

    elf_calories = defaultdict(list)
    while True:
        try:
            c = next(calories_iter)
        except StopIteration:
            break

        if c == "":
            elf_number += 1
        else:
            elf_calories[elf_number].append(int(c))

    return [calories for elf, calories in elf_calories.items()]


def most_calories_carried(calories: list[str], n=1) -> int:
    elf_calories = get_elves_calories(calories)
    calories_carried = sorted(
        [sum(calories) for calories in elf_calories], reverse=True
    )
    calories_sum = sum(calories_carried[:n])

    return calories_sum


def solve(file_name: str, n: int = 1):
    calories = read_input(file_name)
    return most_calories_carried(calories, n)


def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", type=str, default="input.txt")
    parser.add_argument("--n", type=int, default=1)

    args = parser.parse_args()

    result = solve(file_name=args.file, n=args.n)
    print(f"Result: {result}")


if __name__ == "__main__":
    # python calorie_counter.py
    # python calorie_counter.py --n 3
    cli()
