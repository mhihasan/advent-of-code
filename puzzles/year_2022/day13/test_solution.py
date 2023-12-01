from day13.solution import solve


def test_solves_part1():
    assert solve("demo_input.txt", part=1) == 13
    assert solve("input.txt", part=1) == 5806


def test_solves_part2():
    assert solve("demo_input.txt", part=2) == 140
    assert solve("input.txt", part=2) == 23600
