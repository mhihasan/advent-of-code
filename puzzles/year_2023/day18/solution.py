"""
Using Shoelace formula to calculate the area of a polygon given its vertices
Shoelace formula returns the interior area of a polygon, which is the area of the polygon excluding the area of the boundary cells
Using Pick's theorem to calculate the number of interior cells of a polygon given its area and number of boundary cells (Area is calculated using Shoelace formula)

Interior Area = (x1y2 + x2y3 + ... + xn-1yn + xny1 - x2y1 - x3y2 - ... - xnyn-1 - x1yn) / 2
Interior Cells = Interior Area - Total Boundary Cells / 2 + 1
"""
import os


def read_input(file_name: str) -> list[str]:
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, "r") as f:
        return f.read().splitlines()


def parse_input(file_name):
    inputs = read_input(file_name)
    return inputs


def calculate_inside_area(vertices):
    """Calculate the area of a polygon given its vertices using shoelace formula"""
    n = len(vertices)
    area = 0

    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[j][0] * vertices[i][1]

    return int(abs(area) / 2)


def find_vertices(dig_plan):
    current_row = 0
    current_col = 0
    vertices = []
    directions = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}
    for direction, distance in dig_plan:
        direction = directions[direction]

        current_row += direction[0] * distance
        current_col += direction[1] * distance
        vertices.append((current_row, current_col))
    return vertices


def solve_part1(inputs):
    dig_plans = []
    peripheral_cells = 0
    for line in inputs:
        direction, distance, _ = line.split(" ")
        peripheral_cells += int(distance)
        dig_plans.append((direction, int(distance)))

    inner_area = calculate_inside_area(find_vertices(dig_plans))
    # Find inner cells using Pick's theorem
    inner_cells = inner_area - peripheral_cells // 2 + 1
    return inner_cells + peripheral_cells


def solve_part2(inputs):
    dig_plans = []
    peripheral_cells = 0
    for line in inputs:
        _, _, hex_code = line.split(" ")

        hex_code = hex_code[2:-1]
        direction = {"0": "R", "1": "D", "2": "L", "3": "U"}[hex_code[-1]]
        distance = int(hex_code[:5], 16)

        peripheral_cells += int(distance)
        dig_plans.append((direction, int(distance)))

    inner_area = calculate_inside_area(find_vertices(dig_plans))
    # Find inner cells using Pick's theorem
    inner_cells = inner_area - peripheral_cells // 2 + 1
    return peripheral_cells + inner_cells


def solve(file_name, part=1):
    inputs = parse_input(file_name)
    if part == 1:
        return solve_part1(inputs)

    return solve_part2(inputs)


if __name__ == "__main__":
    solve("input.txt", part=2)
