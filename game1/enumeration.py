import enum

class Status(enum.Enum):
    Unknown = -1
    Absent = 0
    Present = 1
    LikelyPresent = 2


class Entity(enum.Enum):
    Wumpus = 0
    Pit = 1
    Gold = 2


class Action(enum.Enum):
    Move = 0
    Shoot = 1
    Grab = 2
    Turn = 3


class Goal(enum.Enum):
    SeekGold = 0
    BackToEntry = 1

class CardinalDirection(enum.Enum):
    North = 0
    East = 1
    South = 2
    West = 3
