import os


def read_input(file_name: str) -> str:
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, "r") as f:
        return f.read()


def find_start_of_unique_stream_marker(datastream_buffer: str, unique_stream_size: int) -> int:
    low_pointer = 0
    high_pointer = unique_stream_size

    while high_pointer < len(datastream_buffer):
        marker = datastream_buffer[low_pointer:high_pointer]
        if len(set(marker)) == unique_stream_size:
            return high_pointer

        low_pointer += 1
        high_pointer += 1

    return -1


def solve(file_name: str, part: int = 1) -> int:
    inputs = read_input(file_name)
    return find_start_of_unique_stream_marker(inputs, unique_stream_size=part == 1 and 4 or 14)
