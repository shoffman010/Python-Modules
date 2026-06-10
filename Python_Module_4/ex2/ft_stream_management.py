#!/usr/bin/env python3

import sys


def data_transformer(text_file: str) -> None:
    f = open(text_file)
    transformed_data = ""
    line = f.readline()

    while line != "":
        transformed_data += line.strip("\n") + "#\n"
        line = f.readline()
    
    f.close()

    print(
        "---\n"
        f"{transformed_data}"
        "\n---"
        )
    
    print("Enter new file name (or empty): ", end="", flush=True)
    input = sys.stdin.readline().strip()

    if input == "":
        print("Not saving data.")
        return
    
    print(f"Saving data to '{input}'")

    f_new = None
    try:
        f_new = open(input, "w")
    except OSError as e:
        print(f"[STDERR] Error opening file '{input}': {e}",
              file=sys.stderr)
        print("Data not saved.")
    else:
        f_new.write(transformed_data)
        print(f"Data saved in file '{input}'")
    finally:
        if f_new is not None:
            f_new.close()


def recovery_and_preservation():

    text = "ancient_fragment.txt"
    print(
        "=== Cyber Archives Recovery & Preservation ===\n"
        f"Accessing file '{text}'"
    )
    try:
        f = open(text)
        print(
            "---\n"
            f"{f.read()}"
            "\n---"
            )

    except OSError as e:
        print(f"[STDERR] Error opening file '{text}': {e}", file=sys.stderr)
     
    else:
        f.close()
        print(f"File '{text}' closed.")
        data_transformer(text)


if __name__ == "__main__":
    recovery_and_preservation()