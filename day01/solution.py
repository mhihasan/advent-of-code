import os


def read_input(file_name: str) -> list[str]:
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, "r") as f:
        return f.read().splitlines()


def _sum_of_digits(line):
    digits = [int(c) for c in line if c.isdigit()]
    number = digits[0] * 10 + digits[-1]
    return number


def does_contain_substring_next(line, substring, current_index):
    matches = {
        "start_index": None,
        "end_index": None,
    }
    if line.startswith(substring):
        matches["start_index"] = current_index
    if line.endswith(substring):
        matches["end_index"] = current_index
        return matches


def _convert_letter_to_digit(line):
    digits_str_to_number_dict = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    i = 0
    while i < len(line):
        if line[i].isdigit():
            i += 1
            continue

        if line[i].isalpha():
            word = ""
            while i < len(line) and line[i].isalpha():
                word += line[i]
                i += 1

            if word in digits_str_to_number_dict:
                line = line.replace(word, digits_str_to_number_dict[word])
            continue

        i += 1

    digit_indices = {}
    for word, number in digits_str_to_number_dict.items():
        try:
            digit_indices[word] = line.index(word)
        except ValueError:
            pass

    if digit_indices:
        sorted_digits = sorted(digit_indices.items(), key=lambda x: x[1])
        for digit in [sorted_digits[0], sorted_digits[-1]]:
            if digit[1] + len(digit[0]) > len(line):
                continue

            line = line.replace(digit[0], digits_str_to_number_dict[digit[0]])
    return line


def find_all(a_str, sub):
    indices = []
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1:
            return indices

        indices.append(start)
        start += len(sub)


def solve_part1(inputs):
    total = 0
    for line in inputs:
        total += _sum_of_digits(line)
    print(total)


def solve_part2(inputs):
    digits_str_to_number_dict = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    total = 0
    for line in inputs:
        # replace all digits with their number
        digit_indices = []
        for word, number in digits_str_to_number_dict.items():
            try:
                indices = find_all(line, word)
                print("indices", indices)
                if len(indices) > 1:
                    raise ValueError

                for index in indices:
                    digit_indices.append((word, index))
            except ValueError:
                pass

        modified_line = line

        if digit_indices:
            sorted_digits = sorted(digit_indices, key=lambda x: x[1])
            # modified_line.replace(sorted_digits[0][0], digits_str_to_number_dict[sorted_digits[0][0]])
            # modified_line.replace(sorted_digits[-1][0], digits_str_to_number_dict[sorted_digits[-1][0]])
            for digit in [sorted_digits[0], sorted_digits[-1]]:
                modified_line = modified_line.replace(digit[0], digits_str_to_number_dict[digit[0]])

        line_total = _sum_of_digits(modified_line)
        print(f"{line} --> {modified_line} --> {line_total}")

        total += line_total
    print(total)


def solve(file_name, part=1):
    inputs = read_input(file_name)
    if part == 1:
        return solve_part1(inputs)

    return solve_part_2_v(inputs)


def find_calibration_value(line):
    digits_str_to_number_dict = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    i = 0
    first_digit = None
    while i < len(line):
        if line[i].isdigit():
            first_digit = int(line[i])
            break

        if line[i].isalpha():
            for word, number in digits_str_to_number_dict.items():
                if line[i:].startswith(word):
                    first_digit = int(number)
                    break

        if first_digit:
            break

        i += 1

    second_digit = None
    j = len(line) - 1
    while j > i:
        if line[j].isdigit():
            second_digit = int(line[j])
            break

        if line[j].isalpha():
            for word, number in digits_str_to_number_dict.items():
                if line[: j + 1].endswith(word):
                    second_digit = int(number)
                    break
        if second_digit:
            break

        j -= 1

    number = first_digit * 10 + (second_digit or first_digit)
    print(f"{line} --> {number}")
    return number


def solve_part_2_v(inputs):
    total = 0
    for line in inputs:
        total += find_calibration_value(line)
    print(total)


if __name__ == "__main__":
    solve("input.txt", part=2)
    # solve("demo_input.txt", part=2)
    # indices = find_calibration_value("twonetwoonetwo")
    # print(indices)
