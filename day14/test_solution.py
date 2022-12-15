from day14.solution import solve


def test_solves_part1():
    assert solve("demo_input.txt", part=1) == 24
    assert solve("input.txt", part=1) == 728


def test_solves_part2():
    assert solve("demo_input.txt", part=2) == 93
    assert solve("input.txt", part=2) == 27623
