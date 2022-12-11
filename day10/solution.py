import os


def read_input(file_name: str) -> list[str]:
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, "r") as f:
        return f.read().splitlines()


CYCLE_COUNT = {"addx": 2, "noop": 1}


def solve_part1(inputs):
    total_cycle_count = 0
    register_value = 1
    register_values = {}
    initial_cycle = 20
    end_cycle = 220
    increment = 40

    cycles = [cycle for cycle in range(initial_cycle, end_cycle + 1, increment)]

    i = 0
    current_cycle = cycles[i]

    for line in inputs:
        operation = line.split(" ")
        operator = operation[0]
        try:
            operand = int(operation[1])
        except Exception:
            operand = 0

        cycle_count = CYCLE_COUNT[operator]

        total_cycle_count += cycle_count

        if current_cycle <= total_cycle_count:
            register_values[current_cycle] = register_value
            i += 1
            if i == len(cycles):
                break

            current_cycle = cycles[i]

        register_value += operand

        print(f"Cycle count: {total_cycle_count}, value: {register_value}")

    signal_strength = sum([cycle * val for cycle, val in register_values.items()])
    return signal_strength


def _chunkify(arr, n):
    return "\n".join([arr[i : i + n] for i in range(0, len(arr), n)])


def solve_part2(inputs):
    pixel_width = 40
    pixel_height = 6
    pixel_dimensions = pixel_width * pixel_height
    pixel_pos = 0
    register_value = 1
    crt_image = ""

    for line in inputs:
        operation = line.split(" ")
        operator = operation[0]
        try:
            operand = int(operation[1])
        except Exception:
            operand = 0

        cycle_count = CYCLE_COUNT[operator]

        for i in range(cycle_count):
            if register_value - 1 <= (pixel_pos % pixel_width) <= register_value + 1:
                crt_image += "#"
            else:
                crt_image += "."

            pixel_pos += 1
            if pixel_pos >= pixel_dimensions:
                break

        register_value += operand

    return _chunkify(crt_image, pixel_width)


def solve(file_name, part=1):
    inputs = read_input(file_name)
    if part == 1:
        return solve_part1(inputs)

    return solve_part2(inputs)


if __name__ == "__main__":
    solve("demo_input.txt", part=2)
