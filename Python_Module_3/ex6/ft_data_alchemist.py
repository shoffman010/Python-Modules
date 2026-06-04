#!/usr/bin/env python3

import random


def main() -> None:
    print("=== Game Data Alchemist ===\n")

    initial_list = [
        "Alice",
        "bob",
        "Charlie",
        "dylan",
        "Emma",
        "Gregory",
        "john",
        "kevin",
        "Liam"
                ]
    print(f"Initial list of players: {initial_list}")

    new_list = [name.capitalize() for name in initial_list]
    print(f"New list with all names capitalized: {new_list}")

    capped = [name for name in initial_list if name == name.capitalize()]
    print(f"New list of capitalized names only: {capped}\n")

    score_dict: dict[str, int] = {
        name: random.randint(0, 1000) for name in new_list
    }
    print(f"Score dict: {score_dict}")

    score_average = round(sum(score_dict.values()) / len(score_dict), 2)
    print(f"Score average is {score_average}")

    high_score = {
        name: score for name, score in score_dict.items()
        if score > score_average
        }
    print(f"High scores: {high_score}")


if __name__ == "__main__":
    main()
