from ex1 import HealingCreatureFactory, TransformCreatureFactory


def main() -> None:
    print("Testing Creature with healing capability")
    print(" base:")

    heal_factory = HealingCreatureFactory()
    heal_creature_base = heal_factory.create_base()
    print(f"{heal_creature_base.describe()}")
    print(f"{heal_creature_base.attack()}")
    print(f"{heal_creature_base.heal()}")

    print(" evolved:")

    heal_creature_evolved = heal_factory.create_evolved()
    print(f"{heal_creature_evolved.describe()}")
    print(f"{heal_creature_evolved.attack()}")
    print(f"{heal_creature_evolved.heal}\n")

    print("Testing Creature with transform capability")
    print(" base:")

    transform_factory = TransformCreatureFactory()
    transform_creature_base = transform_factory.create_base()
    print(f"{transform_creature_base.describe()}")
    print(f"{transform_creature_base.attack()}")
    print(f"{transform_creature_base.transform()}")
    print(f"{transform_creature_base.attack()}")
    print(f"{transform_creature_base.revert()}")

    transform_creature_evolved = transform_factory.create_evolved()
    print(" evolved:")
    print(f"{transform_creature_evolved.describe()}")
    print(f"{transform_creature_evolved.attack()}")
    print(f"{transform_creature_evolved.transform()}")
    print(f"{transform_creature_evolved.attack()}")
    print(f"{transform_creature_evolved.revert()}")


if __name__ == "__main__":
    main()
