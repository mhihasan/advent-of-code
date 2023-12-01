from day21.file_parser import parse_input


def find_number_to_yell(monkey_jobs, monkey):
    if isinstance(monkey_jobs.get(monkey), int):
        return monkey_jobs[monkey]

    monkey_job = monkey_jobs[monkey]

    left_monkey = monkey_job["left_operand"]
    right_monkey = monkey_job["right_operand"]
    math_operation = monkey_job["operator"]
    result = int(
        math_operation(find_number_to_yell(monkey_jobs, left_monkey), find_number_to_yell(monkey_jobs, right_monkey))
    )
    monkey_jobs[monkey] = result
    return result


def solve_part1(monkey_jobs, monkey="root"):
    print("monkey_jobs", monkey_jobs)
    return find_number_to_yell(monkey_jobs, monkey)


def solve_part2(monkey_jobs, monkey="root"):
    left_monkey = monkey_jobs[monkey]["left_operand"]
    right_monkey = monkey_jobs[monkey]["right_operand"]
    monkey_jobs["humn"] = 301
    left_val = find_number_to_yell(monkey_jobs, left_monkey)
    right_val = find_number_to_yell(monkey_jobs, right_monkey)
    print(left_val)
    print(right_val)


def solve(file_name, part=1):
    monkey_jobs = parse_input(file_name)
    if part == 1:
        return solve_part1(monkey_jobs, monkey="root")

    return solve_part2(monkey_jobs, monkey="root")


if __name__ == "__main__":
    r = solve("demo_input.txt", part=2)
    print(r)
