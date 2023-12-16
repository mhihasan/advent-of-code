from .solution import solve


def test_solves_part1():
    assert solve("demo_input.txt", part=1) == 1320
    assert solve("input.txt", part=1) == 512283


def test_solves_part2():
    assert solve("demo_input.txt", part=2) == 145
    assert solve("input.txt", part=2) == 215827
