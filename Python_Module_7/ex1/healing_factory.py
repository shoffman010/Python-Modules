from ex0.creature_factory import CreatureFactory
from ex0.creature import Creature
from .heal import HealCapability

class HealingCreatureFactory(CreatureFactory):

    def create_base():
        return (Sproutling())

    def create_evolved(self):
        if not isinstance(self, Creature):
            raise TypeError
        return (Bloomelle())


class Sproutling(Creature, HealCapability):

    _type = "Grass type"

    @property
    def attack(self) -> str:
        return (f"{__class__.__name__} uses Vine Whip!")

    def heal(self, other: Creature | None = None) -> str:
        if other is None:
            return (f"{__class__.__name__} heals itself for a small amount")
        return (f"{__class__.__name__} heals {other} for a small amount")


class Bloomelle(Creature, HealCapability):

    _type = "Grass/Fairy type"

    @property
    def attack(self) -> str:
        return (f"{__class__.__name__} uses Petal Dance!")

    @property
    def heal(self):
        return (f"{__class__.__name__} heals itself and others for a large amount")
    
