from ex0 import FlameFactory, AquaFactory


def main() -> None:
    print("Testing factory")
    flame_factory = FlameFactory()
    creature_1 = flame_factory.create_base()

    print(creature_1.describe())
    print(creature_1.attack())

    creature_1_evolved = flame_factory.create_evolved()
    print(creature_1_evolved.describe())
    print(f"{creature_1_evolved.attack()}\n")

    print("Testing factory")
    aqua_factory = AquaFactory()
    creature_2 = aqua_factory.create_base()

    print(creature_2.describe())
    print(creature_2.attack())

    creature_2_evolved = aqua_factory.create_evolved()
    print(creature_2_evolved.describe())
    print(f"{creature_2_evolved.attack()}\n")

    print("Testing battle")
    print(f"{creature_1.describe()}")
    print(" vs.")
    print(f"{creature_2.describe()}")
    print(" fight!")
    print(f"{creature_1.attack()}")
    print(f"{creature_2.attack()}")


if __name__ == "__main__":
    main()
