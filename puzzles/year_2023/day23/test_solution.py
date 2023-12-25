from .part1 import solve as solve_part1
from .part2 import solve as solve_part2


def test_solves_part1():
    assert solve_part1("demo_input.txt", part=1) == 94
    assert solve_part1("input.txt", part=1) == 2430


def test_solves_part2():
    assert solve_part2("demo_input.txt", part=2) == 154
    assert solve_part2("input.txt", part=2) == 6534
