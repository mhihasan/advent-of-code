from .solution import solve


def test_solves_part1():
    assert solve("demo_input.txt", part=1) == 114
    assert solve("input.txt", part=1) == 2175229206


def test_solves_part2():
    assert solve("demo_input.txt", part=2) == 2
    assert solve("input.txt", part=2) == 942
