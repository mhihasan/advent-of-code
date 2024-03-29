from .solution import solve


def test_solves_part1():
    assert solve("demo_input.txt", part=1) == 13
    assert solve("input.txt", part=1) == 18519


def test_solves_part2():
    assert solve("demo_input.txt", part=2) == 30
    assert solve("input.txt", part=2) == 11787590
