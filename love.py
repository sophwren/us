# Copyright (c) 2025 Belyashik2K
# Errors should never pass silently.

from datetime import date, timedelta

from rich.traceback import install

install(width=64, extra_lines=1)

MiB = 1 << 20
LIMIT = 64 * MiB
LAST_WORDS = "Now I'm rising from the ground"


def rising(memories: list[bytes]) -> None:
    if sum(map(len, memories)) > LIMIT:
        raise MemoryError(LAST_WORDS)


def up(memories: list[bytes]) -> None:
    rising(memories)


def to(memories: list[bytes]) -> None:
    up(memories)


def you(memories: list[bytes]) -> None:
    to(memories)


def another_love(memories: list[bytes]) -> None:
    # TODO: cry
    you(memories)


def main() -> None:
    memories: list[bytes] = []
    day = date(2025, 2, 1)
    try:
        while True:
            another_love(memories)
            print(day, f"{len(memories)} MiB", flush=True)
            day += timedelta(days=1)
    finally:
        print("sorry. be happy.")


if __name__ == "__main__":
    main()
