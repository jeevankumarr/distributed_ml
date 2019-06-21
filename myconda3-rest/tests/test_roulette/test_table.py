
import pytest
# from itertools import Iterator

from .context import roulette
from roulette import Table, InvalidBetException
from roulette import Bet
from roulette import Wheel

def test_table_place_bet():
    tt = Table(100, 5)
    wh = Wheel()
    bt = Bet(10, wh.get_outcome('Even'))
    assert True == tt.place_bet(bt)

def test_table_iter_bets():
    tt = Table(100, 5)
    test_bets = []
    wh = Wheel()

    bt = Bet(10, wh.get_outcome('Even'))
    test_bets.append(bt)
    bt = Bet(5, wh.get_outcome('Even'))
    test_bets.append(bt)

    for test_bt, bt in zip(test_bets, tt):
        assert  test_bt == bt

def test_table_is_valid():
    wh = Wheel()

    with pytest.raises(InvalidBetException) as e_info:
        tt = Table(100, 5)

        # should violate the min bet amount and throw exception
        bt = Bet(1, wh.get_outcome('Even'))
        tt.place_bet(bt)

    with pytest.raises(InvalidBetException) as e_info:
        tt = Table(10, 5)
        bt = Bet(5, wh.get_outcome('Even'))
        tt.place_bet(bt)

        bt = Bet(5, wh.get_outcome('Even'))
        tt.place_bet(bt)

        # should exceed table limit and throw exception
        bt = Bet(5, wh.get_outcome('Even'))
        tt.place_bet(bt)

# def test_table_iter():
#     tt = Table(100, 5)
#     print(tt.__iter__().isinstance(Iterator))