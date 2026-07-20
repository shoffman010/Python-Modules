import abc
from typing import Any

class DataProcessor(ABC):
    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass
    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass
    def output(self, ):
        pass
class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return isinstance(data, int)
class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return isinstance(data, str)
class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if not isinstance(data, dict):
            return False
        if len(data.keys()) is not 2:
            return False
        if "log_level" not in data:
            return False
        if "log_message" not in data:
            return False
        for value in data.values():
            if not isinstance(value, str):
                return False
        return True