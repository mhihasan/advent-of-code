from .calorie_counter import most_calories_carried, solve


def test_returns_most_calories():
    input_calories = ["1", "2", "", "2", "", "2", "3", "", "3", "4"]
    max_calories = most_calories_carried(input_calories)
    assert max_calories == 7

    max_calories = most_calories_carried(input_calories, 3)
    assert max_calories == 15


def test_solves_part1():
    assert solve("demo_input.txt", n=1) == 24000
    assert solve("input.txt", n=1) == 75622


def test_solves_part2():
    assert solve("demo_input.txt", n=3) == 45000
    assert solve("input.txt", n=3) == 213159
