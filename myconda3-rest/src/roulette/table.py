from .bet import Bet


class Table():
    def __init__(self, limit, minimum):
        self.limit = limit
        self.minimum = minimum
        self.bets = []

    def place_bet(self, bet):
        """Add this bet to a list of working bets

        Args:
            bet(Bet): The bet to be placed

        Returns:
            None

        Raises:
            InvalidBet
        """
        if self.is_valid(bet):
            self.bets.append(bet)
            return True

    def __iter__(self):
        return self.bets.__iter__()

    def __str__(self):
        return ', '.join([bet for bet in self.bets])

    def __repr__(self):
        bet_str = ', '.join([bet for bet in self.bets])
        return f"Table({bet_str})"

    def is_valid(self, bet):
        invalid_bet = False
        bet_sum = sum([b.amount for b in self.bets])

        if bet.amount + bet_sum > self.limit:

            invalid_bet = True
            raise InvalidBetException(f'Bet amount is greater than the limit {bet.amount + bet_sum}, limit is {self.limit}')

        if bet.amount < self.minimum:
            invalid_bet = True
            raise InvalidBetException(
                f'Bet amount is lower than the minimum {bet.amount}, limit is {self.minimum}')


        return True

    def clear_bets(self):
        self.bets.clear()

class InvalidBetException(Exception):
    pass