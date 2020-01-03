import math
import os
from IntComputer import *
import itertools

inputfile = "input-day17.txt"
inputdata = []
grid = []
gridsizex = 50
gridsizey = 50

SPACE = 46
WALL = 35
NEWLINE = 10
VISITED = 0x2A
UP = 0x5E	# 94v
RIGHT = 0x3E	# 62
LEFT = 0x3C	# 60
DOWN = 0x76 # 118 
# DOWN = 0x56 # 86
COMMA = 44

deltas = { UP: [0, -1], DOWN: [0, 1], LEFT: [-1, 0], RIGHT: [1, 0]}

#########################################
#########################################

def ReadInput():
	file = open(inputfile, "r") 
	for line in file:
		for part in line.split(","):
			inputdata.append(int(part))
	file.close()

#########################################
#########################################

def InitGrid():
	grid.clear()
	for y in range(0, gridsizey):
		grid.append([-1 for x in range(0, gridsizex)])

def PrintGrid(cx, cy):
	os.system("cls")

	width = 80
	height = 50

	vanx = max(int(cx - width / 2), 0)
	vany = max(int(cy - height / 2), 0)

	totx = min(vanx + width, gridsizex - 1)
	toty = min(vany + height, gridsizey - 1)

	for y in range(vany, toty):
		for x in range(vanx, totx):
			char = grid[y][x]
			if char == SPACE:
				print(".", end = "")
			elif char == WALL:
				print("#", end = "")
			elif char == UP:
				print("^", end = "")
			elif char == DOWN:
				print("V", end = "")
			elif char == LEFT:
				print("<", end = "")
			elif char == RIGHT:
				print(">", end = "")
			elif char == VISITED:
				print("*", end = "")
		print("")

#########################################
#########################################

posx = 0
posy = 0
facing = 0

def OnOutputA(value, ix):
	global posx
	global posy

	if value in [SPACE, WALL, UP, DOWN, LEFT, RIGHT]:
		grid[posy][posx] = value
		posx += 1
	elif value == NEWLINE:
		posy += 1
		posx = 0

	# PrintGrid(gridsizex / 2, gridsizey / 2)

def  TryGet(x, y):
	if x < 0 or y < 0:
		return None
	if x >= gridsizex:
		return None
	if y >= gridsizey:
		return None
	return grid[y][x]

def  TryGet2(x, y):
	if x < 0 or y < 0:
		return None
	if x >= gridsizex:
		return None
	if y >= gridsizey:
		return None
	return WALL if grid[y][x] == VISITED else grid[y][x]

def OnOutputB(value, ix):
	# print("OUTPUT: %d" % value)
	pass

def GetFacing(fa):
	delta = deltas[fa]
	return TryGet(posx + delta[0], posy + delta[1])

def GetFacing2(fa):
	delta = deltas[fa]
	return TryGet2(posx + delta[0], posy + delta[1])

def MoveFacing():
	global posx
	global posy
	delta = deltas[facing]
	posx += delta[0]
	posy += delta[1]
	grid[posy][posx] = VISITED

def FindNewDirection():
	if GetFacing(UP) == WALL:
		return UP
	if GetFacing(DOWN) == WALL:
		return DOWN
	if GetFacing(LEFT) == WALL:
		return LEFT
	if GetFacing(RIGHT) == WALL:
		return RIGHT
	return None

def GetTurnDirection(fromm, too):
	if fromm == UP:
		if too == LEFT:
			return "L"
		elif too == RIGHT:
			return "R"
	if fromm == DOWN:
		if too == LEFT:
			return "R"
		elif too == RIGHT:
			return "L"
	if fromm == LEFT:
		if too == UP:
			return "R"
		elif too == DOWN:
			return "L"
	if fromm == RIGHT:
		if too == UP:
			return "L"
		elif too == DOWN:
			return "R"
	return None	

def PrintFacing(f):
	if f == UP:
		print("UP", end = "")
	if f == DOWN:
		print("DOWN", end = "")
	if f == LEFT:
		print("LEFT", end = "")
	if f == RIGHT:
		print("RIGHT", end = "")

def BuildPath():
	global posx
	global posy
	global facing
	
	path = []

	# first find location and direction
	for x in range(gridsizex):
		for y in range(gridsizey):
			v = grid[y][x]
			if v == UP or v == DOWN or v == LEFT or v == RIGHT:
				posx = x
				posy = y
				facing = v
				break
	
	stepcount = 0	
	while True:
		p = GetFacing2(facing)
		if p == WALL:
			# print("Can go forward")
			MoveFacing()
			stepcount += 1
		else:
			newfacing = FindNewDirection()
			if newfacing == None:
				print("No new Direction found")
				path.append(stepcount)
				break
			# print("New Direction ")
			# PrintFacing(newfacing)
			turn = GetTurnDirection(facing, newfacing)
			if turn == None:
				print("No turn direction from %d to %d" % (facing, newfacing))
				break
			# print("Turning %s" % turn)
			if stepcount > 0:
				path.append(stepcount)
			stepcount = 0
			path.append(turn)
			facing = newfacing
			# input("Press")
	# input("Done")
	return path


