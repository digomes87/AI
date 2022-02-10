import random

from enumeration import Status, Entity, Action, Goal
from movimento import neighbors, spins, know_path, path_to_spins


def perceive(kb, loc):
    if kb[loc].pit == Status.Present or kb[loc].wumpus == Status.Present:
        return None

    # construindo percepcao dos inimigos
    wumpus, pit, gold = (Status.Absent,) * 3

    # buscar nas celulas vizinhas
    for room in [kb[l] for l in neighbors(loc)]:

        if room.wumpus == Status.Present:
            wumpus = Status.Present
        elif room.wumpus == Status.LikelyPresent and wumpus != wumpus.Present:
            wumpus = Status.LikelyPresent

        # verificar se existe burracos na sala
        if room.pit == Status.Present:
            pit = Status.Present
        elif room.pit == Status.LikelyPresent and pit != Status.Present:
            pit = Status.LikelyPresent

        # verificando se há ouro na sala
        if kb[loc].gold == Status.Present:
            gold = Status.Present

        return wumpus, pit, gold


def tell(kb, perceptions, loc):
    kb[loc].wumpus = kb[loc].pit = Status.Absent
    wumpus, pit, gold = perceptions
    near = [kb[l] for l in neighbors(loc)]

    # iterar sobre salas vizinhas
    for room in (r for r in near if not r.is_safe()):
        if room.wumpus != Status.Absent:
            if wumpus == Status.Absent:
                room.wumpus = Status.Absent
            elif wumpus == Status.LikelyPresent:

                # verificar se este é o unico local onde o wumpus esta
                if len([r for r in near if
                        r.is_dangerous[Entity.Wumpus]]) == 1:
                    room.wumpus = Status.Present
            elif room.wumpus == Status.Unknown:
                if any(r.is_deadly(Entity.Wumpus) for r in near):

                    # o agente sabe o local wumpus
                    room.wumpus = Status.Absent
                elif all(r.is_safe(Entity.Wumpus) for r in near if r != room):
                    # todos os outros vizinhos nao sao seguros
                    room.wumpus = Status.Present
                else:
                    room.wumpus = Status.LikelyPresent

        # analisar a percepcao dos burrascos
        if room.pit != Status.Absent:
            if pit == Status.Absent:
                room.pit = Status.Absent
            elif pit == Status.LikelyPresent:

                # verifica se este é o unico lugar o o burrado pode estar
                if len([r for r in near if
                        r.is_dangerous(Entity.Pit)]) == 1:
                    room.pit = Status.Present
            elif room.pit == Status.Unknown:
                if all(r.is_safe(Entity.Pit) for r in near if r != room):
                    room.pit = Status.Present
                else:
                    room.pit = Status.LikelyPresent
    kb[loc].gold = gold


def update(kb, loc):
    for l in [x for x in kb.explored]:
        tell(kb, perceive(kb, l), l)


def ask(kb, loc, direction, goal):
    if goal == Goal.SeekGold:
        if kb[loc].gold == Status.Present:
            return Action.Grab, None

        state = lambda r: r.is_safe() and r.is_unexplored
        dest = next((l for l in neighbors(loc) if state(kb[l])), None)
        if dest:
            return Action.Move, (spins(loc, direction, dest),)

        # obtem espaço seguro
        state = lambda r, l: r.is_safe() and any(
            kb[x].is_explored for x in neighbors(l))
        dest = next((l for l in kb.unexplored if state(kb[l], l)), None)
        if dest:
            path = know_path(kb, loc, dest)
            return Action.Move, path_to_spins(path, direction)

        # obtem uma sala vizinha
        state = lambda r: r.is_safe(Entity.Pit) and r.is_unsafe(Entity.Wumpus)
        dest = next((l for l in neighbors(loc) if state(kb[l])), None)
        if dest:
            return Action.Shoot, spins(loc, direction, dest)

        # obter uma celula vizinha
        state = lambda r: r.is_safe(Entity.Pit) and r.is_unsafe(Entity.Wumpus)
        dest = next((l for l in kb.unexplored if state(kb[l])), None)
        if dest:
            dest = next((l for l in neighbors(dest) if kb[l].is_explored))
            path = know_path(kb, loc, dest)
            return Action.Move, path_to_spins(path, direction)

        # obtem um quarto vizinho com wumpus
        state = lambda r: r.is_dangerous(Entity.Wumpus)
        dest = next((l for l in neighbors(loc) if state(kb[l])), None)
        if dest:
            return Action.Shoot, spins(loc, direction, dest)

        # obtem um quarto com burraco
        rooms = [l for l in kb.unexplored if kb[l].is_dangerous(Entity.Pit)]
        if rooms:
            dest = random.choice(rooms)
            path = know_path(kb, loc, dest)
            return Action.Move, path_to_spins(path, direction)

        # celucal inexplorada
        dest = next((l for l in kb.unexplored), None)
        if dest:
            path = know_path(kb, loc, dest)
            return Action.Move, path_to_spins(path, direction)
    elif goal == Goal.BackToEntry:

        path = know_path(kb, loc, (0, 0))
        return Action.Move, path_to_spins(path, direction)
