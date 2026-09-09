from ex0.creature_factory import CreatureFactory
from ex0.creature import Creature
from .heal import HealCapability


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> "Sproutling":
        return (Sproutling())

    def create_evolved(self) -> "Bloomelle":
        return (Bloomelle())


class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        self._type = "Grass type"

    def attack(self) -> str:
        return (f"{self.__class__.__name__} uses Vine Whip!")

    def heal(self, other: Creature | None = None) -> str:
        if other is None:
            return (
                f"{self.__class__.__name__} "
                "heals itself for a small amount"
            )
        return (f"{self.__class__.__name__} heals {other} for a small amount")


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        self._type = "Grass/Fairy type"

    def attack(self) -> str:
        return (f"{self.__class__.__name__} uses Petal Dance!")

    def heal(self) -> str:
        return (
            f"{self.__class__.__name__} "
            "heals itself and others for a large amount"
        )
