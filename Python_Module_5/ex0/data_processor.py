from abc import ABC
from abc import abstractmethod
from typing import Any

class DataProcessor(ABC):
    def __init__(self) -> None:
        self._data = list[tuple[int, str]] = []
        self._next_rank = 0
    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass
    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass
    def output(self):
        out = self._data.pop(0)
        print(f"{out}")
class NumericProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        return isinstance(data, int)

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        else:
            for item in data:
                self._data.append((self._next_rank, str(item)))
                self._next_rank += 1

class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return isinstance(data, str)
    def ingest(self, data: str | list[str]):
        if not self.validate(data):
            raise ValueError("Improper text data")
        else:
            for item in data:
                self._data.append((self._next_rank, str(item)))
                self._next_rank += 1

class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if not isinstance(data, dict):
            return False
        for item in data.items():
            if not isinstance(item, str):
                return False
        if "log_level" not in data:
            return False
        if "log_message" not in data:
            return False
        return True
    def ingest(self, data: dict(str, str) | list(dict)):
        if not self.validate(data):
            raise ValueError("Improper log data")
        else:
            

def main() -> None:
    num_proc = NumericProcessor()
    txt_proc = TextProcessor()
    log_proc = LogProcessor()
    print(f"{num_proc.validate(54)}")
    print(f"{txt_proc.validate("43")}")
    print(f"{log_proc.validate("log_level": "This is a test", "log_message": "This is a test")}")
    try:
        num_proc.ingest("54")
    except ValueError as e:
        print(f"{e}")
    try:
        txt_proc.ingest(54)
    except ValueError as e:
        print(f"{e}")
    try:
        log_proc.ingest("54")
    except ValueError as e:
        print(f"{e}")


if __name__ == "__main__":
    main()
