#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    result = int(temp_str)

    if result < 0:
        raise ValueError(f"{result}°C is too cold for plants (min 0°C)")
    if result > 40:
        raise ValueError(f"{result}°C is too hot for plants (max 40°C)")

    return result


def run_temperature_test(temp_str: str) -> None:
    print(f"Input data is '{temp_str}'")

    try:
        result = input_temperature(temp_str)
        print(f"Temperature is now {result}°C\n")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}\n")


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===\n")

    run_temperature_test("25")
    run_temperature_test("abc")
    run_temperature_test("100")
    run_temperature_test("-50")

    print("All tests completed - program didn't crash!")


def main() -> None:
    test_temperature()


if __name__ == "__main__":
    main()
    