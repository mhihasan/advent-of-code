from input_parser import parse_input


def find_ways_to_beat(current_time, current_best):
    win_possibilities = set()

    for i in range(2, current_time // 2 + 1):
        holding_button_duration, travel_duration = i, current_time - i

        if holding_button_duration * travel_duration > current_best:
            win_possibilities.add(holding_button_duration)
            win_possibilities.add(travel_duration)

    return len(win_possibilities)


def solve_part1(inputs):
    m = 1
    for t in inputs:
        m *= find_ways_to_beat(t[0], t[1])
    return m


def solve_part2(inputs):
    time = int("".join([str(i[0]) for i in inputs]))
    distance = int("".join([str(i[1]) for i in inputs]))
    return find_ways_to_beat(time, distance)


def solve(file_name, part=1):
    inputs = parse_input(file_name)
    if part == 1:
        return solve_part1(inputs)

    return solve_part2(inputs)


if __name__ == "__main__":
    a = solve("demo_input.txt", part=1)
    print(a)
