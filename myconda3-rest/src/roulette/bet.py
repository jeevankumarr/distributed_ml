from .outcome import Outcome

class Bet():
    def __init__(self, amount, outcome: Outcome):
        self.amount = amount
        self.outcome = outcome

    def win_amount(self):
        return self.outcome.win_amount(self.amount)

    def lose_amount(self):
        return self.amount

    def __str__(self):
        return f'{self.amount} on {self.outcome}'

    def __repr__(self):
        return f'Bet({self.amount}, {self.outcome})'
