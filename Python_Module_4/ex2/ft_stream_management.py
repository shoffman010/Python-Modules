#!/usr/bin/env python3

import sys


def data_transformer(file_name: str) -> None:
    f = None
    try:
        f = open(file_name, "r")
        content = f.read().replace("\n", "#\n")
    except OSError as e:
        print(
            f"[STDERR] Error opening file '{file_name}': {e}",
            file=sys.stderr
        )
        return
    finally:
        if f is not None:
            f.close()

    if not content.endswith("\n"):
        content = content + "#\n"

    print(
        "Transform data:\n"
        "---\n\n"
        f"{content}"
        "\n---"
    )

    print("Enter new file name (or empty): ", end="", flush=True)
    new_file_name = sys.stdin.readline().strip()

    if new_file_name == "":
        print("Not saving data.")
        return

    print(f"Saving data to '{new_file_name}'")

    f_new = None
    try:
        f_new = open(new_file_name, "w")
        f_new.write(content)
    except OSError as e:
        print(
            f"[STDERR] Error opening file '{new_file_name}': {e}",
            file=sys.stderr
        )
        print("Data not saved.")
    else:
        print(f"Data saved in file '{new_file_name}'")
    finally:
        if f_new is not None:
            f_new.close()


def main() -> None:
    if len(sys.argv) == 2:
        print(
            "=== Cyber Archives Recovery & Preservation ===\n"
            f"Accessing file '{sys.argv[1]}'"
        )

        f = None
        opened = False

        try:
            f = open(sys.argv[1], "r")
            opened = True
            print(
                "---\n\n"
                f"{f.read()}"
                "\n\n---"
            )
        except OSError as e:
            print(
                f"[STDERR] Error opening file '{sys.argv[1]}': {e}",
                file=sys.stderr
            )
        finally:
            if f is not None:
                f.close()
                print(f"File '{sys.argv[1]}' closed.\n")

        if opened:
            data_transformer(sys.argv[1])
    else:
        print("Usage: ft_stream_management.py <file>")


if __name__ == "__main__":
    main()