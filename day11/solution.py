import math
from collections import defaultdict
from textwrap import indent

from day11.file_parser import parse_input

WORRY_LEVEL_DIVISOR = 3


def _calc_new_worry_level(current_worry_level, operation):
    left_operand = operation["left_operand"] == "old" and current_worry_level or operation["left_operand"]
    right_operand = operation["right_operand"] == "old" and current_worry_level or operation["right_operand"]
    operator = operation["operator"]
    return eval(f"{left_operand} {operator} {right_operand}") // WORRY_LEVEL_DIVISOR


def _new_monkey_to_throw_item(new_worry_level, test):
    is_divisible = eval(f'{new_worry_level} % {test["divisible_by"]}') == 0
    return test["true"] if is_divisible else test["false"]


def inspect_item(item, monkey_op):
    new_worry_level = _calc_new_worry_level(item, monkey_op["operation"])

    print(indent(f"Worry level is divided by {WORRY_LEVEL_DIVISOR} to {new_worry_level}", "    "))
    new_monkey_no = _new_monkey_to_throw_item(new_worry_level, monkey_op["test"])

    print(indent(f"Item with worry level {new_worry_level} is thrown to monkey {new_monkey_no}.", "    "))
    return new_monkey_no, new_worry_level


def inspect_items(monkey_operations, items_inspected):
    for monkey_no, monkey_op in monkey_operations.items():
        print(f"Monkey {monkey_no}:")

        while monkey_op["items"]:
            item = monkey_op["items"].popleft()

            print(indent(f"Monkey inspects an item with a worry level of {item}.", "  "))
            new_monkey_no, new_worry_level = inspect_item(item, monkey_op)
            monkey_operations[new_monkey_no]["items"].append(new_worry_level)

            items_inspected[monkey_no].append(item)

    return monkey_operations, items_inspected


def _calculate_monkey_business_level(items_inspected, active_monkeys: int = 2):
    most_inspected_items = sorted([len(items) for items in items_inspected.values()], reverse=True)[:active_monkeys]
    return math.prod(most_inspected_items)


def solve_part1(monkey_operations, total_round=20):
    print("monkey", monkey_operations)
    round_no = 1
    items_inspected = defaultdict(list)

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
            print(f"Monkey {monkey_no} inspected items: {len(items)} times.")

        round_no += 1

    return _calculate_monkey_business_level(items_inspected)


def solve_part2(inputs):
    pass


def solve(file_name, part=1):
    inputs = parse_input(file_name)
    if part == 1:
        return solve_part1(inputs)

    return solve_part2(inputs)


if __name__ == "__main__":
    solve("demo_input.txt", part=1)
