from .solution import solve


def test_solves_part1():
    assert solve("demo_input_part1.txt", part=1) == 2
    assert solve("input.txt", part=1) == 17287


def test_solves_part2():
    assert solve("demo_input_part2.txt", part=2) == 6
    assert solve("input.txt", part=2) == 18625484023687
