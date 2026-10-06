#!/usr/bin/env python3

import math


def parse_input(raw_input: str) -> tuple[float, float, float]:
    parts = raw_input.split(",")

    if len(parts) != 3:
        raise SyntaxError

    coordinates = []

    for part in parts:
        clean_part = part.strip()
        try:
            coordinates.append(float(clean_part))
        except ValueError as error:
            raise ValueError(
                f"Error on parameter '{clean_part}': {error}"
            )

    return (coordinates[0], coordinates[1], coordinates[2])


def get_player_pos() -> tuple[float, float, float]:
    while True:
        try:
            return parse_input(
                input("Enter new coordinates as floats in format 'x,y,z': ")
            )
        except ValueError as error:
            print(error)
        except SyntaxError:
            print("Invalid syntax")


def distance_coordinates(
    coordinate_1: tuple[float, float, float],
    coordinate_2: tuple[float, float, float],
) -> float:
    return math.sqrt(
        (coordinate_1[0] - coordinate_2[0]) ** 2
        + (coordinate_1[1] - coordinate_2[1]) ** 2
        + (coordinate_1[2] - coordinate_2[2]) ** 2
    )


def main() -> None:
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")

    coordinate_1 = get_player_pos()

    print(
        f"Got a first tuple: {coordinate_1}\n"
        f"It includes: X={coordinate_1[0]}, "
        f"Y={coordinate_1[1]}, "
        f"Z={coordinate_1[2]}"
    )

    center = (0.0, 0.0, 0.0)
    print(
        f"Distance to center: "
        f"{round(distance_coordinates(coordinate_1, center), 4)}\n"
    )

    print("Get a second set of coordinates")
    coordinate_2 = get_player_pos()

    print(
        "Distance between the 2 sets of coordinates:",
        round(distance_coordinates(coordinate_1, coordinate_2), 4),
    )


if __name__ == "__main__":
    main()
