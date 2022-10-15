import random

file = open("facts.txt")

def randnum(fname):
	lines = open(fname).read().splitlines()
	# print(lines)
	return random.choice(lines)

print(randnum('facts.txt'))