from .solution import solve


def test_solves_part1():
    assert solve("demo_input.txt", part=1) == 95437
    assert solve("input.txt", part=1) == 2104783


def test_solves_part2():
    assert solve("demo_input.txt", part=2) == 24933642
    assert solve("input.txt", part=2) == 5883165
