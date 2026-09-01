import alchemy.elements

def main() -> None:
    print("=== Alembic 5 ===")
    print("Accessing the alchemy module using 'from alchemy import ...'")
    print("Testing create_air: ", end="")

    Test = alchemy.elements.create_air()

    if Test != "Air element created":
        print("Failed")
        return
    
    print(f"{Test}\n")

if __name__ == "__main__":
    main()