from abc import ABC, abstractmethod
from typing import Any, Protocol, TypeAlias


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

    @property
    def total_processed(self) -> int:
        return self._next_rank

    @property
    def remaining(self) -> int:
        return len(self._data)

    @property
    def processor_name(self) -> str:
        class_name = type(self).__name__
        return f"{class_name.removesuffix('Processor')} Processor"


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


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class CSVExportPlugin:
    @staticmethod
    def _escape(value: str) -> str:
        if any(character in value for character in ',"\r\n'):
            return f'"{value.replace(chr(34), chr(34) * 2)}"'
        return value

    def process_output(self, data: list[tuple[int, str]]) -> None:
        values = (self._escape(value) for _, value in data)
        print("CSV Output:")
        print(",".join(values))


class JSONExportPlugin:
    @staticmethod
    def _escape(value: str) -> str:
        escaped: list[str] = []
        replacements = {
            '"': '\\"',
            "\\": "\\\\",
            "\b": "\\b",
            "\f": "\\f",
            "\n": "\\n",
            "\r": "\\r",
            "\t": "\\t",
        }
        for character in value:
            if character in replacements:
                escaped.append(replacements[character])
            elif ord(character) < 0x20:
                escaped.append(f"\\u{ord(character):04x}")
            else:
                escaped.append(character)
        return "".join(escaped)

    def process_output(self, data: list[tuple[int, str]]) -> None:
        fields = (
            f'"item_{rank}": "{self._escape(value)}"'
            for rank, value in data
        )
        print("JSON Output:")
        print("{" + ", ".join(fields) + "}")


class DataStream:
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for element in stream:
            for processor in self._processors:
                if processor.validate(element):
                    processor.ingest(element)
                    break
            else:
                print(
                    "DataStream error - Can't process element in stream: "
                    f"{element}"
                )

    def output_pipeline(
        self,
        nb: int,
        plugin: ExportPlugin,
    ) -> None:
        if nb < 0:
            raise ValueError("Number of items must not be negative")

        for processor in self._processors:
            output = [
                processor.output()
                for _ in range(min(nb, processor.remaining))
            ]
            plugin.process_output(output)

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
            return

        for processor in self._processors:
            print(
                f"{processor.processor_name}: total "
                f"{processor.total_processed} items processed, remaining "
                f"{processor.remaining} on processor"
            )


def first_batch() -> list[Any]:
    return [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead",
            },
            {
                "log_level": "INFO",
                "log_message": "User wil is connected",
            },
        ],
        42,
        ["Hi", "five"],
    ]


def second_batch() -> list[Any]:
    return [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {
                "log_level": "ERROR",
                "log_message": "500 server crash",
            },
            {
                "log_level": "NOTICE",
                "log_message": "Certificate expires in 10 days",
            },
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello",
    ]


def main() -> None:
    print("=== Code Nexus - Data Pipeline ===\n")

    print("Initialize Data Stream...\n")
    data_stream = DataStream()
    data_stream.print_processors_stats()

    print("\nRegistering Processors\n")
    data_stream.register_processor(NumericProcessor())
    data_stream.register_processor(TextProcessor())
    data_stream.register_processor(LogProcessor())

    data_batch = first_batch()
    print(f"Send first batch of data on stream: {data_batch}\n")
    data_stream.process_stream(data_batch)
    data_stream.print_processors_stats()

    print(
        "\nSend 3 processed data from each processor to a CSV plugin:"
    )
    data_stream.output_pipeline(3, CSVExportPlugin())
    print()
    data_stream.print_processors_stats()

    data_batch = second_batch()
    print(f"\nSend another batch of data: {data_batch}\n")
    data_stream.process_stream(data_batch)
    data_stream.print_processors_stats()

    print(
        "\nSend 5 processed data from each processor to a JSON plugin:"
    )
    data_stream.output_pipeline(5, JSONExportPlugin())
    print()
    data_stream.print_processors_stats()


if __name__ == "__main__":
    main()
