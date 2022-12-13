from day13.solution import solve, compare


def test_solves_part1():
    assert solve("demo_input.txt", part=1) == 13
    assert solve("input.txt", part=1) == 5806


def test_solves_part2():
    assert solve("demo_input.txt", part=2) == 1
    assert solve("input.txt", part=2) == 2


class TestIsRightSide:
    def test_is_right_side(self):
        assert compare([[4, 4], 4, 4], [[4, 4], 4, 4, 4])["right_order"] is True
        assert compare([1, 1, 3, 1, 1], [1, 1, 5, 1, 1])["right_order"] is True
