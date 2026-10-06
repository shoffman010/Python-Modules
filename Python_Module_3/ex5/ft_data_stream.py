#!/usr/bin/env python3
import random
from typing import Generator


def gen_events() -> Generator[tuple[str, str], None, None]:
    players = [
        "bob",
        "dylan",
        "alice",
        "charlie"
        ]
    actions = [
        "run",
        "eat",
        "sleep",
        "grab",
        "move",
        "climb",
        "swim",
        "release"
        ]

    while True:
        player = random.choice(players)
        action = random.choice(actions)
        yield (player, action)


def consume_events(
    events_list: list[tuple[str, str]],
) -> Generator[tuple[str, str], None, None]:
    while len(events_list) > 0:
        index = random.randrange(len(events_list))
        event = events_list.pop(index)
        yield event


def main() -> None:
    event_stream = gen_events()
    events_list: list[tuple[str, str]] = []

    print("=== Game Data Stream Processor ===")

    for i in range(1000):
        event = next(event_stream)
        if i < 10:
            events_list.append(event)
        player, action = event
        print(f"Event {i}: Player {player} did action {action}")

    print(f"Built list of 10 events: {events_list}")

    for event in consume_events(events_list):
        print(
            f"Got event from list: {event}\n"
            f"Remains in list: {events_list}"
        )


if __name__ == "__main__":
    main()
