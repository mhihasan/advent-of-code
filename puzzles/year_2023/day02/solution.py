import os

COLORS = ["red", "green", "blue"]


def read_input(file_name: str) -> list[str]:
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, "r") as f:
        return f.read().splitlines()


def _get_cubes_revealed(game_result):
    cubes_revealed = []
    results = game_result.split("; ")
    for result in results:
        cubes = result.split(", ")
        cube_times = {c.split(" ")[1]: int(c.split(" ")[0]) for c in cubes}
        cubes_revealed.append(cube_times)

    return cubes_revealed


def _fewest_number_of_cubes(game_result):
    cubes_revealed = _get_cubes_revealed(game_result)
    min_cubes = {}
    for cube in cubes_revealed:
        for c in COLORS:
            if cube.get(c):
                min_cubes[c] = max(min_cubes.get(c, 0), cube[c])
    return min_cubes


def solve_part1(inputs, max_cubes):
    possible_games = set()
    for line in inputs:
        game, result = line.split(": ")
        game_id = int(game.split(" ")[1])
        cubes_revealed = _get_cubes_revealed(result)
        is_game_possible = True
        for cube in cubes_revealed:
            if (
                cube.get("red", 0) > max_cubes["red"]
                or cube.get("blue", 0) > max_cubes["blue"]
                or cube.get("green", 0) > max_cubes["green"]
            ):
                is_game_possible = False
                break

        if is_game_possible:
            possible_games.add(game_id)

    return sum(possible_games)


def solve_part2(inputs):
    total = 0
    for line in inputs:
        game, result = line.split(": ")
        cubes_revealed = _fewest_number_of_cubes(result)

        multiply_cubes = cubes_revealed.get("red", 1) * cubes_revealed.get("blue", 1) * cubes_revealed.get("green", 1)
        total += multiply_cubes
    return total


def solve(file_name, part=1):
    inputs = read_input(file_name)
    if part == 1:
        return solve_part1(inputs, max_cubes={"red": 12, "blue": 14, "green": 13})

    return solve_part2(inputs)


if __name__ == "__main__":
    solve("input.txt", part=2)
