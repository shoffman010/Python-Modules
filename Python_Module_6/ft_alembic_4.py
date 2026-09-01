import alchemy

def main() -> None:
    print("=== Alembic 4 ===")
    print("Accessing the alchemy module using 'import alchemy'")
    print("Testing create_air: ", end="")

    Test = alchemy.create_air()

    if Test != "Air element created":
        print("Failed")
        return
    
    print(Test)
    
    print("Now show that not all functions can be reached")
    print("This will raise an exception!")
    print("Testing the hidden create_earth: ", end="")
    print(f"{alchemy.create_earth()}")


if __name__ == "__main__":
    main()