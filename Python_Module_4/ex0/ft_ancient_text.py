#!/usr/bin/env python3

def ft_archive_recovery() -> None:
    test_file = 'ancient_fragment.txt'
    print(f"Accessing file '{test_file}'")
    try:
        reader = open(test_file, "r")
        print(
            "---\n",
            f"{reader.read()}",
            "\n---",
            sep=''
        )
        # breakpoint()
    except OSError as e:
        print(
            f"Error opening file '{test_file}': {e}"
        )
    except PermissionError as e:
        print(
            f"Error opening file '{test_file}': {e}"
        )


def main() -> None:
    print("=== Cyber Archives Recovery ===")
    ft_archive_recovery()


if __name__ == "__main__":
    main()
