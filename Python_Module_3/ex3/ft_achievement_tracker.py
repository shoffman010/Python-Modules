#!/usr/bin/env python3

import random


ALL_ACHIEVEMENTS = [
    "First Steps",
    "Boss Slayer",
    "Treasure Hunter",
    "Master Explorer",
    "Crafting Genius",
    "World Savior",
    "Collector Supreme",
    "Untouchable",
    "Strategist",
    "Speed Runner",
    "Survivor",
    "Sharp Mind",
    "Unstoppable",
    "Hidden Path Finder",
]


def gen_player_achievements() -> set[str]:
    achievement_amount = random.randint(5, 9)
    picked_achievements = random.sample(ALL_ACHIEVEMENTS, achievement_amount)
    return set(picked_achievements)


def print_player_achievements(
    player_name: str,
    achievements: set[str],
) -> None:
    print(f"Player {player_name}: {achievements}")


def print_unique_player_achievements(
    player_name: str,
    player_achievements: set[str],
    other_achievements: set[str],
) -> None:
    unique_achievements = player_achievements.difference(other_achievements)
    print(f"Only {player_name} has: {unique_achievements}")


def print_missing_achievements(
    player_name: str,
    complete_achievement_set: set[str],
    player_achievements: set[str],
) -> None:
    missing_achievements = complete_achievement_set.difference(
        player_achievements
    )
    print(f"{player_name} is missing: {missing_achievements}")


def main() -> None:
    print("=== Achievement Tracker System ===\n")

    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()

    print_player_achievements("Alice", alice)
    print()
    print_player_achievements("Bob", bob)
    print()
    print_player_achievements("Charlie", charlie)
    print()
    print_player_achievements("Dylan", dylan)
    print()

    all_distinct_achievements = alice.union(bob, charlie, dylan)
    common_achievements = alice.intersection(bob, charlie, dylan)

    print(f"All distinct achievements: {all_distinct_achievements}\n")
    print(f"Common achievements: {common_achievements}\n")

    bob_charlie_dylan = bob.union(charlie, dylan)
    alice_charlie_dylan = alice.union(charlie, dylan)
    alice_bob_dylan = alice.union(bob, dylan)
    alice_bob_charlie = alice.union(bob, charlie)

    print_unique_player_achievements("Alice", alice, bob_charlie_dylan)
    print_unique_player_achievements("Bob", bob, alice_charlie_dylan)
    print_unique_player_achievements("Charlie", charlie, alice_bob_dylan)
    print_unique_player_achievements("Dylan", dylan, alice_bob_charlie)
    print()

    complete_achievement_set = set(ALL_ACHIEVEMENTS)

    print_missing_achievements("Alice", complete_achievement_set, alice)
    print_missing_achievements("Bob", complete_achievement_set, bob)
    print_missing_achievements("Charlie", complete_achievement_set, charlie)
    print_missing_achievements("Dylan", complete_achievement_set, dylan)


if __name__ == "__main__":
    main()