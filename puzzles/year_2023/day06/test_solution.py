from .solution import solve


def test_solves_part1():
    assert solve("demo_input.txt", part=1) == 288
    assert solve("input.txt", part=1) == 140220


def test_solves_part2():
    assert solve("demo_input.txt", part=2) == 71503
    assert solve("input.txt", part=2) == 39570185
