from ex0.creature_factory import CreatureFactory
from ex0.creature import Creature
from .transform import TransformCapability


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> "Shiftling":
        return (Shiftling())

    def create_evolved(self) -> "Morphagon":
        return (Morphagon())


class Shiftling(Creature, TransformCapability):
    _form: str

    def __init__(self) -> None:
        self._type = "Normal type"
        self._form: str = "normal"

    def attack(self) -> str:
        if self._form == "normal":
            return (f"{self.__class__.__name__} attacks normally.")
        return (f"{self.__class__.__name__} performs a boosted strike!")

    def transform(self) -> str:
        if self._form == "normal":
            self._form = "sharp"
            return (f"{self.__class__.__name__} shifts into a sharper form!")
        return (f"{self.__class__.__name__} is transformed already")

    def revert(self) -> str:
        if self._form == "sharp":
            self._form = "normal"
            return (f"{self.__class__.__name__} returns to normal.")
        return (f"{self.__class__.__name__} is in it's default form already!")


class Morphagon(Creature, TransformCapability):
    _form: str

    def __init__(self) -> None:
        self._type = "Normal/Dragon type"
        self._form: str = "normal"

    def attack(self) -> str:
        if self._form == "normal":
            return (f"{self.__class__.__name__} attacks normally.")
        return (
            f"{self.__class__.__name__} "
            "unleashes a devastating morph strike!"
        )

    def transform(self) -> str:
        if self._form == "normal":
            self._form = "dragonic"
            return (
                f"{self.__class__.__name__} "
                "morphs into a dragonic battle form!"
            )
        return (f"{self.__class__.__name__} is transformed already")

    def revert(self) -> str:
        if self._form == "dragonic":
            self._form = "normal"
            return (f"{self.__class__.__name__} stabilizes its form.")
        return (f"{self.__class__.__name__} is in it's default form already!")
