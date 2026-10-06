#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature(input) -> None:
    try:
        result = input_temperature(input)
        print(
            f"Input data is '{input}'\n"
            f"Temperatur is now {result}°C\n"
        )
    except ValueError as e:
        print(
            f"Input data is '{input}'\n"
            f"Caught input_temperature error: {e}\n"
        )


def main():
    print("=== Garden Temperature ===\n")
    test_temperature("25")
    test_temperature("abc")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
