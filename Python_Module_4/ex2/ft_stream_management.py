#!/usr/bin/env python3

import sys


def data_transformer(text_file: str) -> None:
    f = open(text_file)
    transformed_data = ""
    line = f.readline()
    while line != "":
        transformed_data += line.strip("\n") + "#\n"
        line = f.readline()
    print(
        "---\n\n"
        f"{transformed_data}"
        "\n\n---"
        )
    print("Enter new file name (or empty): ", end="", flush=True)
    input = sys.stdin.readline().strip()
    print(f"Saving data to '{input}'")
    try:
        f_new = open(input, "w")
        if f_new == "":
            print(f"Not saving data")
            exit()
    except OSError as e:
        f_new.write(transformed_data)
        print(
        f"Data saved in file '{input}'"    
        )
    except PermissionError as e:
        print(
            f"[STDERR] Error opening file '{input}': {e}"
            "Data not saved."
            )
    finally:
        f_new.close()


def recovery_and_preservation():

    text = "ancient_fragment.txt"
    print(
        "=== Cyber Archives Recovery & Preservation ===\n"
        f"Accessing file '{text}"
    )
    try:
        f = open(text)
        print(
            "---\n\n"
            f"{f.read()}"
            "\n\n---"
            )
    except OSError as e:
        print(f"[STDERR] Error opening file {text}: {e}")
    except PermissionError as e:
        print(f"[STDERR] Error opening file '{text}': {e}", file=sys.stderr)
    else:
        f.close()
        print(f"File '{text}' closed.")
        data_transformer(text)


if __name__ == "__main__":
    recovery_and_preservation()