# Score categories.
# Change the values as you see fit.
from secrets import choice


YACHT = lambda dice: 50 if sorted(dice)[0] == sorted(dice)[4] else 0
ONES = lambda dice: dice.count(1)
TWOS = lambda dice: 2*dice.count(2)
THREES = lambda dice: 3*dice.count(3)
FOURS = lambda dice: 4*dice.count(4)
FIVES = lambda dice: 5*dice.count(5)
SIXES = lambda dice: 6*dice.count(6)
FULL_HOUSE = lambda dice: sum(dice) if set(dice.count(y) for y in dice) == {2,3} else 0
FOUR_OF_A_KIND = lambda dice: 4*sum(set(i for i in dice if dice.count(i) >= 4))
LITTLE_STRAIGHT = lambda dice: 30 if sorted(dice) == [1,2,3,4,5] else 0
BIG_STRAIGHT = lambda dice: 30 if sorted(dice) == [2,3,4,5,6] else 0
CHOICE = lambda dice: sum(dice)

def score(dice, category):
    return category(dice)
