from day08.solution import solve


def test_solves_part1():
    assert solve("demo_input.txt", part=1) == 21
    assert solve("input.txt", part=1) == 1703


def test_solves_part2():
    assert solve("demo_input.txt", part=2) == 8
    assert solve("input.txt", part=2) == 496650
