import pytest

from .solution import solve


def test_solves_part1():
    assert solve("demo_input.txt", part=1) == 5
    assert solve("input.txt", part=1) == 480


@pytest.mark.skip
def test_solves_part2():
    assert solve("demo_input.txt", part=2) == 1
    assert solve("input.txt", part=2) == 2
