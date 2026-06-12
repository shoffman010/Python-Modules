#!/usr/bin/env python3

import sys


def data_transformer(file_name: str) -> None:
    f = None
    try:
        f = open(file_name, "r")
        content = f.read().replace("\n", "#\n")
    except OSError as e:
        print(f"Error opening file '{file_name}': {e}")
        return
    finally:
        if f is not None:
            f.close()

    if not content.endswith("\n"):
        content += "#\n"

    print("Transform data:")
    print("---")
    print(content, end="")
    print("---")

    new_name = input("Enter a new file name (or empty): ")
    if new_name == "":
        print("Not saving data.")
        return

    new_f = None
    try:
        new_f = open(new_name, "w")
        print(f"Saving data to '{new_name}'")
        new_f.write(content)
    except OSError as e:
        print(f"Error opening file '{new_name}': {e}")
        print("Data not saved.")
        return
    finally:
        if new_f is not None:
            new_f.close()

    print(f"Data saved in file '{new_name}'.")


def ft_archive_recovery(file_name: str) -> None:
    print(f"Accessing file '{file_name}'")
    try:
        f = open(file_name)
        print(
            "---\n",
            f"{f.read()}",
            "\n---",
            sep=''
            )
        f.close()
        print(f"File '{file_name}' closed.\n")
        data_transformer(file_name)
    except OSError as e:
        print(
            f"Error opening file '{file_name}': {e}"
        )


def main() -> None:
    if len(sys.argv) == 2:
        print("=== Cyber Archives Recovery & Preservation ===")
        ft_archive_recovery(sys.argv[1])
    else:
        print("Usage: ft_archive_creation.py <file>")


if __name__ == "__main__":
    main()
