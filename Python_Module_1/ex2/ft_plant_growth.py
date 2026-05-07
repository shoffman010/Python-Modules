#!/usr/bin/env python3

class Plant:
    name: str
    height: float
    a_age: int

    def grow(self, growth_factor: float) -> None:
        self.height += growth_factor

    def age(self) -> None:
        self.a_age += 1

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.a_age} days old")


def init_plant(plant_name: str) -> None:
    growth_factor = 0.0
    print("=== Garden Plant Growth ===")

    if plant_name == "Rose":
        rose = Plant()
        rose.name = plant_name
        rose.height = 25.0
        rose.a_age = 30

        rose.show()
        for day in range(1, 8):
            print(f"=== Day {day} ===")
            rose.grow(0.8)
            rose.age()
            growth_factor += 0.8
            rose.show()
        print(f"Growth this week: {round(growth_factor, 1)}cm")

    elif plant_name == "Cactus":
        cactus = Plant()
        cactus.name = plant_name
        cactus.height = 110.0
        cactus.a_age = 423

        cactus.show()
        for day in range(1, 8):
            print(f"=== Day {day} ===")
            cactus.grow(1.1)
            cactus.age()
            growth_factor += 1.1
            cactus.show()
        print(f"Growth this week: {round(growth_factor, 1)}cm")

    else:
        plant = Plant()
        plant.name = plant_name
        plant.height = 5.0
        plant.a_age = 10

        plant.show()
        for day in range(1, 8):
            print(f"=== Day {day} ===")
            plant.grow(0.3)
            plant.age()
            growth_factor += 0.3
            plant.show()
        print(f"Growth this week: {round(growth_factor, 1)}cm")


if __name__ == "__main__":
    init_plant("Raspberry")
