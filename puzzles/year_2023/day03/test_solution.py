from .solution import solve


def test_solves_part1():
    assert solve("demo_input.txt", part=1) == 4361
    assert solve("input.txt", part=1) == 498559


def test_solves_part2():
    assert solve("demo_input.txt", part=2) == 467835
    assert solve("input.txt", part=2) == 72246648
