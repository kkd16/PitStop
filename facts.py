import random

def getFact(fname):
	lines = open(fname).read().splitlines()
	# print(lines)
	return random.choice(lines)