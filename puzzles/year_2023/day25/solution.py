import os
from collections import defaultdict
import networkx as nx


def read_input(file_name: str) -> list[str]:
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, "r") as f:
        return f.read().splitlines()


def parse_input(file_name):
    inputs = read_input(file_name)
    graph = defaultdict(set)
    for line in inputs:
        node, neighbors = line.split(": ")
        neighbors = neighbors.split(" ")
        graph[node] = set(neighbors)
        for neighbor in neighbors:
            graph[neighbor].add(node)

    return graph


def get_connected_components(graph):
    nx_graph = nx.Graph(graph, capacity=1)
    edges_with_minimum_connectivity = nx.minimum_edge_cut(nx_graph)
    nx_graph.remove_edges_from(edges_with_minimum_connectivity)
    return list(nx.connected_components(nx_graph))


def solve_part1(graph):
    graph1, graph2 = get_connected_components(graph)
    return len(graph1) * len(graph2)


def solve_part2(inputs):
    pass


def solve(file_name, part=1):
    inputs = parse_input(file_name)
    if part == 1:
        return solve_part1(inputs)

    return solve_part2(inputs)


if __name__ == "__main__":
    solve("demo_input.txt", part=1)
    # solve("input.txt", part=1)
