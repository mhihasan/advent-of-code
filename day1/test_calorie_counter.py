from .calorie_counter import solve


def test_solves_part1():
    assert solve("demo_input.txt", n=1) == 24000
    assert solve("input.txt", n=1) == 75622


def test_solves_part2():
    assert solve("demo_input.txt", n=3) == 45000
    assert solve("input.txt", n=3) == 213159
