from day05.solution import solve


def test_solves_part1():
    assert solve("demo_input.txt", part=1) == "CMZ"
    assert solve("input.txt", part=1) == "BWNCQRMDB"


def test_solves_part2():
    assert solve("demo_input.txt", part=2) == "MCD"
    assert solve("input.txt", part=2) == "NHWZCBNBF"
