from .file_parser import parse_input

card_strengths = {
    "2": 0,
    "3": 1,
    "4": 2,
    "5": 3,
    "6": 4,
    "7": 5,
    "8": 6,
    "9": 7,
    "T": 8,
    "J": -1,
    "Q": 10,
    "K": 11,
    "A": 12,
}


hand_type_strengths = {
    "high_card": 0,
    "one_pair": 10,
    "two_pairs": 20,
    "three_of_a_kind": 30,
    "full_house": 40,
    "four_of_a_kind": 50,
    "five_of_a_kind": 70,
}

all_cards = "".join(card_strengths.keys())
cards_excluding_jacks = all_cards.replace("J", "")


def find_all_possible_hands(hand):
    if hand == "":
        return [""]

    return [
        part1 + part2
        for part1 in (cards_excluding_jacks if hand[0] == "J" else hand[0])
        for part2 in find_all_possible_hands(hand[1:])
    ]


def get_hand_strength(hand):
    if "J" in hand:
        all_possible_hands = find_all_possible_hands(hand)
        return max([get_hand_strength(h) for h in all_possible_hands])

    hand_type = find_hand_type(hand)
    return hand_type_strengths[hand_type]


def sort_hand(hand):
    hand_strength = get_hand_strength(hand)
    return hand_strength, [card_strengths[c] for c in hand]


def find_hand_type(hand):
    card_freq = {}
    for c in hand:
        card_freq[c[0]] = card_freq.get(c[0], 0) + 1

    card_freq = {k: v for k, v in sorted(card_freq.items(), key=lambda item: item[1], reverse=True)}

    for card, frequency in card_freq.items():
        if frequency == 5:
            return "five_of_a_kind"
        if frequency == 4:
            return "four_of_a_kind"
        if frequency == 3:
            if len(card_freq) == 2:
                return "full_house"
            return "three_of_a_kind"
        if frequency == 2:
            if len(card_freq) == 3:
                return "two_pairs"
            return "one_pair"
        if frequency == 1 and len(card_freq) == 5:
            return "high_card"


def solve(file_name):
    inputs = parse_input(file_name)
    sorted_hands = sorted(inputs.keys(), key=lambda x: sort_hand(x))

    total_winnings = 0
    for i, hand in enumerate(sorted_hands):
        total_winnings += (i + 1) * inputs[hand]
    print(total_winnings)
    return total_winnings


if __name__ == "__main__":
    # possible_hands = find_all_possible_hands("JAJQ3")
    # print("dd", possible_hands)
    # print(len(possible_hands))
    # hands = replacements("JAJQ3")
    # print("dd", hands)
    # print(len(hands))
    assert solve("input.txt", part=1) == 250946742
