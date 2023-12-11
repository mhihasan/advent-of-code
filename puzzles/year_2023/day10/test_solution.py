from .solution import solve


def test_solves_part1():
    assert solve("demo_input.txt", part=1) == 8
    assert solve("input.txt", part=1) == 6738


def test_solves_part2():
    assert solve("example1_part2.txt", part=2) == 4
    assert solve("example2_part2.txt", part=2) == 8
    assert solve("example3_part2.txt", part=2) == 10
    assert solve("input.txt", part=2) == 579
