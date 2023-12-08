import os


def read_input(file_name: str) -> list[str]:
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, "r") as f:
        return f.read().splitlines()


def parse_input(file_name):
    inputs = read_input(file_name)
    card_bids = {}
    for line in inputs:
        card, bid = line.split(" ")
        card_bids[card] = int(bid)
    return card_bids
