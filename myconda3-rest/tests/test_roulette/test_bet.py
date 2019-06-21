from .context import roulette
import sys


from roulette import Bet
from roulette import Outcome

def test_bet_lost_amount():
    BET_AMT = 5
    b = Bet(BET_AMT, None)

    assert BET_AMT == b.lose_amount()

def test_bet_won_amount():
    BET_AMT = 5
    ODDS = 2
    b = Bet(BET_AMT, Outcome('Even', ODDS))

    assert BET_AMT * ODDS == b.win_amount()
