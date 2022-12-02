from day2.solution import solve

demo_input = ["A Y", "B X", "C Z"]


def test_solves_part1():
    assert solve("demo_input.txt", part=1) == 15
    assert solve("input.txt", part=1) == 11603


def test_solves_part2():
    assert solve("demo_input.txt", part=2) == 12
    assert solve("input.txt", part=2) == 12725
