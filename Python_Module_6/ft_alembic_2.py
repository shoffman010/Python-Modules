from alchemy import elements

def main() -> None:
    print("=== Alembic 2 ===")
    print("Accessing alchemy/elements.py using 'import ...' structure")
    print("Testing create_earth: ", end="")

    Test = elements.create_earth()

    if Test != "Earth element created":
        print("Failed")
        return
    
    print(f"{Test}\n")

if __name__ == "__main__":
    main()