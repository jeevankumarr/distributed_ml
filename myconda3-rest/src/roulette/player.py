import abc
from .wheel import Wheel
from .table import Table
from .bet import Bet

class Player(abc.ABC):
    def __init__(self):
        pass
    @abc.abstractmethod
    def place_bets(self, table: Table, wheel: Wheel):
        raise NotImplementedError

    @abc.abstractmethod
    def is_playing(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_wallet(self):
        raise NotImplementedError

    @abc.abstractmethod
    def win(self, bet: Bet):
        raise NotImplementedError


class Passenger57(Player):
    def __init__(self):
        super().__init__()
        self.bets = []


    def place_bets(self, table: Table, wheel: Wheel):
        black = wheel.get_outcome('Black')
        black_bet = Bet(10, black)
        table.place_bet(black_bet)

        self.bets.append(black_bet)


class PlayerEven(Player):
    def __init__(self):
        super().__init__()
        self.bets = []
        self.wallet = 0
        self.rounds = 10
        self.active = True

    def place_bets(self, table: Table, wheel: Wheel) -> None:
        """Places bets on the table,
            - looks up outcomes from the wheel
            - creates bet(s) with the chosen outcome and bet amount
            - places the bet(s) on the table

        Args:
            table (Table): current table being played
            wheel (Wheel): current wheel being played

        Returns:
            None
        """
        black = wheel.get_outcome('Even')
        black_bet = None

        if self.wallet >= 10:
            black_bet = Bet(10, black)
            self.wallet -= 10

            table.place_bet(black_bet)

            self.bets.append(black_bet)
        else:
            self.active = False

    def is_playing(self) -> bool:
        """Notifies is a player is playing

        Returns:
            bool: whether this player is playing the game
        """

        # if self.rounds > 0 and self.active is True:
        #     self.rounds -= 1
        #     return True
        # else:
        #     return False
        return True

    def win(self, bet: Bet):
        self.wallet += bet.win_amount()

    def lose(self, bet: Bet):
        pass

    def get_wallet(self):
        return self.wallet