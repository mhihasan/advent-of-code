from calorie_counter import most_calories_carried


def test_returns_most_calories():
    input_calories = ["1", "2", "", "2", "", "2", "3", "", "3", "4"]
    max_calories = most_calories_carried(input_calories)
    assert max_calories == 7

    max_calories = most_calories_carried(input_calories, 3)
    assert max_calories == 15
