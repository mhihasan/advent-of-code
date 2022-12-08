import os


def read_input(file_name: str) -> list[str]:
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, "r") as f:
        return f.read().splitlines()


def parse_grid(lines):
    grid = []
    for i, line in enumerate(lines):
        vals = []
        for j, v in enumerate(line):
            vals.append(int(v))

        grid.append(vals)
    return grid
