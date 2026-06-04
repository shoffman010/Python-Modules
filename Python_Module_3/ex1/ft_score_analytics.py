#!/usr/bin/env python3

import sys


def check_input(argument: str, scores: list[int]) -> None:
    score = int(argument)
    scores.append(score)


def test_args() -> None:
    scores: list[int] = []

    print("=== Player Score Analytics ===")

    for argument in sys.argv[1:]:
        try:
            check_input(argument, scores)
        except ValueError:
            print(f"Invalid parameter: '{argument}'")

    if len(scores) == 0:
        print(
            "No scores provided. Usage: python3 "
            "ft_score_analytics.py <score1> <score2> ..."
        )
        return

    player_count = len(scores)
    total = sum(scores)
    high_score = max(scores)
    low_score = min(scores)
    score_range = high_score - low_score
    print(f"Scores processed: {scores}")
    print(f"Total players: {player_count}")
    print(f"Total score: {total}")
    print(f"Average score: {total / player_count}")
    print(f"High score: {high_score}")
    print(f"Low score: {low_score}")
    print(f"Score range: {score_range}")


def main() -> None:
    test_args()


if __name__ == "__main__":
    main()
