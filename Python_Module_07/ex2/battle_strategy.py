from abc import ABC, abstractmethod

from ex0.creature import Creature
from ex1.heal import HealCapability
from ex1.transform import TransformCapability


class StrategyError(Exception):

    def __init__(self, creature: Creature, strategy_name: str) -> None:
        message = (
                "Battle error, aborting tournament: "
                f"Invalid Creature '{creature.__class__.__name__}'"
                f"for this {self.__class__.__name__} strategy"
        )
        super().__init__(message)


class BattleStrategy(ABC):

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        raise NotImplementedError

    @abstractmethod
    def act(self, creature: Creature) -> None:
        raise NotImplementedError


class NormalStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, Creature):
            return True
        return False

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise StrategyError(creature, "normal")
        print(creature.attack())


class DefensiveStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        if not isinstance(creature, HealCapability):
            return False
        return True

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise StrategyError(creature, "defensive")
        assert isinstance(creature, HealCapability)
        print(creature.attack())
        print(creature.heal())


class AggressiveStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        if not isinstance(creature, TransformCapability):
            return False
        return True

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise StrategyError(creature, "aggressive")
        assert isinstance(creature, TransformCapability)
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())
