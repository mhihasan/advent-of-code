from day3.solution import solve


def test_solves_part1():
    assert solve("demo_input.txt") == 157
    assert solve("input.txt") == 7428


def test_solves_part2():
    assert solve("demo_input.txt", part=2) == 70
    assert solve("input.txt", part=2) == 2650
