#!/usr/bin/env python3

def secure_archive(
        filename: str,
        action: str = "r",
        content: str = ""
    ) -> tuple:
    try:
        f = open(filename, action)
    except PermissionError as e:
        print(f"Using '{filename}' to read from an inaccessible file:")
        return (False, e)
    except OSError as e:
        print(f"Using '{filename}' to read from a nonexistent file:")
        return(False, e)

    with f:
        if action == "r":
            text = ""
            content = f.readline()
            while content != "":
                text += content.strip("\n") + "\n"
                content = f.readline()
            return (True, text)
        elif action == "w":
            print(f"\nUsing '{filename}' to write previous content to a new file:")
            with open(filename, "w") as f_new:
                f_new.write(content)
                return (True, "Content succesfully written to file")
            

def main() -> None:
    print("=== Cyber Archives Security ===\n\n")
    operation = secure_archive(
        "ancient_fragment.txt",
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