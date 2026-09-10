from ex0 import FlameFactory, AquaFactory
from ex0.creature import Creature
from ex0.creature_factory import CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    BattleStrategy,
    NormalStrategy,
    DefensiveStrategy,
    AggressiveStrategy,
    StrategyError
)
from typing import TypeAlias

Opponent: TypeAlias = tuple[CreatureFactory, BattleStrategy]
PreparedOpponent: TypeAlias = tuple[Creature, BattleStrategy]


def battle(opponents: list[Opponent]) -> None:
    print(" *** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    prepared: list[PreparedOpponent] = []

    for factory, strategy in opponents:
        creature = factory.create_base()
        prepared.append((creature, strategy))

    try:
        for left_index in range(len(prepared)):
            for right_index in range(left_index + 1, len(prepared)):
                left_creature, left_strategy = prepared[left_index]
                right_creature, right_strategy = prepared[right_index]
            print("\n* Battle *")
            print(f"{left_creature.describe()}")
            print(" vs.")
            print(f"{right_creature.describe()}")
            print(" now fight!")

            left_strategy.act(left_creature)
            right_strategy.act(right_creature)

    except StrategyError as error:
        print(f" Battle error, aborting torunament: {error}")

def main() -> None:
    tournament_0: list[Opponent] = [
        (FlameFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
    ]

    print("Tournament 0 (basic)")
    print(" [ (Flameling+Normal), (Healing+Defensive) ]")
    battle(tournament_0)

    tournament_1: list[Opponent] = [
        (FlameFactory(), AggressiveStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
    ]

    print("\nTournament 1 (error)")
    print(" [ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle(tournament_1)

    tournament_2: list[Opponent] = [
        (AquaFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy()),
    ]

    print("\nTournament 2 (multiple)")
    print(
        " [ (Aquabub+Normal), (Healing+Defensive), "
        "(Transform+Aggressive) ]"
    )
    battle(tournament_2)


if __name__ == "__main__":
    main()