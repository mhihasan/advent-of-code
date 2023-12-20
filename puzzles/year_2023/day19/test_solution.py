import pytest

from .solution import solve


def test_solves_part1():
    assert solve("demo_input.txt", part=1) == 19114
    assert solve("input.txt", part=1) == 395382


@pytest.mark.skip
def test_solves_part2():
    assert solve("demo_input.txt", part=2) == 1
    assert solve("input.txt", part=2) == 2
