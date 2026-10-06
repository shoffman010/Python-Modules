#!/usr/bin/env python3

def secure_archive(
        filename: str,
        action: str = "r",
        content: str = ""
        ) -> tuple[bool, str]:
    if action not in ("r", "w"):
        return (False, f"Invalid mode '{action}'")

    try:
        with open(filename, action) as f:
            if action == "r":
                return (True, f.read())

            else:
                f.write(content)
                return (True, "Content successfully written to file")

    except OSError as e:
        return (False, str(e))


def main() -> None:
    print("=== Cyber Archives Security ===\n")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file", "r"))

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd", "r"))

    print("\nUsing 'secure_archive' to read from a regular file:")
    operation = secure_archive("ancient_fragment.txt", "r")
    print(operation)

    if operation[0]:
        print(
            "\nUsing 'secure_archive' to write previous content to a new file:"
        )
        print(secure_archive("new.txt", "w", operation[1]))


if __name__ == "__main__":
    main()
