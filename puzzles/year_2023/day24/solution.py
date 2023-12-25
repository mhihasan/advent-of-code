import os


def read_input(file_name: str) -> list[str]:
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, "r") as f:
        return f.read().splitlines()


def parse_input(file_name):
    inputs = read_input(file_name)
    stones = []
    for line in inputs:
        coord, velocity = line.split(" @ ")
        stones.append({"coord": tuple(map(int, coord.split(", "))), "velocity": tuple(map(int, velocity.split(", ")))})
    return stones


def calculate_time_range(x1, y1, vx1, vy1, area_x, area_y):
    t1_x = (area_x[0] - x1) / vx1
    t2_x = (area_x[1] - x1) / vx1

    t1_y = (area_y[0] - y1) / vy1
    t2_y = (area_x[1] - y1) / vy1

    tx_min = min(t1_x, t2_x)
    tx_max = max(t1_x, t2_x)

    ty_min = min(t1_y, t2_y)
    ty_max = max(t1_y, t2_y)

    t_range_min = max(tx_min, ty_min)
    t_range_max = min(tx_max, ty_max)

    return t_range_min, t_range_max


def find_intersection_time(t_range_1, t_range_2):
    t1_min, t1_max = t_range_1
    t2_min, t2_max = t_range_2

    # if t1_min > t2_max or t2_min > t1_max:
    #     return None

    return max(t1_min, t2_min), min(t1_max, t2_max)


def calculate_position(x, y, z, vx, vy, vz, t):
    return x + vx * t, y + vy * t


def calculate_locations(stone, velocity, t_min, t_max, area_x_min, area_x_max, area_y_min, area_y_max):
    x, y, z = stone
    vx, vy, vz = velocity
    # t_min = max(t_min, 1)
    # t_max = min(t_max, 1)

    locations = [calculate_position(x, y, z, vx, vy, vz, t_min), calculate_position(x, y, z, vx, vy, vz, t_max)]
    # t = max(t_min, 1)
    # while t <= t_max:
    #     new_x, new_y , _ = calculate_position(x, y, z, vx, vy, vz, t)
    #     if area_x_min <= new_x <= area_x_max and area_y_min <= new_y <= area_y_max:
    #         locations.append((new_x, new_y, t))
    #     t += 1

    return locations


def find_line_intersection(p1_x, p1_y, p2_x, p2_y, q1_x, q1_y, q2_x, q2_y):
    # Calculate slopes (m) of each line
    m_A = (p2_y - p1_y) / (p2_x - p1_x) if p2_x != p1_x else None  # Check for vertical line
    m_B = (q2_y - q1_y) / (q2_x - q1_x) if q2_x != q1_x else None

    # Check for parallel lines
    if m_A == m_B:
        return None
        # return "Lines are parallel" if m_A is not None else "Both lines are vertical"

    # Calculate y-intercepts (b) of each line
    b_A = p1_y - m_A * p1_x if m_A is not None else p1_x  # x coordinate for vertical line
    b_B = q1_y - m_B * q1_x if m_B is not None else q1_x

    # Solve for x and y
    if m_A is not None and m_B is not None:
        x = (b_B - b_A) / (m_A - m_B)
        y = m_A * x + b_A
    elif m_A is None:  # Line A is vertical
        x = b_A
        y = m_B * x + b_B
    else:  # Line B is vertical
        x = b_B
        y = m_A * x + b_A

    return (x, y)


def calculate_time(x, x1, vx):
    return (x - x1) / vx


