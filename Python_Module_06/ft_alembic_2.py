import alchemy.elements


def main() -> None:
    print("=== Alembic 2 ===")
    print("Accessing alchemy/elements.py using 'import ...' structure")
    print("Testing create_earth: ", end="")

    Test = alchemy.elements.create_earth()

    if Test != "Earth element created":
        print("Failed")
        return

    print(Test)


if __name__ == "__main__":
    main()
