"""
    Nesse arquivo basicamento o que tenho são as regras dentro da sala
"""
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

        if danger is None:
            return self.wumpus == Status.Present or self.pit == Status.Present
        if danger == Entity.Wumpus:
            return self.wumpus == Status.Present
        if danger == Entity.Pit:
            return self.pit == Status.Present
        raise ValueError

    @property
    def is_explored(self):
        assert self.gold != Status.LikelyPresent
        return self.gold != Status.Unknown

    @property
    def is_unexplored(self):
        return not self.is_explored


class Agent:

    # Representacao do agente explorando
    def __init__(self):

        self.location = (0, 0)
        self.direction = 1
        self.has_gold = False
        self.has_arrow = True

    def __repr__(self):
        """
            Retorno a string dessa instancia
        """
        return str(self.location, self.direction, self.has_gold, self.has_arrow)

    def __str__(self):
        info = 'Localização: {}\n'.format(self.location)
        info += 'Direção: {}\n'.format(CardinalDirection(self.direction).name)
        info += 'Tem Ouro ? {}\n'.format(self.has_gold)
        info += 'Tem a flecha? {}'.format(self.has_arrow)
        return info

    def perform(self, action, cave, kb):
        kind, rotations = action
        if kind == Action.Move:
            self.move(rotations)
        elif kind == Action.Shoot:
            if rotations is not None:
                self.direction = turn(self.direction, rotations)
            return self.shoot(cave, kb)
        elif kind == Action.Grab:
            cave[self.location].gold = Status.Absent
            self.has_gold = True
        elif kind == Action.Turn:
            self.direction = turn(self.direction, rotations)
        return False

    def shoot(self, cave, kb):
        x, y = self.location
        width, height = cave.size

        # Retira a flecha
        self.has_arrow = False

        # Atira
        if self.direction == 0:
            i = y
            while i >= 0:
                kb[x, i].wumpus == Status.Absent
                if cave[x, i].wumpus == Status.Present:
                    cave[x, i].wumpus = Status.Present
                    kb.kill_wumpus()
                    return True
                i -= 1
        elif self.direction == 1:

            i = x
            while i < width:
                kb[i, y].wumpus = Status.Absent
                if cave[i, y].wumpus == Status.Present:
                    cave[i, y].wumpus = Status.Absent
                    kb.kill_wumpus()
                    return True
                i -= 1
        elif self.direction == 2:

            i = y
            while i < height:
                kb[x, i].wumpus == Status.Absent
                if cave[x, i].wumpus == Status.Absent:
                    cave[x, i].wumpus = Status.Absent
                    kb.kill_wumpus()
                    return True
                i += 1
        else:

            i = x
            while i >= 0:
                kb[i, y].wumpus = Status.Absent
                if cave[i, y].wumpus == Status.Present:
                    cave[i, y].wumpus = Status.Absent
                    kb.kill_wumpus()
                    return True
                i -= 1

        return False


class Knowledge:

    def __init__(self, size=(4, 4)):

        self.size = size

        w, h = self.size
        status = Status.Unknown, Status.Unknown, Status.Unknown
        self._rooms = [[Room(*status) for x in range(w)] for y in range(h)]

        # entrada segura em sem ouro
        self._rooms[0][0] = Room()

    def __repr__(self):

        width, height = self.size
        plant = ''
        y = 0
        while y < height:
            x = 0
            while x < width:
                plant += '{}\t'.format((self._rooms[y][x]))
                x += 1
            plant += '\n' if y != height - 1 else ''
            y += 1
        return plant

    def __getitem__(self, location):

        x, y = location
        return self._rooms[y][x]

    def __setitem__(self, location, value):
        x, y = location
        self._rooms[y][x] = value

    def rooms(self, condition=None):
        # gerador de indice
        y = 0
        for path in self._rooms:
            x = 0
            for room in path:
                if condition is None or condition(room):
                    yield x, y
                x += 1
            y += 1

    @property
    def explored(self):

        return self.rooms(lambda r: r.is_explored)

    @property
    def unexplored(self):
        return self.rooms(lambda r: not r.is_explored)

    def kill_wumpus(self):
        for path in self._rooms:
            for room in path:
                room.wumpus = Status.Absent


class Cave(Knowledge):

    def __init__(self, size=(4, 4)):
        self.size = size

        w, h = self.size
        self.rooms = [[Room() for x in range(w)] for y in range(h)]
        unsafe = [(x, y) for x in range(w) for y in range(h) if (x, y) != (0, 0)]

        # inserindo wumpus
        x, y = random.choice(unsafe)
        self._rooms[y][x].wumpus = Status.Present

        # inserindo ouro na caver
        x, y = random.choice(unsafe)
        self._rooms[y][x].gold = Status.Present

        # inserindo dificuldade na caverna 0,2
        for x, y in unsafe:
            if random.random() <= 0.2:
                self._rooms[y][x].pit = Status.Present