from .solution import solve


def test_solves_part1():
    assert solve("demo_input.txt", part=1) == 35
    assert solve("input.txt", part=1) == 650599855


def test_solves_part2():
    assert solve("demo_input.txt", part=2) == 46
    assert solve("input.txt", part=2) == 1240035
