from day06.solution import solve


def test_solves_part1():
    assert solve("demo_input.txt", part=1) == 7
    assert solve("input.txt", part=1) == 1702


def test_solves_part2():
    assert solve("demo_input.txt", part=2) == 19
    assert solve("input.txt", part=2) == 3559
