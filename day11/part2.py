import math
import operator
from collections import defaultdict
from textwrap import indent  # noqa

from day11.file_parser import parse_input

WORRY_LEVEL_DIVISOR = 3

OPERATOR = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
}


def _calc_new_worry_level(current_worry_level, operation):
    left_operand = operation["left_operand"] == "old" and current_worry_level or operation["left_operand"]
    right_operand = operation["right_operand"] == "old" and current_worry_level or operation["right_operand"]
    return OPERATOR[operation["operator"]](left_operand, right_operand)


def _new_monkey_to_throw_item(new_worry_level, test):
    is_divisible = new_worry_level % test["divisible_by"] == 0
    return test["true"] if is_divisible else test["false"]


def inspect_item(item, monkey_op, divide_worry_level):
    new_worry_level = _calc_new_worry_level(item, monkey_op["operation"])
    if divide_worry_level:
        new_worry_level //= 3
        # print(indent(f"Worry level is divided by {WORRY_LEVEL_DIVISOR} to {new_worry_level}", "    "))

    print(f"new worry level: {new_worry_level}")
    new_monkey_no = _new_monkey_to_throw_item(new_worry_level, monkey_op["test"])
    # print(f"Time taken for finding new monkey no: {time.perf_counter() - t1}")

    # print(indent(f"Item with worry level {new_worry_level} is thrown to monkey {new_monkey_no}.", "    "))
    return new_monkey_no, new_worry_level


def inspect_item_by_modulo(item, monkey_op, divide_worry_level):
    operation = monkey_op["operation"]
    left_operand = item if operation["left_operand"] == "old" else operation["left_operand"]
    right_operand = item if operation["right_operand"] == "old" else operation["right_operand"]

    test = monkey_op["test"]
    divisor = test["divisible_by"]

    oper = OPERATOR[operation["operator"]]
    print("operator", oper, left_operand, right_operand, type(left_operand), type(right_operand), type(divisor))
    level = OPERATOR[operation["operator"]](left_operand, right_operand)
    # new_worry_level = oper(left_operand % divisor, right_operand % divisor)
    res, reminder = divmod(oper(left_operand % divisor, right_operand % divisor), divisor)
    next_monkey = test["true"] if reminder else test["false"]
    return next_monkey, level


def inspect_items(monkey_operations, items_inspected, divide_worry_level: bool = True):
    for monkey_no, monkey_op in monkey_operations.items():
        # print(f"Monkey {monkey_no}:")

        total_items = len(monkey_op["items"])

        while monkey_op["items"]:
            item = monkey_op["items"].popleft()

            # print(indent(f"Monkey inspects an item with a worry level of {item}.", "  "))
            new_monkey_no, new_worry_level = inspect_item_by_modulo(item, monkey_op, divide_worry_level)
            monkey_operations[new_monkey_no]["items"].append(new_worry_level)

        # print(f"Time taken for inspecting items, monkey, {monkey_no}: {time.perf_counter() - t1}")

        items_inspected[monkey_no] += total_items

    return monkey_operations, items_inspected


def _calculate_monkey_business_level(items_inspected, active_monkeys: int = 2):
    most_inspected_items = sorted(items_inspected.values(), reverse=True)[:active_monkeys]
    return math.prod(most_inspected_items)


def calculate_monkey_business_level(monkey_operations, divide_worry_level=True, total_round=1):
    round_no = 1
    items_inspected = defaultdict(int)

    while round_no < total_round + 1:
        monkey_operations, items_inspected = inspect_items(monkey_operations, items_inspected, divide_worry_level)

        # print(f"\nAfter round {round_no}, the monkeys are holding items with these worry levels:")
        # for monkey_no, monkey_op in monkey_operations.items():
        #     s = ", ".join([str(item) for item in monkey_op["items"]])
        #     print(f"Monkey {monkey_no}: {s}")
        # print("\n\n")

        # print(f"<<<<<<< Items inspected: {round_no} >>>>>>>>>: {time.perf_counter() - t1}")
        # for monkey_no, items_count in items_inspected.items():
        # s = ', '.join([str(item) for item in items])
        # print(f"Monkey {monkey_no} inspected items: {items_count} times.")

        round_no += 1

    return _calculate_monkey_business_level(items_inspected)


def solve_part2(inputs):
    pass


def solve(file_name, part=1):
    inputs = parse_input(file_name)
    if part == 1:
        return calculate_monkey_business_level(inputs, divide_worry_level=True, total_round=20)

    return calculate_monkey_business_level(inputs, divide_worry_level=False, total_round=20)


if __name__ == "__main__":
    v = solve("demo_input.txt", part=2)
    print(v)
