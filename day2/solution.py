import argparse

OPPONENT_ROCK = "A"
OPPONENT_PAPER = "B"
OPPONENT_SCISSORS = "C"

PLAYER_ROCK = "X"
PLAYER_PAPER = "Y"
PLAYER_SCISSORS = "Z"

SCORES = {
    PLAYER_ROCK: 1,
    PLAYER_PAPER: 2,
    PLAYER_SCISSORS: 3,
    OPPONENT_ROCK: 1,
    OPPONENT_PAPER: 2,
    OPPONENT_SCISSORS: 3,
}

WINNING_CONDITIONS = {OPPONENT_SCISSORS: PLAYER_ROCK, OPPONENT_PAPER: PLAYER_SCISSORS, OPPONENT_ROCK: PLAYER_PAPER}

LOSING_CONDITIONS = {OPPONENT_ROCK: PLAYER_SCISSORS, OPPONENT_PAPER: PLAYER_ROCK, OPPONENT_SCISSORS: PLAYER_PAPER}

WINNING_SCORE = 6
DRAW_SCORE = 3
LOSE_SCORE = 0


def read_input(file_name: str) -> list[str]:
    with open(file_name, "r") as f:
        return f.read().splitlines()


def calculate_part1_score(rounds: list[str]) -> int:
    outcome_score = 0
    selection_score = 0

    for r in rounds:
        opponent_turn, player_turn = r.split(" ")
        opponent_score = SCORES[opponent_turn]
        player_score = SCORES[player_turn]
        turn_required_to_win = WINNING_CONDITIONS[opponent_turn]

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

        if player_turn == PLAYER_PAPER:
            selection_score += SCORES[opponent_turn]
            outcome_score += DRAW_SCORE
        elif player_turn == PLAYER_SCISSORS:
            turn_required_to_win = WINNING_CONDITIONS[opponent_turn]
            selection_score += SCORES[turn_required_to_win]
            outcome_score += WINNING_SCORE
        else:
            turn_required_to_lose = LOSING_CONDITIONS[opponent_turn]
            selection_score += SCORES[turn_required_to_lose]

    return selection_score + outcome_score


def solve(file_name: str, part: int = 1) -> int:
    moves = read_input(file_name)
    return part == 1 and calculate_part1_score(moves) or calculate_part2_score(moves)


def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", default="input.txt")
    parser.add_argument("--part", default=1, type=int)

    args = parser.parse_args()

    solve(file_name=args.file, part=args.part)


if __name__ == "__main__":
    cli()
