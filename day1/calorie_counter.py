import argparse
from collections import defaultdict


def read_input(file_name):
    with open(file_name, "r") as f:
        return f.read().splitlines()


def get_elves_calories(calories):
    calories = iter(calories)
    elf_number = 1

    elf_calories = defaultdict(list)
    while True:
        try:
            c = next(calories)
        except StopIteration:
            break

        if c == "":
            elf_number += 1
        else:
            elf_calories[elf_number].append(int(c))

    return [calories for elf, calories in elf_calories.items()]


def most_calories_carried(calories, n=1):
    elf_calories = get_elves_calories(calories)
    calories_carried = sorted(
        [sum(calories) for calories in elf_calories], reverse=True
    )
    most = sum(calories_carried[:n])

    return most


def main(n):
    calories = read_input("input.txt")
    calories_carried = most_calories_carried(calories, n)
    print(f"Total calories carried: {calories_carried}")


def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=1, help="Top most calories")

    args = parser.parse_args()

    main(args.n)


if __name__ == "__main__":
    # python calorie_counter.py
    # python calorie_counter.py --n 3
    cli()
