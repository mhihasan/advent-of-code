from .solution import solve


def test_solves_part1():
    assert solve("demo_input.txt", part=1) == 46
    assert solve("input.txt", part=1) == 6816


def test_solves_part2():
    assert solve("demo_input.txt", part=2) == 51
    assert solve("input.txt", part=2) == 8163
