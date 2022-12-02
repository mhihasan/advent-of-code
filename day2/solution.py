import argparse


def read_input(file_name):
    with open(file_name, "r") as f:
        return f.read().splitlines()


SCORES = {"X": 1, "Y": 2, "Z": 3, "A": 1, "B": 2, "C": 3}

WINNING_CONDITIONS_OPP_TO_PLAYER = {"C": "X", "B": "Z", "A": "Y"}

LOSING_CONDITIONS_OPP_TO_PLAYER = {"A": "Z", "B": "X", "C": "Y"}

WINNING_SCORE = 6
DRAW_SCORE = 3
LOSE_SCORE = 0


def calculate_part1_score(rounds: list[str]) -> int:
    outcome_score = 0
    selection_score = 0

    for r in rounds:
        opponent_turn, player_turn = r.split(" ")
        opponent_score = SCORES[opponent_turn]
        player_score = SCORES[player_turn]
        turn_required_to_win = WINNING_CONDITIONS_OPP_TO_PLAYER[opponent_turn]

        if turn_required_to_win == player_turn:
            outcome_score += WINNING_SCORE
        elif opponent_score == player_score:
            outcome_score += DRAW_SCORE

        selection_score += SCORES[player_turn]

    return outcome_score + selection_score


def calculate_part2_score(rounds: list[str]) -> int:
    outcome_score = 0
    selection_score = 0
    for r in rounds:
        opponent_turn, player_turn = r.split(" ")

        if player_turn == "Y":
            selection_score += SCORES[opponent_turn]
            outcome_score += DRAW_SCORE

        elif player_turn == "Z":
            turn_required_to_win = WINNING_CONDITIONS_OPP_TO_PLAYER[opponent_turn]
            selection_score += SCORES[turn_required_to_win]
            outcome_score += WINNING_SCORE
        else:
            turn_required_to_lose = LOSING_CONDITIONS_OPP_TO_PLAYER[opponent_turn]
            selection_score += SCORES[turn_required_to_lose]

    return selection_score + outcome_score


def solve_part1(file_name: str) -> int:
    rounds = read_input(file_name)
    score = calculate_part1_score(rounds)
    return score


def solve_part2(file_name: str) -> int:
    rounds = read_input(file_name)
    score = calculate_part2_score(rounds)
    return score


def solve(file_name: str, part: int = 1) -> int:
    if part == 1:
        return solve_part1(file_name)
    else:
        return solve_part2(file_name)


def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", default="input.txt")
    parser.add_argument("--part", default=1, type=int)

    args = parser.parse_args()

    solve(file_name=args.file, part=args.part)


if __name__ == "__main__":
    cli()
