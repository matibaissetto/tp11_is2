
from collatz import collatz


def test_t1():
    assert collatz(1) == 0


def test_t2():
    assert collatz(2) == 1


def test_t3():
    assert collatz(3) == 7


def test_t4():
    assert collatz(4) == 2


def test_t5():
    assert collatz(6) == 8


def test_t6():
    assert collatz(20) == 7
