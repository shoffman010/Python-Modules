#!/usr/bin/env python3

import sys


def ft_archive_recovery(file_name: str) -> None:
    reader = None
    try:
        reader = open(file_name, "r")
        print("---\n\n", f"{reader.read()}", "\n\n---", sep="")
    except OSError as e:
        print(f"Error opening file '{file_name}': {e}")
    finally:
        if reader is not None:
            reader.close()
            print(f"File '{file_name}' closed.")


def main() -> None:
    if len(sys.argv) == 2:
        print("=== Cyber Archives Recovery ===")
        print(f"Accessing file '{sys.argv[1]}'")
        ft_archive_recovery(sys.argv[1])
    else:
        print("Usage: ft_ancient_text.py <file>")


if __name__ == "__main__":
    main()
