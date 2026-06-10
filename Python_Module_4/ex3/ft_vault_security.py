#!/usr/bin/env python3

def secure_archive(
        filename: str,
        action: str = "r",
        content: str = ""
    ) -> tuple:
    try:
        f = open(filename, action)
    except PermissionError as e:
        print(f"Using '{secure_archive.__name__}' to read from an inaccessible file:")
        return (False, str(e))
    except OSError as e:
        print(f"Using '{secure_archive.__name__}' to read from a nonexistent file:")
        return(False, str(e))

    with f:
        if action == "r":
            print(f"Using '{secure_archive.__name__}' to read from a regular file:")
            text = ""
            content = f.readline()
            while content != "":
                text += content.strip("\n") + "\n"
                content = f.readline()
            return (True, text)
        elif action == "w":
            print(f"\nUsing '{secure_archive.__name__}' to write to a new file:")
            with open(filename, "w") as f_new:
                f_new.write(content)
                return (True, "Content succesfully written to file")
            

def main() -> None:
    filename = "ancient_fragment.txt"
    print("=== Cyber Archives Security ===\n")
    operation = secure_archive(
        filename,
        "r",
        ""
        )
    print(operation)
    if operation[0] == True:
        file_content = str(operation[1])
        operation = secure_archive(
            "new.txt",
            "w",
            file_content
        )
        print(operation)


if __name__ == "__main__":
    main()