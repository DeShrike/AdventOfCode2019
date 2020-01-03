import math
import re

inputfile = "input-day22.txt"
inputdata = []
deck = []
decksize = 10007		# identical after 5003
decksize = 5003			# identical after 5002
decksize = 4001			# identical after 4000
decksize = 10009		# identical after 10008
decksize = 10037		# identical after 10036

DEAL_INTO_NEW_STACK = 1
CUT_N_CARDS = 2
DEAL_WITH_INCREMENT = 3

#########################################
#########################################

def ReadInput():
	file = open(inputfile, "r") 
	for line in file:
		inputdata.append(line.rstrip("\n"))
	file.close()

#########################################
#########################################

def ParseCommand(cmd):
	if cmd == "deal into new stack":
		return (DEAL_INTO_NEW_STACK, 0)
	
	rx2 = re.compile("cut (?P<n>[0-9\-]*)")
	match = rx2.search(cmd)
	if match:
		n = match["n"]
		return (CUT_N_CARDS, int(n))

	rx3 = re.compile("deal with increment (?P<n>[0-9\-]*)")
	match = rx3.search(cmd)
	if match:
		n = match["n"]
		return (DEAL_WITH_INCREMENT, int(n))

	return None

#########################################
#########################################

def LoadTestData1():
	global decksize
	inputdata.clear()
	inputdata.append("deal with increment 7")
	inputdata.append("deal into new stack")
	inputdata.append("deal into new stack")
	# Result: 0 3 6 9 2 5 8 1 4 7
	decksize = 10

def LoadTestData2():
	global decksize
	inputdata.clear()
	inputdata.append("cut 6")
	inputdata.append("deal with increment 7")
	inputdata.append("deal into new stack")
	# Result: 3 0 7 4 1 8 5 2 9 6
	decksize = 10

def LoadTestData3():
	global decksize
	inputdata.clear()
	inputdata.append("deal with increment 7")
	inputdata.append("deal with increment 9")
	inputdata.append("cut -2")
	# Result: 6 3 0 7 4 1 8 5 2 9
	decksize = 10

def LoadTestData4():
	global decksize
	inputdata.clear()
	inputdata.append("deal into new stack")
	inputdata.append("cut -2")
	inputdata.append("deal with increment 7")
	inputdata.append("cut 8")
	inputdata.append("cut -4")
	inputdata.append("deal with increment 7")
	inputdata.append("cut 3")
	inputdata.append("deal with increment 9")
	inputdata.append("deal with increment 3")
	inputdata.append("cut -1")
	decksize = 10
	# Result: 9 2 5 8 1 4 7 0 3 6	

#########################################
#########################################

def CutCardsNegative(n):
	global deck
	# print("==========")
	# print(f"CUT -{n}")

	# print("STart")
	# print(deck)
	l = len(deck)
	part = deck[-n:]
	deck = part + deck[0:l - n]
	# print(part)
	# print(deck)

#########################################
#########################################

def CutCardsPositive(n):
	global deck
	# print("==========")
	# print(f"CUT {n}")

	part = deck[0:n]
	deck = deck[n:] + part

#########################################
#########################################

def DealWithIncrement(n):
	global deck
	newdeck = [-1 for x in range(decksize)]
	newdeck[0] = deck[0]
	pos = 0
	opos = 1
	while opos < decksize:
		pos = (pos + n) % decksize
		# print(f"{pos}   =  {opos}")
		newdeck[pos] = deck[opos]
		opos += 1

	deck = newdeck

#########################################
#########################################

def PartA():
	global deck
	print("Part A")

	# LoadTestData1()
	# LoadTestData2()
	# LoadTestData3()
	# LoadTestData4()

	deck = [x for x in range(decksize)]

	for cmd in inputdata:
		shuffle, n = ParseCommand(cmd)
		print(f"[{cmd}] = {shuffle}  N: {n}")
		if shuffle == DEAL_INTO_NEW_STACK:
			deck.reverse()
		elif shuffle == CUT_N_CARDS:
			if n < 0:
				CutCardsNegative(abs(n))
			else:
				CutCardsPositive(n)
		elif shuffle == DEAL_WITH_INCREMENT:
			DealWithIncrement(n)
		else:
			print("UNKNOWN COMMAND")
		# input("press...")
	# print(deck)

	print(f"Lengte: {len(deck)}")
	if -1 in deck:
		print("ERROR")

	answer = deck.index(2019)
	# poging 1: 2453: too low
	# poging 2: 8380: too high
	# poging 3: 5271: too low
	# poging 4: 7665: Correct

	print("Answer:", answer)

#########################################
#########################################

def PartB():
	global deck
	print("Part B")

	deck = [x for x in range(decksize)]
	firstdeck = None
	for xx in range(20000):
		for cmd in inputdata:
			shuffle, n = ParseCommand(cmd)
			print(f"[{cmd}] = {shuffle}  N: {n}")
			if shuffle == DEAL_INTO_NEW_STACK:
				deck.reverse()
			elif shuffle == CUT_N_CARDS:
				if n < 0:
					CutCardsNegative(abs(n))
				else:
					CutCardsPositive(n)
			elif shuffle == DEAL_WITH_INCREMENT:
				DealWithIncrement(n)
			else:
				print("UNKNOWN COMMAND")
		if xx == 0:
			firstdeck = [x for x in deck]
		else:
			if firstdeck == deck:
				print("Identical %d" % xx)
				break
	print("Answer:", 0)

#########################################
#########################################

if __name__ == "__main__":
	print("Day 22")
	ReadInput()
	# PartA()
	PartB()
