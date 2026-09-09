from abc import ABC, abstractmethod
from ex0.creature import Creature


class HealCapability(ABC):
    @abstractmethod
    def heal() -> str:
        pass