def find_intersection_point(stone1, stone2, area_min, area_max):
    x1, y1, z1 = stone1["coord"]
    vx1, vy1, vz1 = stone1["velocity"]

    x2, y2, z2 = stone2["coord"]
    vx2, vy2, vz2 = stone2["velocity"]

    area_x = (area_min, area_max)
    area_y = (area_min, area_max)

    t1, t2 = calculate_time_range(x1, y1, vx1, vy1, area_x, area_y)
    t3, t4 = calculate_time_range(x2, y2, vx2, vy2, area_x, area_y)

    t_range = find_intersection_time((t1, t2), (t3, t4))
    # print("t_range", t_range)
    t_range = (max(t_range[0], 0), max(t_range[1], 1))

    if not t_range:
        return None

    # locations1 = calculate_locations(stone1["coord"], stone1["velocity"], t_range[0], t_range[1], area_x[0], area_x[1], area_y[0], area_y[1])
    # locations2 = calculate_locations(stone2["coord"], stone2["velocity"], t_range[0], t_range[1], area_x[0], area_x[1], area_y[0], area_y[1])

    locations_s1 = calculate_locations((x1, y1, z1), (vx1, vy1, vz1), *t_range, *area_x, *area_y)
    if not locations_s1:
        return
    # print("locations_s1", locations_s1)

    locations_s2 = calculate_locations((x2, y2, z2), (vx2, vy2, vz2), *t_range, *area_x, *area_y)
    if not locations_s2:
        return
    # print("locations_s2", locations_s2)

    intersection = find_line_intersection(
        p1_x=locations_s1[0][0],
        p1_y=locations_s1[0][1],
        p2_x=locations_s1[1][0],
        p2_y=locations_s1[1][1],
        q1_x=locations_s2[0][0],
        q1_y=locations_s2[0][1],
        q2_x=locations_s2[1][0],
        q2_y=locations_s2[1][1],
    )
    if not intersection:
        return None
    t1 = calculate_time(intersection[0], x1, vx1)
    t2 = calculate_time(intersection[0], x2, vx2)
    # print(t1, t2)
    if t1 <= 0 or t2 <= 0:
        # print("t1", t1)
        return None
    # print("intersection", intersection)
    return intersection


def is_within_area(intersection_point, area_min, area_max):
    x, y = intersection_point
    return area_min <= x <= area_max and area_min <= y <= area_max


def solve_part1(inputs, area_min=7, area_max=27):
    total = 0
    # input_min = 200000000000000
    # input_max = 400000000000000
    for i, stone1 in enumerate(inputs):
        for j, stone2 in enumerate(inputs[i + 1 :]):
            intersection_point = find_intersection_point(
                stone1, stone2, area_min=200000000000000, area_max=400000000000000
            )
            if intersection_point and is_within_area(
                intersection_point, area_min=200000000000000, area_max=400000000000000
            ):
                print(f"<<<<<<<<{stone1}>>>>>>>> {stone2} >>>>>>>>> {intersection_point}")
                total += 1
            # print()
    print(total)


def solve_part2(inputs):
    pass


def solve(file_name, part=1):
    inputs = parse_input(file_name)
    if part == 1:
        return solve_part1(inputs)

    return solve_part2(inputs)


if __name__ == "__main__":
    solve("input.txt", part=1)
    # solve("input.txt", part=1)


# def parse_stone(stone):
#     stone, velocity = stone.split(" @ ")
#     stone = tuple(map(int, stone.split(", ")))
#     velocity = tuple(map(int, velocity.split(", ")))
#     return {
#         "coord": stone,
#         "velocity": velocity
#     }
#
#
# if __name__ == '__main__':
#     solve(parse_stone("19, 13, 30 @ -2, 1, -2"), parse_stone("18, 19, 22 @ -1, -1, -2"), area_min=7, area_max=27)
#     # solve(parse_stone("19, 13, 30 @ -2, 1, -2"), parse_stone("20, 25, 34 @ -2, -2, -4"), area_min=7, area_max=27)
#     # solve(parse_stone("19, 13, 30 @ -2, 1, -2"), parse_stone("12, 31, 28 @ -1, -2, -1"), area_min=7, area_max=27)
#     # solve(parse_stone("19, 13, 30 @ -2, 1, -2"), parse_stone("20, 19, 15 @ 1, -5, -3"), area_min=7, area_max=27)
#     # solve(parse_stone("18, 19, 22 @ -1, -1, -2"), parse_stone("20, 25, 34 @ -2, -2, -4"), area_min=7, area_max=27)
#     # solve(parse_stone("18, 19, 22 @ -1, -1, -2"), parse_stone("12, 31, 28 @ -1, -2, -1"), area_min=7, area_max=27)
#     # solve(parse_stone("18, 19, 22 @ -1, -1, -2"), parse_stone("20, 19, 15 @ 1, -5, -3"), area_min=7, area_max=27)
#     # solve(parse_stone("20, 25, 34 @ -2, -2, -4"), parse_stone("12, 31, 28 @ -1, -2, -1"), area_min=7, area_max=27)
#     solve(parse_stone("20, 25, 34 @ -2, -2, -4"), parse_stone("20, 19, 15 @ 1, -5, -3"), area_min=7, area_max=27)
#     # solve(parse_stone("12, 31, 28 @ -1, -2, -1"), parse_stone("20, 19, 15 @ 1, -5, -3"), area_min=7, area_max=27)
