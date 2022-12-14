from day09.solution import solve


def test_solves_part1():
    assert solve("demo_input.txt", part=1) == 13
    assert solve("input.txt", part=1) == 5981


def test_solves_part2():
    assert solve("demo_input_part2.txt", part=2) == 36
    # assert solve("input.txt", part=2) == 2
