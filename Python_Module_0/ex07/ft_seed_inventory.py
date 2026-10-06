def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    capitalized = seed_type.capitalize()
    if unit == "packets":
        print(f"{capitalized} seeds: {quantity} {unit} available")
    elif unit == "grams":
        print(f"{capitalized} seeds: {quantity} {unit} total")
    elif unit == "area":
        print(f"{capitalized} seeds: covers {quantity} square meters")
    else:
        print("Unknown unit type")
