from .solution import solve


def test_solves_part1():
    assert solve("demo_input.txt", part=1) == 136
    assert solve("input.txt", part=1) == 108826


def test_solves_part2():
    assert solve("demo_input.txt", part=2) == 64
    assert solve("input.txt", part=2) == 99291
