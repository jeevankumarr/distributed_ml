"""

Responsibilities:
1. Container Responsbility: Have all the bins
2. Random Bin Selection Responsbility

"""
import random
from .outcome import Outcome
from .bin import Bin


class Wheel():

    def __init__(self, seed=None):
        # TODO: Add a bin construction method
        self.bins = [frozenset() for _ in range(38)]
        if seed is not None:
            random.seed(seed)
        self.rng = random
        self.all_outcomes = {}



    def get_outcome(self, name):
        return self.all_outcomes.get(name, None)

    def add_outcome(self, number, outcome):
        """

        Args:
            number (int): index of bin [0, 37]
            outcome (Outcome): The outcome to be added to the Bin

        Returns:
            None

        """
        self.all_outcomes[outcome.name] = outcome
        self.bins[number] = self.bins[number].union(frozenset([outcome]))



    def next(self):
        """Randomly selects and returns a Bin.

        Returns:
            Bin: randomly selected Bin
        """
        idx = self.rng.choice(range(len(self.bins)))
        return idx, self.bins[idx]

    def get(self, bin):
        """Get a Bin with the given index

        Args:
            bin (int): index of the bin [0, 37]

        Returns:
            Bin: Requested Bin
        """
        return self.bins[bin]

class BinBuilder():

    def generate_straight_bets(self, wheel):
        for i in range(0, 37):
            wheel.add_outcome(i, Outcome(f'{i}', 35))
        wheel.add_outcome(37, Outcome('00', 35))

    def generate_split_bets(self, wheel):

        # left-right splits
        for r in range(0, 12):
            col_num = 3 * r + 1
            outcome = Outcome(f'{col_num} {col_num + 1}', 17)
            wheel.add_outcome(col_num, outcome)
            wheel.add_outcome(col_num + 1, outcome)

            col_num = 3 * r + 2
            outcome = Outcome(f'{col_num} {col_num + 1}', 17)
            wheel.add_outcome(col_num, outcome)
            wheel.add_outcome(col_num + 1, outcome)

        for r in range(0, 11):
            n = 3 * r + 1
            outcome = Outcome(f'{n} {n + 3}', 17)
            wheel.add_outcome(n, outcome)
            wheel.add_outcome(n + 3, outcome)

            n += 1
            outcome = Outcome(f'{n} {n + 3}', 17)
            wheel.add_outcome(n, outcome)
            wheel.add_outcome(n + 3, outcome)

            n += 1
            outcome = Outcome(f'{n} {n + 3}', 17)
            wheel.add_outcome(n, outcome)
            wheel.add_outcome(n + 3, outcome)

    def generate_street_bets(self, wheel):
        for r in range(0, 12):
            col = 3 * r + 1
            outcome = Outcome(f'{col} {col + 1} {col + 2}', 11)
            wheel.add_outcome(col, outcome)
            wheel.add_outcome(col + 1, outcome)
            wheel.add_outcome(col + 2, outcome)

    def generate_corner_bets(self, wheel):
        for r in range(0, 11):
            n = 3 * r + 1
            out = Outcome(f'{n} {n + 1} {n + 3} {n + 4}', 8)
            wheel.add_outcome(n, out)
            wheel.add_outcome(n + 1, out)
            wheel.add_outcome(n + 3, out)
            wheel.add_outcome(n + 4, out)

            n += 1
            out = Outcome(f'{n} {n + 1} {n + 3} {n + 4}', 8)
            wheel.add_outcome(n, out)
            wheel.add_outcome(n + 1, out)
            wheel.add_outcome(n + 3, out)
            wheel.add_outcome(n + 4, out)

    def generate_line_bets(self, wheel):
        for r in range(0, 11):
            n = 3 * r + 1
            line_out = Outcome(f'{n} {n+1} {n+2} {n+3} {n+4} {n+5}', 5)
            wheel.add_outcome(n, line_out)
            wheel.add_outcome(n + 1, line_out)
            wheel.add_outcome(n + 2, line_out)
            wheel.add_outcome(n + 3, line_out)
            wheel.add_outcome(n + 4, line_out)
            wheel.add_outcome(n + 5, line_out)

    def generate_dozen_bets(self, wheel):
        doz_one = Outcome(f'Dozen 1', 2)
        doz_two = Outcome(f'Dozen 2', 2)
        doz_thr = Outcome(f'Dozen 3', 2)
        out_map = {1: doz_one, 2: doz_two, 3: doz_thr}

        for d in range(0, 3):
            out = out_map[d+1]
            m = 12 * d + 1
            for n in range(0, 12):
                wheel.add_outcome(n+m, out)

    def generate_column_bets(self, wheel):
        col_one = Outcome(f'Column 1', 2)
        col_two = Outcome(f'Column 2', 2)
        col_thr = Outcome(f'Column 3', 2)
        out_map = {1: col_one, 2: col_two, 3: col_thr}

        for c in range(0, 3):

            for r in range(0, 12):
                wheel.add_outcome(3*r + c + 1, out_map[c+1])

    def generate_even_money_bets(self, wheel):
        # Red-Black
        reds = {1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36}
        blacks = set(range(1, 37)) - reds
        red_out = Outcome('Red', 1)
        black_out = Outcome('Black', 1)

        #Even-Odd
        even_out = Outcome('Even', 1)
        odd_out = Outcome('Odd', 1)

        # Hi - Lo
        hi_out = Outcome('High', 1)
        lo_out = Outcome('Low', 1)

        for n in range(1, 37):
            if n < 19: wheel.add_outcome(n, lo_out)
            else: wheel.add_outcome(n, hi_out)

            if n % 2 == 0: wheel.add_outcome(n, even_out)
            else: wheel.add_outcome(n, odd_out)

            if n in reds: wheel.add_outcome(n, red_out)
            else: wheel.add_outcome(n, black_out)

    def build_bins(self, wheel):
        self.generate_straight_bets(wheel)
        self.generate_split_bets(wheel)
        self.generate_street_bets(wheel)
        self.generate_corner_bets(wheel)
        self.generate_line_bets(wheel)
        self.generate_dozen_bets(wheel)
        self.generate_column_bets(wheel)
        self.generate_even_money_bets(wheel)

