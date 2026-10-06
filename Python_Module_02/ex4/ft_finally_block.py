#!/usr/bin/env python3

class PlantError(Exception):
    def __init__(self, error: str = "Unknown error"):
        super().__init__(error)


def water_plant(plant_name: str):
    if plant_name == plant_name.capitalize():
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(
                f"Caught PlantError:"
                f" Invalid plant name to water:"
                f" '{plant_name}'"
        )


def test_watering_system():
    Veggies = ["Tomato", "Lettuce,", "Carrots"]
    print("===Garden Watering System ===\n")
    print(
        "Testing valid plants...\n",
        "Opening watering systems",
        sep=''
    )
    for vegetable in Veggies:
        water_plant(vegetable)
    print("Closing watering system\n")

    Veggies2 = ["Tomato", "lettuce"]
    print("Testing invalid plants...")
    print("Opening watering system")
    try:
        for vegetable2 in Veggies2:
            water_plant(vegetable2)
    except PlantError as e:
        print(
            f"{e}\n"
            ".. ending tests and returning to main"
        )
    finally:
        print(
            "Closing watering system\n"
            "\nCleanup always happens, even with errors!"
        )


def main():
    test_watering_system()


if __name__ == "__main__":
    main()
