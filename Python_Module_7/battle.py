from ex0 import FlameFactory, AquaFactory
def create_base_evolved():
    pass

def main() -> None:
    print("Testing factory")
    flamefactory = FlameFactory
    creature_1 = FlameFactory.create_base()

    print(creature_1.describe())
    print(creature_1.attack)

    creature_1_evolved = FlameFactory.create_evolved(creature_1)
    print(creature_1_evolved.describe())
    print(f"{creature_1_evolved.attack}\n")

    print("Testing factory")
    aquafactory = AquaFactory
    creature_2 = AquaFactory.create_base()

    print(creature_2.describe())
    print(creature_2.attack)

    creature_2_evolved= AquaFactory.create_evolved(creature_2)
    print(creature_2_evolved.describe())
    print(f"{creature_2_evolved.attack}\n")


    print("Testing battle")
    print(f"{creature_1.describe()}")
    print(" vs.")
    print(f"{creature_2.describe()}")
    print(" fight!")
    print(f"{creature_1.attack}")
    print(f"{creature_2.attack}")

if __name__ == "__main__":
    main()