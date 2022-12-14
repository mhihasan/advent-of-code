import math
import os

UP = (0, 1)
DOWN = (0, -1)
LEFT = (-1, 0)
RIGHT = (1, 0)
DIRECTIONS = {"U": UP, "D": DOWN, "L": LEFT, "R": RIGHT}


def read_input(file_name: str) -> list[str]:
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, "r") as f:
        return f.read().splitlines()


def calculate_distance(head, tail):
    vertical_distance = head[0] - tail[0]
    horizontal_distance = head[1] - tail[1]
    return math.sqrt(math.pow(vertical_distance, 2) + math.pow(horizontal_distance, 2))


def solve_part1(inputs, total_knots=2):
    knot_positions = [(0, 0)] * total_knots
    visited_by_tail = [(0, 0)]

    for line in inputs:
        direction, distance = line.split(" ")
        distance = int(distance)
        direction_delta = DIRECTIONS[direction]

        print(f"<<<<<<<<<<- Processing move: {line} ->>>>>>>>>>>>>")
        print("direction delta", direction_delta)
        visited = []
        while distance > 0:
            print("-------------------")

            tail = knot_positions[-1]
            knot_positions[0] = (
                knot_positions[0][0] + direction_delta[0],
                knot_positions[0][1] + direction_delta[1],
            )

            for i in range(1, total_knots):
                # knot_positions[0] = (
                #     knot_positions[0][0] + direction_delta[0],
                #     knot_positions[0][1] + direction_delta[1],
                # )
                # knot_positions = move_knots(knot_positions, direction_delta, curr=i)

                prev_knot, curr_knot = move_two_knots(knot_positions[i - 1], knot_positions[i], direction_delta)
                knot_positions[i - 1] = prev_knot
                knot_positions[i] = curr_knot

            distance -= 1

            if knot_positions[-1] != tail:
                visited.append(knot_positions[-1])
                print("Tailed moved to: ", knot_positions[-1])

        print(f"Knot positions after: {line}:", knot_positions)
        print(f"Visited nodes by move {line}:", visited)
        visited_by_tail.extend(visited)

    visited_at_least_once = len((set(visited_by_tail)))
    print("Total visited", visited_at_least_once)
    return visited_at_least_once


def move_knots(knot_positions, direction_delta, curr):
    prev = curr - 1
    knot_positions[prev] = (
        knot_positions[prev][0] + direction_delta[0],
        knot_positions[prev][1] + direction_delta[1],
    )

    dist = calculate_distance(knot_positions[prev], knot_positions[curr])

    print("head", knot_positions[0])
    print("tail", knot_positions[1])
    print("distance", dist)

    if dist < 2:
        return knot_positions

    if dist == 2:
        knot_positions[curr] = (
            knot_positions[curr][0] + direction_delta[0],
            knot_positions[curr][1] + direction_delta[1],
        )

    elif dist > 2:
        knot_positions[curr] = (
            knot_positions[curr][0] + (1 if knot_positions[prev][0] > knot_positions[curr][0] else -1),
            knot_positions[curr][1] + (1 if knot_positions[prev][1] > knot_positions[curr][1] else -1),
        )
    return knot_positions


def move_two_knots(prev_knot, curr_knot, direction_delta):
    dist = calculate_distance(prev_knot, curr_knot)

    # print("head", knot_positions[0])
    # print("tail", knot_positions[1])
    print("distance", dist)

    if dist < 2:
        return prev_knot, curr_knot

    if dist == 2:
        curr_knot = (
            curr_knot[0] + direction_delta[0],
            curr_knot[1] + direction_delta[1],
        )

    elif dist > 2:
        curr_knot = (
            curr_knot[0] + (1 if prev_knot[0] > curr_knot[0] else -1),
            curr_knot[1] + (1 if prev_knot[1] > curr_knot[1] else -1),
        )
    return prev_knot, curr_knot


def solve_part2(inputs, knots=10):
    head_row, head_col = (0, 0)
    tail_row, tail_col = (0, 0)
    visited_by_tail = [(tail_row, tail_col)]
    knot_distances = [(0, 0)] * knots

    for line in inputs:
        direction, distance = line.split(" ")
        distance = int(distance)
        direction_delta = DIRECTIONS[direction]

        print(f"<<<<<<<<<<- Processing move: {line} ->>>>>>>>>>>>>")
        print("direction delta", direction_delta)
        visited = []
        while distance > 0:
            print("-------------------")
            head_row, head_col = (
                head_row + direction_delta[0],
                head_col + direction_delta[1],
            )
            tail_row, tail_col = knot_distances[knots - 1]

            knot_distances[0] = (head_row, head_col)

            i = 1

            while i < knots:
                current_knot_row, current_knot_col = knot_distances[i]
                prev_knot_row, prev_knot_col = knot_distances[i - 1]

                dist = calculate_distance(knot_distances[i], knot_distances[i + 1])
                if dist < 2:
                    break

                if dist == 2:
                    current_knot_row, current_knot_col = (
                        prev_knot_row + direction_delta[0],
                        prev_knot_col + direction_delta[1],
                    )

                elif dist > 2:
                    current_knot_row += 1 if prev_knot_row > current_knot_row else -1
                    current_knot_col += 1 if prev_knot_col > current_knot_col else -1

                knot_distances[i] = (current_knot_row, current_knot_col)

                i += 1

            if knot_distances[knots - 1] != (tail_row, tail_col):
                visited.append((tail_row, tail_col))
                print("Tail moved to: ", (tail_row, tail_col))

            distance -= 1

        print(f"Visited nodes by move {line}:", visited)
        visited_by_tail.extend(visited)

    visited_at_least_once = len((set(visited_by_tail)))
    print("Total visited", visited_at_least_once)
    return visited_at_least_once


def solve(file_name, part=1):
    inputs = read_input(file_name)
    if part == 1:
        return solve_part1(inputs)

    return solve_part1(inputs, total_knots=10)


if __name__ == "__main__":
    solve("demo_input.txt", part=2)
