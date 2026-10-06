#!/usr/bin/env python3

def garden_operations(operation_number: int) -> None:
    match operation_number:
        case 0:
            int("abc")

        case 1:
            10 / 0

        case 2:
            open("/non/existent/file")

        case 3:
            "plant" + 42

        case _:
            print("Operation completed successfully")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")

    for operation in range(5):
        print(f"Testing operation {operation}...")

        try:
            garden_operations(operation)

        except ValueError as e:
            print(f"Caught ValueError: {e}")

        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")

        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")

        except TypeError as e:
            print(f"Caught TypeError: {e}")

    print("\nAll error types tested successfully!")


def main():
    test_error_types()


if __name__ == "__main__":
    main()
