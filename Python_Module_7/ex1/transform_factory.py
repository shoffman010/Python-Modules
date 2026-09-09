from ex0.creature_factory import CreatureFactory
from ex0.creature import Creature
from .transform import TransformCapability
class TransformCreatureFactory(CreatureFactory):
    def create_base():
        return (Shiftling())

    def create_evolved(self):
        if not isinstance(self, Creature):
            return TypeError
        return (Morphagon())

class Shiftling(Creature, TransformCapability):
    _type: str = "Normal type"
    _form: str = "normal"
    @property
    def attack(self) -> str:
        if self._form == "normal":
            return (f"{__class__.__name__} attacks normally.")
        return (f"{__class__.__name__} performs a boosted strike!")

    def transform(self) -> str:
        if self._form == "normal":
            self._form = "sharp"
            return (f"{__class__.__name__} shifts into a sharper form!")
        return (f"{__class__.__name__} is transformed already")

    def revert(self) -> str:
        if self._form == "sharp":
            self._form = "normal"
            return (f"{__class__.__name__} returns to normal.")
        return (f"{__class__.__name__} is in it's default form already!")


class Morphagon(Creature, TransformCapability):
    _type: str = "Normal/Dragon type"
    _form: str = "normal"

    @property
    def attack(self) -> str:
        if self._form == "normal":
            return (f"{__class__.__name__} attacks normally.")
        return (f"{__class__.__name__} unleashes a devastating morph strike!")

    def transform(self) -> str:
        if self._form == "normal":
            self._form = "dragonic"
            return (f"{__class__.__name__} morphs into a dragonic battle form!")
        return (f"{__class__.__name__} is transformed already")

    def revert(self) -> str:
        if self._form == "dragonic":
            self._form = "normal"
            return (f"{__class__.__name__} stabalizes its form.")
        return (f"{__class__.__name__} is in it's default form already!")