def print_days(current: int, days: int) -> None:
    if current > days:
        return
    print("Day " + str(current))
    print_days(current + 1, days)


def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    print_days(1, days)
    print("Harvest time!")
