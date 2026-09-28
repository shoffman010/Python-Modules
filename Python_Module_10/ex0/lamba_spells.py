def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(
        artifacts,
        key = lambda artifact: artifact["power"],
        reverse=True
    )


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda artifact: artifact["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: f"*{spell}*", spells))


def mage_stats(mages: list[dict]) -> dict:
    ...


if __name__ == "__main__":

    artifacts = [
        {'name': 'Ice Wand', 'power': 93, 'type': 'accessory'},
        {'name': 'Storm Crown', 'power': 112, 'type': 'weapon'},
        {'name': 'Wind Cloak', 'power': 102, 'type': 'weapon'},
        {'name': 'Water Chalice', 'power': 105, 'type': 'focus'}
        ]

    mages = [
        {'name': 'Sage', 'power': 70, 'element': 'lightning'},
        {'name': 'Morgan', 'power': 61, 'element': 'shadow'},
        {'name': 'Casey', 'power': 56, 'element': 'water'},
        {'name': 'Phoenix', 'power': 79, 'element': 'light'},
        {'name': 'Zara', 'power': 52, 'element': 'water'}
        ]

    spells = [
        'darkness',
        'earthquake',
        'blizzard',
        'freeze'
        ]

    print(
        "Testing artifact_sorter",
        "====================================",
        sep="\n"
    )
    for artifact in artifact_sorter(artifacts):
        print(artifact)
    print()
    
    print(
        "Testing power_filter",
        "====================================",
        sep="\n"
    )
    for power in power_filter(mages, 50):
        print(power)
    print()
    
    print(
        "Testing spell_transformer",
        "====================================",
        sep="\n"
    )
    for spell in spell_transformer(spells):
        print(spell)