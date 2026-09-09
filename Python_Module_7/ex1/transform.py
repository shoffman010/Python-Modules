from abc import ABC, abstractmethod


class TransformCapability(ABC):
    @abstractmethod
    def transform(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def revert(self) -> str:
        raise NotImplementedError
