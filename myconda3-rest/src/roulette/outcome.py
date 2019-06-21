"""

Note about design:
    todo: add design notes to outcome.py

Note about choice of equality:
    todo: clean choice of quality up
    - id: Python object id
    - hash: Hash of the object ()
    -
"""
class Outcome():
    """Calculates the payout amount

    """
    def __init__(self, name, odds):
        """

        Args:
            name (str): Name of the outcome
            odds (int): Payout odds of this outcome
        """
        self.name = name
        self.odds = odds

    def win_amount(self, amount):
        """Return the product of this Outcome's odds by the given amount.

        Args:
            amount(float):

        Returns:
            float: payout amount
        """
        return self.odds * amount

    def __eq__(self, other):
        """

        Args:
            other (Outcome):

        Returns:
            boolean
        """
        return self.name.__eq__(other.name)

    def __ne__(self, other):
        """Compare the name attributes of `self` and `outer`.

        Args:
            other (Outcome):

        Returns:
            boolean
        """
        return self.name.__ne__(other.name)

    def __hash__(self):
        return hash(self.name)

    def __str__(self):
        """Easy-to-read representation of this outcome."""
        return f'{self.name} ({self.odds}:1)'

    def __repr__(self):
        """Detailed representation of this outcome."""
        return f'Outcome({self.name}, {self.odds})'
