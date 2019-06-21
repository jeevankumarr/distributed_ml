import math
from .context import roulette
from roulette import Wheel, BinBuilder
from roulette import Outcome


def test_add_outcome():
    wheel = Wheel()

    wheel.add_outcome(0, Outcome(f'0', 35))
    wheel.add_outcome(0, Outcome(f'0', 35))

    assert Outcome(f'0', 35) in wheel.get(0)
    assert 1 == len(wheel.get(0))

    wheel.add_outcome(0, Outcome(f'street', 11))
    assert Outcome(f'street', 11) in wheel.get(0)
    assert 2 == len(wheel.get(0))

def test_wheel_next():
    wheel = Wheel(seed=1)
    bb = BinBuilder()

    # bb.generate_straight_bets(wheel)
    bb.build_bins(wheel)
    # wheel.add_outcome(0, Outcome(f'0', 35))
    ct = 10
    expected_seq = [8, 36, 4, 16, 7, 31, 28, 30, 24, 13]
    for num in expected_seq:
        i, bin = wheel.next()
        assert num == i

def test_bin_staight_bets():
    wheel = Wheel()
    bb = BinBuilder()

    bb.generate_straight_bets(wheel)


    for i, bin in enumerate(wheel.bins):
        assert 1 == len(bin)
        nm = f'{i}' if i < 37 else '00'
        assert Outcome(nm, 35) in bin

def test_street_bets():
    wheel = Wheel()
    bb = BinBuilder()

    bb.generate_street_bets(wheel)
    for i, bin in enumerate(wheel.bins):
        if i == 0 or i == 37:
            assert 0 == len(bin)
        else:
            assert 1 == len(bin)

    for i in range(1, 36, 3):
        out = Outcome(f'{i} {i + 1} {i + 2}', 11)
        assert out in wheel.get(i)
        assert out in wheel.get(i + 1)
        assert out in wheel.get(i + 2)

def test_split_bets():
    wheel = Wheel()
    bb = BinBuilder()

    bb.generate_split_bets(wheel)
    for r in range(12):
        # left-right splits
        n = 3 * r + 1
        out = Outcome(f'{n} {n + 1}', 17)
        assert out in wheel.get(n) and out in wheel.get(n + 1)

        n = 3 * r + 2
        out = Outcome(f'{n} {n + 1}', 17)
        assert out in wheel.get(n) and out in wheel.get(n + 1)

        # top-down splits
        if r == 11:
            break
        else:
            n = 3 * r + 1
            out = Outcome(f'{n} {n + 3}', 17)
            assert out in wheel.get(n) and out in wheel.get(n + 3)

            n += 1
            out = Outcome(f'{n} {n + 3}', 17)
            assert out in wheel.get(n) and out in wheel.get(n + 3)

            n += 1
            out = Outcome(f'{n} {n + 3}', 17)
            assert out in wheel.get(n) and out in wheel.get(n + 3)

def test_corner_bets():
    wheel = Wheel()
    bb = BinBuilder()
    bb.generate_corner_bets(wheel)

    for r in range(0, 11):
        n = 3 * r + 1
        outcome = Outcome(f'{n} {n+1} {n+3} {n+4}', 8)
        assert outcome in wheel.get(n)
        assert outcome in wheel.get(n + 1)
        assert outcome in wheel.get(n + 3)
        assert outcome in wheel.get(n + 4)

        n += 1
        outcome = Outcome(f'{n} {n + 1} {n + 3} {n + 4}', 8)
        assert outcome in wheel.get(n)
        assert outcome in wheel.get(n + 1)
        assert outcome in wheel.get(n + 3)
        assert outcome in wheel.get(n + 4)

def test_line_bets():
    wheel = Wheel()
    bb = BinBuilder()
    bb.generate_line_bets(wheel)
    for r in range(0, 11):
        n = 3 * r + 1
        line_out = Outcome(f'{n} {n + 1} {n + 2} {n + 3} {n + 4} {n + 5}', 5)
        assert line_out in wheel.get(n)
        assert line_out in wheel.get(n + 1)
        assert line_out in wheel.get(n + 2)
        assert line_out in wheel.get(n + 3)
        assert line_out in wheel.get(n + 4)
        assert line_out in wheel.get(n + 5)

def test_generate_doze_bets():
    wheel = Wheel()
    bb = BinBuilder()
    bb.generate_dozen_bets(wheel)

    for i, bin in enumerate(wheel.bins):
        if i == 0 or i == 37:
            assert 0 == len(bin)
        else:
            out = Outcome(f'Dozen {math.ceil(i/12)}', 2)
            assert out in bin

def test_column_bets():
    wheel = Wheel()
    bb = BinBuilder()
    bb.generate_column_bets(wheel)

    col_one = Outcome(f'Column 1', 2)
    col_two = Outcome(f'Column 2', 2)
    col_thr = Outcome(f'Column 3', 2)
    outcomes = {1:col_one, 2:col_two, 0:col_thr}

    for i, bin in enumerate(wheel.bins):
        if i == 0 or i == 37:
            assert 0 == len(bin)
        else:
            out = outcomes[i%3]
            assert out in bin

def test_even_money_bets():
    wheel = Wheel()
    bb = BinBuilder()
    bb.generate_even_money_bets(wheel)
    # Red-Black
    reds = {1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36}
    blacks = set(range(1, 37)) - reds
    red_out = Outcome('Red', 1)
    black_out = Outcome('Black', 1)

    # Even-Odd
    even_out = Outcome('Even', 1)
    odd_out = Outcome('Odd', 1)

    # Hi - Lo
    hi_out = Outcome('High', 1)
    lo_out = Outcome('Low', 1)

    for i, bin in enumerate(wheel.bins):
        if i == 0 or i == 37:
            assert 0 == len(bin)
        elif i < 19:
            assert lo_out in bin
        else:
            assert hi_out in bin

        if i == 0 or i == 37:
            assert 0 == len(bin)
        elif i % 2 == 0:
            assert even_out in bin
        else:
            assert odd_out in bin

        if i == 0 or i == 37:
            assert 0 == len(bin)
        elif i in reds:
            assert red_out in bin
        else:
            assert black_out in bin

def test_get_outcome():
    wheel = Wheel()
    bb = BinBuilder()
    bb.generate_even_money_bets(wheel)
    bb.generate_column_bets(wheel)

    assert Outcome('High', 1) == wheel.get_outcome('High')
    assert Outcome('Low', 1) == wheel.get_outcome('Low')
    assert Outcome('Red', 1) == wheel.get_outcome('Red')
    assert Outcome('Black', 1) == wheel.get_outcome('Black')

    assert Outcome('Column 1', 1) == wheel.get_outcome('Column 1')
    assert Outcome('Column 2', 1) == wheel.get_outcome('Column 2')
    assert Outcome('Column 3', 1) == wheel.get_outcome('Column 3')