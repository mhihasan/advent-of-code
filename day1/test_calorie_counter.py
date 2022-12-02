from .calorie_counter import most_calories_carried


demo_input = ["1000", "2000", "3000", "", "4000", "", "5000", "6000", "", "7000", "8000", "9000", "", "10000"]


def test_solves_part1():
    assert most_calories_carried(demo_input, n=1) == 24000


def test_solves_part2():
    assert most_calories_carried(demo_input, n=3) == 45000
