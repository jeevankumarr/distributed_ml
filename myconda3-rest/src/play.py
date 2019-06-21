from roulette import Game, Passenger57, PlayerEven, Table, Wheel, BinBuilder

if __name__ == '__main__':
    TABLE_MIN = 10
    table = Table(500, TABLE_MIN)
    wheel = Wheel()
    BinBuilder().build_bins(wheel)
    game = Game(wheel, table)
    playr = PlayerEven()
    playr.wallet = 10000
    round = 1

    while playr.is_playing() and playr.get_wallet() > TABLE_MIN:
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print(f'Round {round}: player wallet is {playr.get_wallet()}')
        game.cycle(playr)
        round += 1
        table.clear_bets()


    if playr.is_playing() is False:
        print(f"Thanks for playing: player final wallet is {playr.get_wallet()} {playr.is_playing()}")
    else:
        print(f"GAME OVER: player final wallet is {playr.get_wallet()} {playr.is_playing()}")
