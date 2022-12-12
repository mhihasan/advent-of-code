import math
import operator
from collections import defaultdict
from textwrap import indent

from day11.file_parser import parse_input

WORRY_LEVEL_DIVISOR = 3


def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y
    else:
        n = max(len(str(x)), len(str(y)))
        half = n // 2
        a = x // (10 ** (half))  # left part of x
        b = x % (10 ** (half))  # right part of x
        c = y // (10 ** (half))  # left part of y
        d = y % (10 ** (half))  # right part of y
        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        ad_plus_bc = karatsuba(a + b, c + d) - ac - bd
        return ac * (10 ** (2 * half)) + (ad_plus_bc * (10**half)) + bd


OPERATOR = {
    "+": operator.add,
    "-": operator.sub,
    "*": karatsuba,
}


def _calc_new_worry_level(current_worry_level, operation):
    left_operand = current_worry_level if operation["left_operand"] == "old" else operation["left_operand"]
    right_operand = current_worry_level if operation["right_operand"] == "old" else operation["right_operand"]
    print("left", left_operand)
    print("right", right_operand)
    return OPERATOR[operation["operator"]](left_operand, right_operand)


def _new_monkey_to_throw_item(new_worry_level, test):
    is_divisible = new_worry_level % test["divisible_by"] == 0
    return test["true"] if is_divisible else test["false"]


# def inspect_item(item, monkey_op, divide_worry_level=True):
#     new_worry_level = _calc_new_worry_level(item, monkey_op["operation"])
#
#     if divide_worry_level:
#         new_worry_level //= WORRY_LEVEL_DIVISOR
#
#     print(indent(f"Worry level is divided by {WORRY_LEVEL_DIVISOR} to {new_worry_level}", "    "))
#     new_monkey_no = _new_monkey_to_throw_item(new_worry_level, monkey_op["test"])
#
#     print(indent(f"Item with worry level {new_worry_level} is thrown to monkey {new_monkey_no}.", "    "))
#     return new_monkey_no, new_worry_level


def inspect_item(item, monkey_op, divide_worry_level=True):
    operation = monkey_op["operation"]
    left_operand = item if operation["left_operand"] == "old" else operation["left_operand"]
    right_operand = item if operation["right_operand"] == "old" else operation["right_operand"]
    new_item = OPERATOR[operation["operator"]](left_operand, right_operand)

    if divide_worry_level:
        new_item //= WORRY_LEVEL_DIVISOR

    print(indent(f"Worry level is divided by {WORRY_LEVEL_DIVISOR} to {item}", "    "))
    # new_monkey_no = _new_monkey_to_throw_item(new_item, monkey_op["test"])
    test = monkey_op["test"]
    divisor = test["divisible_by"]
    is_divisible = new_item % divisor == 0
    new_monkey_no = test["true"] if is_divisible else test["false"]

    print(indent(f"Item with worry level {new_item} is thrown to monkey {new_monkey_no}.", "    "))
    return new_monkey_no, new_item


def inspect_items(monkey_operations, items_inspected, divide_worry_level=True):
    for monkey_no, monkey_op in monkey_operations.items():
        print(f"Monkey {monkey_no}:")

        while monkey_op["items"]:
            item = monkey_op["items"].popleft()

            print(indent(f"Monkey inspects an item with a worry level of {item}.", "  "))
            new_monkey_no, new_worry_level = inspect_item(item, monkey_op, divide_worry_level)
            monkey_operations[new_monkey_no]["items"].append(new_worry_level)

            items_inspected[monkey_no] += 1

    return monkey_operations, items_inspected


def _calculate_monkey_business_level(items_inspected, active_monkeys: int = 2):
    most_inspected_items = sorted(items_inspected.values(), reverse=True)[:active_monkeys]
    return math.prod(most_inspected_items)


def solve_part1(monkey_operations, total_round=20):
    print("monkey", monkey_operations)
    round_no = 1
    items_inspected = defaultdict(int)

    while round_no < total_round + 1:
        monkey_operations, items_inspected = inspect_items(monkey_operations, items_inspected)

        print(f"\nAfter round {round_no}, the monkeys are holding items with these worry levels:")
        for monkey_no, monkey_op in monkey_operations.items():
            s = ", ".join([str(item) for item in monkey_op["items"]])
            print(f"Monkey {monkey_no}: {s}")
        print("\n\n")

        print("Items inspected")
        for monkey_no, items in items_inspected.items():
            # s = ', '.join([str(item) for item in items])
            print(f"Monkey {monkey_no} inspected items: {items} times.")

        round_no += 1

    return _calculate_monkey_business_level(items_inspected)


def solve_part2(monkey_operations, total_round=20):
    print("monkey", monkey_operations)
    round_no = 1
    items_inspected = defaultdict(int)

    while round_no < total_round + 1:
        monkey_operations, items_inspected = inspect_items(monkey_operations, items_inspected, divide_worry_level=False)

        print(f"\nAfter round {round_no}, the monkeys are holding items with these worry levels:")
        for monkey_no, monkey_op in monkey_operations.items():
            s = ", ".join([str(item) for item in monkey_op["items"]])
            print(f"Monkey {monkey_no}: {s}")
        print("\n\n")

        print("Items inspected")
        for monkey_no, items in items_inspected.items():
            # s = ', '.join([str(item) for item in items])
            print(f"Monkey {monkey_no} inspected items: {items} times.")

        round_no += 1

    return _calculate_monkey_business_level(items_inspected)


def solve(file_name, part=1, total_round=None):
    inputs = parse_input(file_name)
    if part == 1:
        return solve_part1(inputs, total_round=total_round or 20)

    return solve_part2(inputs, total_round=total_round or 10000)


if __name__ == "__main__":
    solve("demo_input.txt", part=1)
