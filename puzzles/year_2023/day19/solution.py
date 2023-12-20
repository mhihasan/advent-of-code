import os


def read_input(file_name: str) -> list[str]:
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, "r") as f:
        return f.read()


def parse_input(file_name):
    inputs = read_input(file_name)
    workflows, parts = inputs.split("\n\n")
    parts = parts.split("\n")
    workflows = workflows.split("\n")
    return {"workflows": workflows, "parts": parts}


def parse_expressions(expressions):
    "Parse expressions into a dictionary"
    parsed_expressions = {}
    for expression in expressions:
        # Extract the function name and conditions string
        func_name, conditions_str = expression.split("{", 1)
        conditions_str = conditions_str.strip("}")

        # Parse conditions and actions
        # conditions = conditions_str.split(',')

        parsed_expressions[func_name] = conditions_str

    return parsed_expressions


def evaluate_expression(conditions_str, params):
    conditions = conditions_str.split(",")

    for condition in conditions:
        if ":" not in condition:
            return condition

        cond, action = condition.split(":")

        for k, v in params.items():
            cond = cond.replace(k, str(v))

        if eval(cond):
            return action

    raise Exception("No conditions met")


def evaluate_expressions(expressions, params, current_expression="in"):
    result = None
    while result not in ["A", "R"]:
        result = evaluate_expression(expressions[current_expression], params)
        current_expression = result

    return result


def get_part_parameters(part):
    part = part[1:-1]
    params = {}
    for p in part.split(","):
        k, v = p.split("=")
        params[k] = int(v)
    return params


def solve_part1(inputs):
    workflows = inputs["workflows"]
    parts = inputs["parts"]

    expressions = parse_expressions(workflows)
    total = 0
    for part in parts:
        params = get_part_parameters(part)
        result = evaluate_expressions(expressions, params)
        if result == "A":
            total += sum(params.values())

    return total


def solve_part2(inputs):
    workflows = inputs["workflows"]
    parts = inputs["parts"]

    expressions = parse_expressions(workflows)
    total = 0
    for part in parts:
        params = get_part_parameters(part)
        result = evaluate_expressions(expressions, params)
        if result == "A":
            total += sum(params.values())

    return total


def solve(file_name, part=1):
    inputs = parse_input(file_name)
    if part == 1:
        return solve_part1(inputs)

    return solve_part2(inputs)


if __name__ == "__main__":
    solve("input.txt", part=1)
