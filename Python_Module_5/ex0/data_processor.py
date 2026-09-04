from abc import ABC, abstractmethod
from typing import Any, TypeAlias


NumericData: TypeAlias = int | float | list[int | float]
TextData: TypeAlias = str | list[str]
LogEntry: TypeAlias = dict[str, str]
LogData: TypeAlias = LogEntry | list[LogEntry]


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._data: list[tuple[int, str]] = []
        self._next_rank: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        raise NotImplementedError

    @abstractmethod
    def ingest(self, data: Any) -> None:
        raise NotImplementedError

    def _store(self, values: list[str]) -> None:
        start = self._next_rank
        self._data.extend(
            (start + offset, value)
            for offset, value in enumerate(values)
        )
        self._next_rank += len(values)

    def output(self) -> tuple[int, str]:
        if not self._data:
            raise IndexError("No processed data available")
        return self._data.pop(0)


class NumericProcessor(DataProcessor):
    @staticmethod
    def _is_number(value: Any) -> bool:
        return (
            isinstance(value, (int, float))
            and not isinstance(value, bool)
        )

    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            return bool(data) and all(
                self._is_number(item) for item in data
            )
        return self._is_number(data)

    def ingest(self, data: NumericData) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")

        items = data if isinstance(data, list) else [data]
        self._store([str(item) for item in items])


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            return bool(data) and all(
                isinstance(item, str) for item in data
            )
        return isinstance(data, str)

    def ingest(self, data: TextData) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")

        items = data if isinstance(data, list) else [data]
        self._store(items)


class LogProcessor(DataProcessor):
    @staticmethod
    def _validate_entry(data: Any) -> bool:
        if not isinstance(data, dict):
            return False

        required_keys = {"log_level", "log_message"}
        return (
            required_keys.issubset(data)
            and all(
                isinstance(key, str) and isinstance(value, str)
                for key, value in data.items()
            )
        )

    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            return bool(data) and all(
                self._validate_entry(entry) for entry in data
            )
        return self._validate_entry(data)

    def ingest(self, data: LogData) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")

        entries = data if isinstance(data, list) else [data]
        formatted = [
            f'{entry["log_level"]}: {entry["log_message"]}'
            for entry in entries
        ]
        self._store(formatted)


def main() -> None:
    print("=== Code Nexus - Data Processor ===\n")

    num_proc = NumericProcessor()
    print("Testing Numeric Processor...")
    print(f"Trying to validate input '42': {num_proc.validate(42)}")
    print(
        "Trying to validate input 'Hello': "
        f"{num_proc.validate('Hello')}"
    )
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        num_proc.ingest("foo")
    except ValueError as error:
        print(f"Got exception: {error}")

    numeric_data: list[int | float] = [1, 2, 3, 4, 5]
    print(f"Processing data: {numeric_data}")
    num_proc.ingest(numeric_data)
    print("Extracting 3 values...")
    for _ in range(3):
        rank, value = num_proc.output()
        print(f"Numeric value {rank}: {value}")

    text_proc = TextProcessor()
    print("\nTesting Text Processor...")
    print(f"Trying to validate input '42': {text_proc.validate(42)}")
    text_data = ["Hello", "Nexus", "World"]
    print(f"Processing data: {text_data}")
    text_proc.ingest(text_data)
    print("Extracting 1 value...")
    rank, value = text_proc.output()
    print(f"Text value {rank}: {value}")

    log_proc = LogProcessor()
    print("\nTesting Log Processor...")
    print(
        "Trying to validate input 'Hello': "
        f"{log_proc.validate('Hello')}"
    )
    log_data: list[LogEntry] = [
        {
            "log_level": "NOTICE",
            "log_message": "Connection to server",
        },
        {
            "log_level": "ERROR",
            "log_message": "Unauthorized access!!",
        },
    ]
    print(f"Processing data: {log_data}")
    log_proc.ingest(log_data)
    print("Extracting 2 values...")
    for _ in range(2):
        rank, value = log_proc.output()
        print(f"Log entry {rank}: {value}")


if __name__ == "__main__":
    main()
