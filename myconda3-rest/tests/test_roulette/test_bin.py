from .context import roulette
from roulette import Bin
from roulette import Outcome


def test_bin():
    five = Outcome("00-0-1-2-3", 6)
    zero_out = Outcome("0", 35)
    zerozero_out = Outcome("00", 35)

    zero_bin = Bin([zero_out, five])
    zerozero_bin = Bin([zerozero_out, five])

    assert len(zero_bin) == 2
    assert five in zero_bin
    assert zero_out in zero_bin


    assert len(zerozero_bin) == 2
    assert five in zero_bin
    assert zerozero_out in zerozero_bin


