from day2.solution import calculate_part1_score, calculate_part2_score

demo_input = ["A Y", "B X", "C Z"]


def test_solves_part1():
    assert calculate_part1_score(demo_input) == 15


def test_solves_part2():
    assert calculate_part2_score(demo_input) == 12
