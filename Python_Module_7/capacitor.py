from ex1 import *

def main() -> None:
    print("Testing Creature with healing capability")
    print(" base:")

    heal_creature_base = HealingCreatureFactory.create_base()
    print(f"{heal_creature_base.describe()}")
    print(f"{heal_creature_base.attack}")
    print(f"{heal_creature_base.heal()}")

    print(" evolved:")

    heal_creature_evolved = HealingCreatureFactory.create_evolved(heal_creature_base)
    print(f"{heal_creature_evolved.describe()}")
    print(f"{heal_creature_evolved.attack}")
    print(f"{heal_creature_evolved.heal}\n")

    print("Testing Creature with transform capability")
    print(" base:")

    transform_creature_base = TransformCreatureFactory.create_base()
    print(f"{transform_creature_base.describe()}")
    print(f"{transform_creature_base.attack}")
    print(f"{transform_creature_base.transform()}")
    print(f"{transform_creature_base.attack}")
    print(f"{transform_creature_base.revert()}")

    transform_creature_evolved = TransformCreatureFactory.create_evolved(transform_creature_base)
    print(" evolved:")
    print(f"{transform_creature_evolved.describe()}")
    print(f"{transform_creature_evolved.attack}")
    print(f"{transform_creature_evolved.transform()}")
    print(f"{transform_creature_evolved.attack}")
    print(f"{transform_creature_evolved.revert()}")

if __name__ == "__main__":
    main()

