from day04.solution import solve


def test_solves_part1():
    assert solve("demo_input.txt", part=1) == 1
    assert solve("input.txt", part=1) == 2


def test_solves_part2():
    assert solve("demo_input.txt", part=2) == 1
    assert solve("input.txt", part=2) == 2
