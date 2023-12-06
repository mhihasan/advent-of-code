import os


def read_input(file_name: str) -> list[str]:
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, "r") as f:
        return f.read().splitlines()


def parse_input(file_name):
    inputs = read_input(file_name)
    times = [i for i in inputs[0].split(": ")[1].strip().split(" ") if i]
    distances = [i for i in inputs[1].split(": ")[1].strip().split(" ") if i]
    return [(int(t), int(d)) for t, d in zip(times, distances)]
