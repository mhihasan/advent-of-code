from day12.solution import solve


def test_solves_part1():
    assert solve("demo_input.txt", part=1) == 31
    assert solve("input.txt", part=1) == 437


def test_solves_part2():
    assert solve("demo_input.txt", part=2) == 29
    assert solve("input.txt", part=2) == 430
