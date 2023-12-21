import pytest

from .solution import solve


def test_solves_part1():
    assert solve("demo_input.txt", part=1) == 32000000
    assert solve("example.txt", part=1) == 11687500
    assert solve("input.txt", part=1) == 1020211150


@pytest.mark.skip
def test_solves_part2():
    assert solve("demo_input.txt", part=2) == 1
    assert solve("input.txt", part=2) == 2
