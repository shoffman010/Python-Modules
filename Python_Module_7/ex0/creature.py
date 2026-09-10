from abc import ABC, abstractmethod


class Creature(ABC):
    _type: str = ""

    @abstractmethod
    def attack(self) -> str:
        raise NotImplementedError

    def describe(self) -> str:
        return (
            f"{self.__class__.__name__} is a "
            f"{self._type} Creature"
        )


class Flameling(Creature):
    def __init__(self) -> None:
        self._type = "Fire type"

    def attack(self) -> str:
        return ("Flameling uses Ember!")


class Pyrodon(Creature):
    def __init__(self) -> None:
        self._type = "Fire/Flying type"

    def attack(self) -> str:
        return ("Pyrodon uses Flamethrower!")


class Aquabub(Creature):
    def __init__(self) -> None:
        self._type = "Water type"

    def attack(self) -> str:
        return ("Aquabub uses Water Gun!")


class Torragon(Creature):
    def __init__(self) -> None:
        self._type = "Water type"

    def attack(self) -> str:
        return ("Torragon uses Hydro Pump!")
