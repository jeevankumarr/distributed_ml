"""

Five basic containers:
    1. Immutable Sequence (tuple)
    2. Mutable Sequence (list)
    3. Mutable Mapping (dict)
    4. Mutable Set(set)
    5. Immutable Set (frozenset)

Wrap vs. Extend:
    1. Wrap requires re-implemetation of wrapped class's methods
    2. Extend requires overidding of specific functions or additions

There are two reasons for introducingBinas a separate class:
    1. to improve the fidelity of our object modelof the problem, and to reduce the complexity of the Wheel class. The definition of the game describesthe wheel as having 38 bins, each bin causes a number of individual Outcomes to win. Without thinking too deeply, we opted to define the Bin class to hold a collection of Outcomes. At the present time, we can’t foresee a lot of processing that is the responsibility of a Bin. But, allocating a class permits us some flexibility in assigning responsibilities there in the future.
    2. Additionally, looking forward, it is clear that the Wheel class will use a random number generator and will pick a winning Bin. In order to keep this crisp definition of responsibilities for the Wheel class, it makes sense to delegate all of the remaining details to another class.

Why extend a built-in data structure? Why not simply use it?There are two reasons for extending a built-in data structure:
    1. We can easily add methods by extending. In the case of aBin, there isn’t much we want to add.
    2. We can easily change the underlying data structure by extending. For example, we might have adifferent set-like collection that also inherits fromCollections.abc.Set. We can make thischange in just one place – our class extension – and the entire application benefits from the alternativeset implementation.
"""

class Bin(frozenset):
    pass
