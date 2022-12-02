from day2.solution import solve


def test_solves_part1():
    assert solve("demo_input.txt", part=1) == 15
    assert solve("input.txt", part=1) == 11603


def test_solves_part2():
    assert solve("demo_input.txt", part=2) == 12
    assert solve("input.txt", part=2) == 12725
