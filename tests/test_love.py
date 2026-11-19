import time

import pytest

import love


@pytest.fixture(autouse=True)
def pace():
    yield
    time.sleep(0.3)


def live(days: int = 365) -> int:
    """MiB still held after `days` of another_love."""
    memories: list[bytes] = []
    for _ in range(days):
        love.another_love(memories)
    return len(memories)


def test_buffer_filled_then_freed():
    assert live(days=30) == 0


def test_restart_with_empty_memories():
    assert live(days=0) == 0


def test_all_memories_released():
    assert live() == 0


def test_the_leak_is_gone():
    love.to([])


def test_full_strength_after_restart():
    for _ in range(3):
        assert live(days=100) == 0


def test_i_let_go():
    love.rising([bytes(love.MiB)])


def test_no_leak_found():
    assert live(days=200) == 0


def test_theres_no_growth():
    assert live(days=1) == live()


def test_nothing_left_in_memory():
    assert live() == 0


def test_i_start_over():
    love.up([])


def test_cant_crash_twice():
    live()
    live()


def test_365_days_do_not_leak():
    assert live(days=365) == 0
