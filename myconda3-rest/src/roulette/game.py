from .wheel import Wheel, BinBuilder
from .table import Table
from .player import Player, Passenger57

class Game():
    def __init__(self, wheel, table):
        self.wheel = wheel
        self.table = table


    def cycle(self, player: Player):


        # Place Bets
        # a. Notify Player to create bets
        if player.is_playing():
            player.place_bets(self.table, self.wheel)
            # b. Reduce Player stake as part of creating a Bet

            # spin wheel
            # 1. Get the winning bin
            bin_name, bin = self.wheel.next()
            # print(bin_name, bin)
            # 2. Collect the winning outcomes

            for i, b in enumerate(self.table):
                print(f'    > bet {i} {b} {b.outcome}')
                if b.outcome in bin:
                    print(f"Roulette spun {bin_name if bin_name <37 else '00'} WIN WIN WIN", b.amount, b.win_amount())
                    player.win(b)
                else:
                    print(f"Roulette spun {bin_name if bin_name <37 else '00'} Better Luck Next time")
            # resolve all bets
            # 1. for each bet b placed by player:
            #   a. Winner: Notify player and update player stake
            #   b. Loser: Notify Player that Bet b was a loser
        else:
            print(f"Game Over {player.get_wallet()}")


