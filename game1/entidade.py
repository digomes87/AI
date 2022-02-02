import random
from enumeration import Status, Entity, Action, CardinalDirection
from movimento import turn, move_forward

class Room:

    def __init__(self, wumpus=Status.Absent, pit=Status.Absent, gold=Status.Absent):
        self.wumpus = wumpus
        self.pit = pit
        self.gold = gold

    def __repr__(self):
        return str([self.wumpus.value, self.pit.value, self.gold.value])

    def is_safe(self, danger=None):
        if danger is None:
            return self.wumpus == Status.Absent and self.pit == Status.Absent
        if danger == Entity.Wumpus:
            return self.wumpus == Status.Absent
        if danger == Entity.pit:
            return self.pit == Status.Absent
        raise ValueError

    def is_unsafe(self, danger=None):
        return self.is_dagerous(danger) or self.is_deadly(danger)

    def is_dangerous(self, danger=None):

        if danger is None:
            return self.wumpus == Status.LikelyPresent or self.pit == Status.LikelyPresent
        if danger ==  Entity.Wumpus:
            return self.wumpus == Status.LikelyPresent
        if danger == Entity.Pit:
            return self.pit == Status.LikelyPresent
        raise ValueError

    def is_deadly(self, danger=None):
