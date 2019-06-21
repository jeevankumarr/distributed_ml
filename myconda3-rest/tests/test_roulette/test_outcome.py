from .context import roulette
from roulette import Outcome
import random


def create_outcome(name=None, odds=None):
    if name is None:
        name = '1'

    if odds is None:
        odds = 35

    tmp_outcome = Outcome(name, odds)
    return name, odds, tmp_outcome

def test_outcome_init():
    name, odds, tmp_outcome = create_outcome()
    assert tmp_outcome.name == name
    assert tmp_outcome.odds == odds

def test_outcome_payout():
    name, odds, tmp_outcome = create_outcome()
    bet = random.random()*1000
    assert tmp_outcome.win_amount(bet) == bet * odds

def test_outcome_eq():
    a_name, a_odds, a_outcome = create_outcome('1', 35)

    b_name, b_odds, b_outcome = create_outcome('1', 55)
    assert a_outcome == b_outcome

    b_name, b_odds, b_outcome = create_outcome('2', 55)
    assert ~(a_outcome == b_outcome)

def test_outcome_ne():
    a_name, a_odds, a_outcome = create_outcome('1', 35)

    b_name, b_odds, b_outcome = create_outcome('1', 55)
    assert ~(a_outcome != b_outcome)

    b_name, b_odds, b_outcome = create_outcome('2', 55)
    assert a_outcome != b_outcome

def test_outcome_str():
    name, odds, tmp_outcome = create_outcome()
    assert tmp_outcome.__str__() == f'{tmp_outcome.name} ({tmp_outcome.odds}:1)'

def test_outcome_repr():
    name, odds, tmp_outcome = create_outcome()
    assert tmp_outcome.__repr__() == f'Outcome({tmp_outcome.name}, {tmp_outcome.odds})'
