import ast
import os


def read_input(file_name: str) -> list[str]:
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, "r") as f:
        return f.read().splitlines()


def _chunkify(arr, n):
    return [arr[i : i + n] for i in range(0, len(arr), n)]


def parse_input(file_name):
    inputs = [ast.literal_eval(line) for line in read_input(file_name) if line]
    return _chunkify(inputs, n=2)


if __name__ == "__main__":
    parse_input("demo_input.txt")
