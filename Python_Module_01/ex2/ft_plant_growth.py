#!/usr/bin/env python3

class Plant:
    name: str
    height: float
    days_old: int
    daily_growth: float

    def __init__(
            self,
            name: str,
            height: float,
            days_old: int,
            daily_growth: float
    ) -> None:
        self.name = name
        self.height = height
        self.days_old = days_old
        self.daily_growth = daily_growth

    def grow(self) -> None:
        self.height += self.daily_growth

    def age(self) -> None:
        self.days_old += 1

    def show(self) -> None:
        print(
            f"{self.name}: {round(self.height, 1)}cm, "
            f"{self.days_old} days old"
        )


def simulate_week(plant: Plant) -> None:
    total_growth = 0.0

    plant.show()
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        plant.grow()
        plant.age()
        total_growth += plant.daily_growth
        plant.show()

    print(f"Growth this week: {round(total_growth, 1)}cm")


def main() -> None:
    print("=== Garden Plant Growth ===")

    plant = Plant("Raspberry", 5.0, 10, 0.3)
    simulate_week(plant)


if __name__ == "__main__":
    main()
