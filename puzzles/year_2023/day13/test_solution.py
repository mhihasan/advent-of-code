from .solution import solve


def test_solves_part1():
    assert solve("demo_input.txt", part=1) == 405
    assert solve("input.txt", part=1) == 33122


def test_solves_part2():
    assert solve("demo_input.txt", part=2) == 400
    assert solve("input.txt", part=2) == 32312
