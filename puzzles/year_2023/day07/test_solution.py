from .part1 import solve as solve_part1
from .part2 import solve as solve_part2


def test_solves_part1():
    assert solve_part1("demo_input.txt", part=1) == 6440
    assert solve_part1("input.txt", part=1) == 250946742


def test_solves_part2():
    assert solve_part2("demo_input.txt") == 5905
    assert solve_part2("input.txt") == 251824095
