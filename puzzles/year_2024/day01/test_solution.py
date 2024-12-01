from .solution import solve


def test_solves_part1():
    assert solve("demo_input.txt", part=1) == 11
    assert solve("input.txt", part=1) == 1590491


def test_solves_part2():
    assert solve("demo_input.txt", part=2) == 31
    assert solve("input.txt", part=2) == 22588371
