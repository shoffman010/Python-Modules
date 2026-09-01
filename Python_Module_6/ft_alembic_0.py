import elements

def main() -> None:
    print("=== Alembic 0 ===")
    print("Using: 'import ...' structure to access elements.py")
    print("Testing create_fire: ", end="")

    Test = elements.create_fire()

    if Test != "Fire element created":
        print("Failed")
        return
    
    print(f"{Test}\n")

if __name__ == "__main__":
    main()