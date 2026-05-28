#!/usr/bin/env python3

import sys


def parse_inventory() -> dict[str, int]:
    inventory: dict[str, int] = {}

    for parameter in sys.argv[1:]:
        parts = parameter.split(":")

        if len(parts) != 2 or parts[0] == "":
            print(f"Error - invalid parameter '{parameter}'")
            continue

        item_name = parts[0]
        quantity_text = parts[1]

        if item_name in inventory:
            print(f"Redundant item '{item_name}' - discarding")
            continue

        try:
            quantity = int(quantity_text)
        except ValueError as error:
            print(f"Quantity error for '{item_name}': {error}")
            continue

        inventory[item_name] = quantity

    return inventory


def print_percentages(inventory: dict[str, int], total_quantity: int) -> None:
    for item_name in inventory.keys():
        percentage = round(inventory[item_name] / total_quantity * 100, 1)
        print(f"Item {item_name} represents {percentage}%")


def print_most_and_least(inventory: dict[str, int]) -> None:
    item_names = list(inventory.keys())

    most_item = item_names[0]
    least_item = item_names[0]

    for item_name in inventory.keys():
        if inventory[item_name] > inventory[most_item]:
            most_item = item_name
        if inventory[item_name] < inventory[least_item]:
            least_item = item_name

    print(
        f"Item most abundant: {most_item} "
        f"with quantity {inventory[most_item]}"
    )
    print(
        f"Item least abundant: {least_item} "
        f"with quantity {inventory[least_item]}"
    )


def analyze_inventory(inventory: dict[str, int]) -> None:
    print(f"Got inventory: {inventory}")

    item_list = list(inventory.keys())
    print(f"Item list: {item_list}")

    total_quantity = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total_quantity}")

    if len(inventory) == 0 or total_quantity == 0:
        print("No valid inventory data to analyze.")
        return

    print_percentages(inventory, total_quantity)
    print_most_and_least(inventory)

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory = parse_inventory()
    analyze_inventory(inventory)


if __name__ == "__main__":
    main()