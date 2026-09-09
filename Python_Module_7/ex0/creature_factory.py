from abc import ABC, abstractmethod
from .creature import Creature, Flameling, Pyrodon, Aquabub, Torragon

class CreatureFactory(ABC):
      @abstractmethod
      def create_base():
            raise NotImplementedError

      @abstractmethod
      def create_evolved():
            raise NotImplementedError


class FlameFactory(CreatureFactory):
      def create_base():
            return (Flameling())

      def create_evolved(self: Creature):
            if not isinstance(self, Flameling):
                  raise ValueError
            return (Pyrodon())


class AquaFactory(CreatureFactory):
        def create_base():
              return (Aquabub())

        def create_evolved(self: Creature):
              if not isinstance(self, Aquabub):
                    raise ValueError
              return (Torragon())