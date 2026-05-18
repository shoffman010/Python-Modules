#!/usr/bin/env python3

class Plant:
    _name: str
    _age: int
    _height: float

    def __init__(
                self,
                name: str,
                age: int,
                height: float
            ) -> None:
        self._name = name
        self._age = 0
        self._height = 0.0
        self.set_height(height)
        self.set_age(age)

    def set_height(self, _height: float) -> None:
        if _height < 0:
            print(f"{self._name}: Error, height can't be negative")
            return
        self._height = _height

    def set_age(self, _age: int) -> None:
        if _age < 0:
            print(f"{self._name}: Error, age can't be negative")
            return
        self._age = _age

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._age} days old",)


class Flower(Plant):
    plant_type = "Flower"
    _color: str
    _bloom: bool

    def __init__(
            self,
            _name: str,
            _age: int,
            _height: float,
            _color: str,
            _bloom: bool
    ) -> None:
        super().__init__(_name, _age, _height)
        self._color = _color
        self._bloom = _bloom

    def bloom(self) -> None:
        print(f"[asking the {self._name.lower()} to bloom]")
        self._bloom = True

    def show(self) -> None:
        super().show()
        if not self._bloom:
            print(
                f" Color: {self._color}\n",
                f"{self._name} has not bloomed yet"
            )
        else:
            print(
                f" Color: {self._color}\n",
                f"{self._name} is blooming beautifully!"
            )


class Tree(Plant):
    plant_type = "Tree"

    _trunk: float
    _shade: bool

    def __init__(
            self,
            _name: str,
            _age: int,
            _height: float,
            _trunk: float,
            _shade: bool
    ) -> None:
        super().__init__(_name, _age, _height)
        self._trunk = _trunk
        self._shade = _shade

    def produce_shade(self) -> None:
        print(f"[asking the {self._name.lower()} to produce shade]")
        self._shade = True
        print(
            f"Tree {self._name} now produces a shade of "
            f"{self._height}cm long and {self._trunk}cm wide"
        )

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk}cm")


class Vegetable(Plant):
    plant_type = "Vegetable"

    _harvest: str
    _nutrition: int
    _grow: int

    def __init__(
            self,
            _name: str,
            _age: int,
            _height: float,
            _harvest: str,
            _nutrition: int,
            _grow: int
    ) -> None:
        super().__init__(_name, _age, _height)
        self._harvest = _harvest
        self._nutrition = _nutrition
        self._grow = _grow

    def show(self) -> None:
        super().show()
        print(
            f" Harvest Season: {self._harvest}\n"
            f" Nutritional value: {self._nutrition}"
        )

    def age(self) -> None:
        self._age += self._grow

    def grow(self) -> None:
        self._height += self._grow * 2.1
        self._nutrition += self._grow


def main() -> None:
    print("=== Garden Plant Types ===")
    rose = Flower("Rose", 10, 15.0, "red", False)
    print(f"=== {rose.plant_type}")
    if not rose._bloom:
        rose.show()
        rose.bloom()
    rose.show()
    print("")

    oak = Tree("Oak", 365, 200.0, 5.0, False)
    print(f"=== {oak.plant_type}")
    oak.show()
    oak.produce_shade()
    print("")

    tomato = Vegetable("Tomato", 10, 5.0, "April", 0, 20)
    print(f"=== {tomato.plant_type}")
    tomato.show()
    print(f"[make the {tomato._name} grow and age for {tomato._grow} days]")
    tomato.grow()
    tomato.age()
    tomato.show()


if __name__ == "__main__":
    main()
