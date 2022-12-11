from day11.solution import solve


def test_solves_part1():
    assert solve("demo_input.txt", part=1) == 10605
    assert solve("input.txt", part=1) == 108240


def test_solves_part2():
    assert solve("demo_input.txt", part=2) == 1
    assert solve("input.txt", part=2) == 2
