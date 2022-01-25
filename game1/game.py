import sys
import random

from enumeration import Goal, Status, Action
from entidade import Room, Agent, Knowledge, Cave
from conhecimento


def print_intro():
	print('\n')
	print('**************************')
	print('Caça ao Wumpus')
	print('Inteligência Artificial em Ação')
	print('**************************')
	print('\n')


def print_actions():
	print('1) Mover para frente')
	print('2) Virar a esquerda')
	print('3) Virar a direita')
	print('4) Pegar')
	print('5) Atirar')


def print_perceptions(perceptions):
	wumpus, pit, gold = perceptions
	if wumpus == Status.Present:
		print('Você oercebeu um stench')
	if pit == Status.Present:
		print('Você percebeu uma Brisa')
	if gold == Status.Present:
		print('Você percebeu um brilho')
	if perceptions == (Status.Absent,) * 3:
		print('Sem percepções')
	print()

def parse_action

