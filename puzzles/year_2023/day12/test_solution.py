from .solution import solve


def test_solves_part1():
    assert solve("demo_input.txt", part=1) == 21
    assert solve("input.txt", part=1) == 8419


def test_solves_part2():
    assert solve("demo_input.txt", part=2) == 525152
    assert solve("input.txt", part=2) == 160500973317706
