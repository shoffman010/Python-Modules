from alchemy import elements

def main() -> None:
    print("=== Alembic 3 ===")
    print("Accessig alchemy/elements.py using 'from ... import ...' structure")
    print("Testing create_air: ", end="")
    Test = elements.create_air()
    if Test != "Air element created":
        print("Failed")
        return
    print(f"Test\n")

    main()