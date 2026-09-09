from abc import ABC, abstractmethod

class TransformCapability(ABC):
    @abstractmethod
    def transform():
        pass

    @abstractmethod
    def revert():
        pass
