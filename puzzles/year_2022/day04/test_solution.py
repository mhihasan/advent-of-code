from day04.solution import solve


def test_solves_part1():
    assert solve("demo_input.txt", part=1) == 2
    assert solve("input.txt", part=1) == 518


def test_solves_part2():
    assert solve("demo_input.txt", part=2) == 4
    assert solve("input.txt", part=2) == 909
