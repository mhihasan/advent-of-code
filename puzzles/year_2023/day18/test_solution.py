from .solution import solve


def test_solves_part1():
    assert solve("demo_input.txt", part=1) == 62
    assert solve("input.txt", part=1) == 48795


def test_solves_part2():
    assert solve("demo_input.txt", part=2) == 952408144115
    assert solve("input.txt", part=2) == 40654918441248
