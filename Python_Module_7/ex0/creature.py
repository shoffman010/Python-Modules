from abc import ABC, abstractmethod


class Creature(ABC):


    @abstractmethod
    def attack(self) -> str:
        """""Abstract method to enforce attack as a method needed to be provided
        by the classes inheriting from Creature"""
        raise NotImplementedError

    def describe(self) -> str:
        """Printing the description of the creature using inheritance"""
        if self is Creature:
            raise ValueError
        return (f"{self.__class__.__name__} is a {self._type} {__class__.__name__}")


class Flameling(Creature):

    _type = "Fire type"

    @property
    def attack(self) -> str:
        return ("Flameling uses Ember!")


class Pyrodon(Creature):
    """Evolved from Flameling"""

    _type = "Fire type"

    @property
    def attack(self):
        return ("Pyrodon uses Flamethrower!")


class Aquabub(Creature):

    _type = "Water type"

    @property
    def attack(self):
        return ("Aquabub uses Water Gun!")


class Torragon(Creature):
    """Evolved from Aquabub"""

    _type = "Water type"

    @property
    def attack(self):
            return ("Torragon uses Hydro Pump!")