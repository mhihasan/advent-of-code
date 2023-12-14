import os


def read_input(file_name: str) -> list[str]:
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, "r") as f:
        return f.read().splitlines()


def parse_input(file_name):
    inputs = read_input(file_name)
    return inputs


def fn(line):
    """
    ('O', 'O', '.', 'O', '.', 'O', '.', '.', '#', '#')
    ('.', '.', '.', 'O', 'O', '.', '.', '.', '.', 'O')
    ('.', 'O', '.', '.', '.', '#', 'O', '.', '.', 'O')
    ('.', 'O', '.', '#', '.', '.', '.', '.', '.', '.')
    ('.', '#', '.', 'O', '.', '.', '.', '.', '.', '.')
    ('#', '.', '#', '.', '.', 'O', '#', '.', '#', '#')
    ('.', '.', '#', '.', '.', '.', 'O', '.', '#', '.')
    ('.', '.', '.', '.', 'O', '#', '.', 'O', '#', '.')
    ('.', '.', '.', '.', '#', '.', '.', '.', '.', '.')
    ('.', '#', '.', 'O', '.', '#', 'O', '.', '.', '.')


     ('.', 'O', '.', '.', '.', '#', 'O', '.', '.', 'O')
     ('.', '#', '.', 'O', '.', '#', 'O', '.', '.', '.')
    """

    for i, c in enumerate(line):
        if c == "O":
            j = i
            while j > 0:
                if line[j - 1] != ".":
                    break

                line[j - 1] = "O"
                line[j] = "."

                j -= 1

    total = 0
    length = len(line)
    for i, c in enumerate(line):
        if c == "O":
            total += length - i
    return total


def solve_part1(inputs):
    sm = 0
    transposed = list(zip(*inputs))
    for line in transposed:
        print(line)
        n = fn(list(line))
        sm += n
        print(n)
    print("total", sm)
    return sm


def solve_part2(inputs):
    pass


def solve(file_name, part=1):
    inputs = parse_input(file_name)
    if part == 1:
        return solve_part1(inputs)

    return solve_part2(inputs)


if __name__ == "__main__":
    # fn(['.', '#', '.', 'O', '.', '#', 'O', '.', '.', '.'])
    solve("input.txt", part=1)
