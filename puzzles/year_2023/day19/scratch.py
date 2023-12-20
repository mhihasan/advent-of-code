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


def evaluate_expression(conditions_str, x, m, a, s):
    # Extract the function name and conditions string

    # Parse conditions and actions
    conditions = conditions_str.split(",")

    for condition in conditions:
        # Split each condition into the condition and action
        cond, action = condition.split(":")

        # Replace parameter names with their values in the condition
        cond_eval = cond.replace("x", str(x)).replace("m", str(m)).replace("a", str(a)).replace("s", str(s))

        # Evaluate the condition
        if eval(cond_eval):
            return action

    # If no conditions are met
    return None


def evaluate_expressions(expressions, x, m, a, s, current_expression="px"):
    # Extract the function name and conditions string

    result = None
    while result not in ["A", "R"]:
        result = evaluate_expression(expressions[current_expression], x, m, a, s)
        current_expression = result

    return result


# Example usage
# result_px = evaluate_expression("px{a<2006:qkq,m>2090:A,rfg}", x=0, m=2100, a=2005, s=0)
# result_rfg = evaluate_expression("rfg{s<537:gd,x>2440:R,A}", x=2500, m=0, a=0, s=500)
# result_gd = evaluate_expression("gd{a>3333:R,R}", x=0, m=0, a=4000, s=0)
#
# print("Result of px:", result_px)
# print("Result of rfg:", result_rfg)
# print("Result of gd:", result_gd)

if __name__ == "__main__":
    expressions = ["px{a<2006:qkq,m>2090:A,rfg}", "rfg{s<537:gd,x>2440:R,A}", "gd{a>3333:R,R}", "qkq{x<1416:A,R}"]
    out = parse_expressions(expressions)
    print("out", out)
    r = evaluate_expressions(out, x=0, m=2100, a=2005, s=0)
    print(r)