#########################################
#########################################

def PartA():
	global posx
	global posy
	print("Part A")

	InitGrid()
	posx = 0
	posy = 0

	computer = IntComputer(inputdata, OnOutputA, "PartA")

	computer.run([])
	while True:
		if computer.finished:
			break

	alignment = 0
	for x in range(gridsizex):
		for y in range(gridsizey):
			if grid[y][x] == WALL:
				if TryGet(x + 1, y) == WALL and TryGet(x - 1, y) == WALL and TryGet(x, y - 1) == WALL and TryGet(x, y + 1) == WALL:
					alignment += x * y

	print("Answer:", alignment)

#########################################
#########################################
'''
Iterate over all the key value pairs in dictionary and call the given
callback function() on each pair. Items for which callback() returns True,
add them to the new dictionary. In the end return the new dictionary.
'''
def filterTheDict(dictObj, callback):
    newDict = dict()
    # Iterate over all the items in dictionary
    for (key, value) in dictObj.items():
        # Check if item satisfies the given condition then add to new dict
        if callback((key, value)):
            newDict[key] = value
    return newDict

kk = 10000000

def TryCombination(comb, full):
	global kk
	test = full
	a = comb[0][0]
	b = comb[1][0]
	c = comb[2][0]

	# print("---------------------------------------")
	# print(test)
	# print(" ")
	# print("A: %s" % a)
	# print("B: %s" % b)
	# print("C: %s" % c)

	test = test.replace(a, "A,")
	test = test.replace(b, "B,")
	test = test.replace(c, "C,")	

	# print(test)
	if kk > len(test):
		kk = len(test)
		# print(test)
		# input("Press")

	if "R" in test:
		return None
	if "L" in test:
		return None
	if "U" in test:
		return None
	if "D" in test:
		return None
	return test

def MakeSentences(path):
	full = ""
	for p in path:
		full = full + str(p) + ","
	# full = full.rstrip(",")
	print(full)

	s = {}
	for l in range(4, len(full) // 3 * 2):  # // 2
		for i in range(0, len(full) - 2):
			ss = full[i:l]
			if ss in s:
				s[ss] += 1
			else:
				s[ss] = 1
	
	newDict = dict(filter(lambda elem: len(elem[0]) > 3
		and elem[0][0] != ","
		and elem[0][0] in ["R","L","U","D"] 
		and elem[0][-2] not in ["R","L","U","D"] 
		and elem[0][-1] == "," 
		and elem[1] > 0, s.items()))
	# newDict = {k: v for k, v in sorted(newDict.items(), key=lambda item: len(item[0]), reverse = True)}
	# newDict = {k: v for k, v in sorted(newDict.items(), key=lambda item: item[1])}
	newDict = [[k, v] for k, v in sorted(newDict.items(), key=lambda item: len(item[0]), reverse = True)]

	solution = None

	for subset in itertools.combinations(newDict, 3):
		prog = TryCombination(subset, full)
		if prog != None:
			# print("Found It")
			# print(subset)
			# print(prog)
			solution = []
			solution.append(prog)
			solution.append(subset[0][0])
			solution.append(subset[1][0])
			solution.append(subset[2][0])
			break
	
	return solution
#########################################
#########################################

def PartB():
	global posx
	global posy
	print("Part B")

	# First build the grid (Same as in Part A)
	InitGrid()
	posx = 0
	posy = 0

	computer = IntComputer(inputdata, OnOutputA, "PartA")

	computer.run([])
	while True:
		if computer.finished:
			break

	path = BuildPath()

	# PrintGrid(0, 0)

	print("Path: ")
	print(len(path))
	print(path)

	solution = MakeSentences(path)
	if solution == None:
		print("No solution found :(")
		return
	
	print(solution)

	# Now Part B
	inputdata[0] = 2
	computer = IntComputer(inputdata, OnOutputB, "PartB")

	program = solution[0].rstrip(",")
	functiona = solution[1].rstrip(",")
	functionb = solution[2].rstrip(",")
	functionc = solution[3].rstrip(",")

	program = [ord(letter) for letter in program]
	program.append(NEWLINE)
	functiona = [ord(letter) for letter in functiona]
	functiona.append(NEWLINE)
	functionb = [ord(letter) for letter in functionb]
	functionb.append(NEWLINE)
	functionc = [ord(letter) for letter in functionc]
	functionc.append(NEWLINE)

	computer.run(program)
	computer.run(functiona)
	computer.run(functionb)
	computer.run(functionc)
	computer.run([ord("n"), NEWLINE])

	while True:
		computer.run([])
		if computer.finished:
			break

	print("Answer:", computer.lastoutput)

#########################################
#########################################

if __name__ == "__main__":
	print("Day 17")
	ReadInput()
	PartA()
	PartB()
