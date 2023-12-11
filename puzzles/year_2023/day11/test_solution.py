from .solution import solve


def test_solves_part1():
    assert solve("demo_input.txt", part=1) == 374
    assert solve("input.txt", part=1) == 10313550


def test_solves_part2():
    assert solve("demo_input.txt", part=2) == 82000210
    assert solve("input.txt", part=2) == 611998089572
