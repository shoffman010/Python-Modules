#!/usr/bin/env python3

def data_transformer(test_file: str) -> None:
    print(
        "Transform data:\n"
        "---\n"
        )
    f = open(test_file)
    transformer = ""
    line = f.readline()
    while line != "":
        transformer += line.strip("\n") + "#\n"
        line = f.readline()
    print(
        f"{transformer}"
        "\n---"
        )
    filename = input("Enter a new file name (or empty): ")
    if filename == "":
        print("Not saving data.")
        exit()
    else:
        print(
            f"Saving data to '{filename}'",
            ""
        )
        new_f = open(filename, "w")
    new_f.write(transformer)
    print(f"Data saved in '{filename}'.")


def ft_archive_recovery() -> None:
    test_file = 'ancient_fragment.txt'
    print(f"Accessing file '{test_file}'")
    try:
        f = open(test_file, "r")
        print(
            "---\n",
            f"{f.read()}",
            "\n---",
            sep=''
            )
        f.close()
        print(f"File '{test_file} closed.\n")
        data_transformer(test_file)
    except OSError as e:
        print(
            f"Error opening file '{test_file}': {e}"
        )


def main() -> None:
    print("=== Cyber Archives Recovery & Preservation ===")
    ft_archive_recovery()


if __name__ == "__main__":
    main()
