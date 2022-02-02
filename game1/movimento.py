# Objetivo Delta criado para mover o agente e alcançår seus vizinhos
DELTA = (0, -1), (1, 0), (0, 1), (-1, 0)

def neighbors(location, size=(4, 4)):

	x, y = location
	width, height = size

	# celula acima
	if y - 1 >= 0:
		yield x, y - 1

	# celulca a direita
	if x + 1 < width:
		yield x + 1, y

	# celula abaixo
	if y + 1 < height:
		yield x, y + 1

	# celulca a esquerda
	if x - 1 >= 0:
		yield x - 1, y


def neighbor(location, direction, size=(4, 4)):

	x, y = location
	width, height = size
	dx, dy = DELTA[direction]

	# verifica se o vizinho está dentro da caverna
	if 0 <= x + dx < width and 0 <= y + dy < height:
		return x + dx, y + dy


def turn(direction, steps):
	return (direction + steps) % len(DELTA)

def move_forward(location, direction):
	return neighbor(location, direction)

def spins(source, direction, destination):
	assert source in neighbors(destination)

	# calcule a diferenca entre os locais
	diff = tuple([a - b for a, b in zip(destination, source)])
	rot = DELTA.index(diff) - direction
	rot = rot if rot != 3 else -1

	# retorna o numero minimo de rotacao
	return rot

def known_path_rec(kb, loc, dest, path, visited):

	if loc == desc:
		return True

	# gerador de vizinhos exploradados
	neighborhood = {l for l in neighbors(loc) if l not in visited
					and (kb[l].is_explored or l == dest)}

	#iterar sobre cada vizinho
	for n in neighborhood:
		path.append(n)
		visited.add(n)

		# chamada recusiva
		if known_path_rec(kb, n, dest, path, visited):
			return True

		# Bactrack este no nao conduz ao destino
		visited.remove(n)
		path.remove(n)
	return False

def know_path(kb, loc, dest):
	path = [loc]
	visited = set()
	visited.add(loc)


	#retorna o cambio ou nenhum se o caminho nao foi encontrado
	if known_path_rec(kb, loc, dest, path, visited):
		return tuple(path)

def path_to_spins(path, direction):
	assert path is not None
	rotations = []

	i = 0
	while i < len(path) - 1:
		rot = spins(path[i], direction, path[i + 1])
		rotations.append(rot)
		direction = (direction + rot) % len(DELTA)
		i += 1
	return tuple(rotations)