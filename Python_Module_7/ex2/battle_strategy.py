from abc import ABC, abstractmethod
from ex0.creature import Creature
from ex0.creature_factory import Flameling, Aquabub
from ex1.transform_factory import Shiftling, Morphagon
from ex1.healing_factory import Sproutling, Bloomelle


class StrategyError(Exception):
    def __init__(self, creature: Creature):
        message = (
        "Battle error, aborting tournament: " \
        f"Invalid Creature '{creature.__class__.__name__}'"
        f"for this {self.__class__.__name__} strategy"
        )
        super().__init__(message)

class BattleStrategy(ABC):
    @abstractmethod
    def act():
        raise NotImplementedError

    @abstractmethod
    def is_valid() -> bool:
        raise NotImplementedError


class NormalStrategy(BattleStrategy):
    def act(self: Flameling | Aquabub):
        if not isinstance(self, Flameling | Aquabub):
            raise StrategyError
        self.attack


class DefensiveStrategy(BattleStrategy):
    def act(self: Sproutling | Bloomelle):
        if not isinstance(self, Sproutling | Bloomelle):
            raise StrategyError
        self.attack
        if self is Sproutling:
            self.heal()
        if self is Bloomelle:
            self.heal


class AggressiveStrategy(BattleStrategy):
    def act(self: Shiftling | Morphagon):
        if not isinstance(self, Shiftling | Morphagon):
            raise StrategyError
        print(self.transform())
        print(self.attack)
