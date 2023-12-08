import math
import os


def read_input(file_name: str) -> list[str]:
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, "r") as f:
        return f.read().splitlines()


def parse_input(file_name):
    inputs = read_input(file_name)
    instructions = inputs[0]
    nodes = {}
    for line in inputs[2:]:
        current, next_node = line.split(" = ")
        left, right = next_node.split(", ")
        left = left[1:]
        right = right[:-1]
        nodes[current] = {"L": left, "R": right}

    return {
        "instructions": instructions,
        "nodes": nodes,
    }


def get_next_node(node, instruction):
    if instruction == "L":
        return node[0]
    elif instruction == "R":
        return node[1]
    else:
        raise Exception(f"Unknown instruction: {instruction}")


def solve_part1(inputs):
    instructions = inputs["instructions"]

    end_node = "ZZZ"
    current_node = "AAA"
    steps = 0
    while current_node != end_node:
        for i, instruction in enumerate(instructions):
            current_node = inputs["nodes"][current_node][instruction]

            steps += 1
            if current_node == end_node:
                break

    return steps


def solve_part2(inputs):
    instructions = inputs["instructions"]

    current_nodes = {node for node in inputs["nodes"].keys() if node.endswith("A")}
    end_nodes = {node for node in inputs["nodes"].keys() if node.endswith("Z")}
    steps = {node: 0 for node in current_nodes}

    for node in current_nodes:
        current_node = node
        while current_node not in end_nodes:
            for i, instruction in enumerate(instructions):
                current_node = inputs["nodes"][current_node][instruction]
                steps[node] += 1
                if current_node in end_nodes:
                    break

    return math.lcm(*steps.values())


def solve(file_name, part=1):
    inputs = parse_input(file_name)
    if part == 1:
        return solve_part1(inputs)

    return solve_part2(inputs)


if __name__ == "__main__":
    solve("input.txt", part=1)
