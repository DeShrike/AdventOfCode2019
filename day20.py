import math
import itertools
import os

inputfile = "input-day20.txt"
inputdata = []
grid = []
gridsizex = 0
gridsizey = 0

portals = {}	# key = Name, Value = (x1, y1, x2, y2)

WALL = ord("#")
SPACE = ord(".")
VOID = ord(" ")
WARP = ord("W")

deltas = [[0, 1], [0, -1], [1, 0], [-1, 0]]

#########################################
#########################################

def ReadInput():
	file = open(inputfile, "r") 
	for line in file:
		inputdata.append(line.rsplit("\n"))
	file.close()

#########################################
#########################################

def LoadTest1():
	inputdata.clear()
	inputdata.append("         A           ")
	inputdata.append("         A           ")
	inputdata.append("  #######.#########  ")
	inputdata.append("  #######.........#  ")
	inputdata.append("  #######.#######.#  ")
	inputdata.append("  #######.#######.#  ")
	inputdata.append("  #######.#######.#  ")
	inputdata.append("  #####  B    ###.#  ")
	inputdata.append("BC...##  C    ###.#  ")
	inputdata.append("  ##.##       ###.#  ")
	inputdata.append("  ##...DE  F  ###.#  ")
	inputdata.append("  #####    G  ###.#  ")
	inputdata.append("  #########.#####.#  ")
	inputdata.append("DE..#######...###.#  ")
	inputdata.append("  #.#########.###.#  ")
	inputdata.append("FG..#########.....#  ")
	inputdata.append("  ###########.#####  ")
	inputdata.append("             Z       ")
	inputdata.append("             Z       ")
	# Answer : 23

def LoadTest2():
	inputdata.clear()
	inputdata.append("                   A               ")
	inputdata.append("                   A               ")
	inputdata.append("  #################.#############  ")
	inputdata.append("  #.#...#...................#.#.#  ")
	inputdata.append("  #.#.#.###.###.###.#########.#.#  ")
	inputdata.append("  #.#.#.......#...#.....#.#.#...#  ")
	inputdata.append("  #.#########.###.#####.#.#.###.#  ")
	inputdata.append("  #.............#.#.....#.......#  ")
	inputdata.append("  ###.###########.###.#####.#.#.#  ")
	inputdata.append("  #.....#        A   C    #.#.#.#  ")
	inputdata.append("  #######        S   P    #####.#  ")
	inputdata.append("  #.#...#                 #......VT")
	inputdata.append("  #.#.#.#                 #.#####  ")
	inputdata.append("  #...#.#               YN....#.#  ")
	inputdata.append("  #.###.#                 #####.#  ")
	inputdata.append("DI....#.#                 #.....#  ")
	inputdata.append("  #####.#                 #.###.#  ")
	inputdata.append("ZZ......#               QG....#..AS")
	inputdata.append("  ###.###                 #######  ")
	inputdata.append("JO..#.#.#                 #.....#  ")
	inputdata.append("  #.#.#.#                 ###.#.#  ")
	inputdata.append("  #...#..DI             BU....#..LF")
	inputdata.append("  #####.#                 #.#####  ")
	inputdata.append("YN......#               VT..#....QG")
	inputdata.append("  #.###.#                 #.###.#  ")
	inputdata.append("  #.#...#                 #.....#  ")
	inputdata.append("  ###.###    J L     J    #.#.###  ")
	inputdata.append("  #.....#    O F     P    #.#...#  ")
	inputdata.append("  #.###.#####.#.#####.#####.###.#  ")
	inputdata.append("  #...#.#.#...#.....#.....#.#...#  ")
	inputdata.append("  #.#####.###.###.#.#.#########.#  ")
	inputdata.append("  #...#.#.....#...#.#.#.#.....#.#  ")
	inputdata.append("  #.###.#####.###.###.#.#.#######  ")
	inputdata.append("  #.#.........#...#.............#  ")
	inputdata.append("  #########.###.###.#############  ")
	inputdata.append("           B   J   C               ")
	inputdata.append("           U   P   P               ")
	# Answer : 58

#########################################
#########################################
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
			if char == WALL:
				print("#", end = "")
			elif char == VOID:
				print(" ", end = "")
			elif char == WARP:
				print("W", end = "")
			elif char == SPACE:
				print(".", end = "")
			else:
				print(char, end = "")
		print("")

#########################################
#########################################

def BuildGrid():
	global gridsizex
	global gridsizey

	gridsizey = len(inputdata)
	gridsizex = len(inputdata[0])

	grid.clear()
	for y in range(0, gridsizey):
		grid.append([-1 for x in range(0, gridsizex)])

	for y, line in enumerate(inputdata):
		for x, char in enumerate(line):
			if char == WALL:
				grid[y][x] = WALL
			elif char == SPACE:
				grid[y][x] = SPACE
			elif char == VOID:
				grid[y][x] = VOID
			else:
				grid[y][x] = ord(char)

def IsLetter(value):
	return value >= ord("A") and value <= ord("Z")

def GetGridValue(x, y):
	if x < 0 or y < 0:
		return None
	if x >= gridsizex or y >= gridsizey:
		return None
	return grid[y][x]

def AddPortal(name, x, y):
	if name in portals:
		portals[name][2] = x
		portals[name][3] = y
	else:
		portals[name] = [x, y, 0, 0]

def FindOtherLetter(x, y):
	for d in deltas:
		nx = x + d[0]
		ny = y + d[1]
		v = GetGridValue(nx, ny)
		if v == None:
			continue
		if IsLetter(v):
			return (nx, ny, v)
	print("Other letter not found")
	return None, None, None

def FindSpaceAround(x, y):
	for d in deltas:
		nx = x + d[0]
		ny = y + d[1]
		v = GetGridValue(nx, ny)
		if v == None:
			continue
		if v == SPACE:
			return (nx, ny)
	print("Space not found")
	return None, None

def FindPortals():
	for x1, y1 in itertools.product(range(gridsizex - 1), range(gridsizey - 1)):
		l1 = grid[y1][x1]
		if IsLetter(l1) == False:
			continue
		x2, y2, l2 = FindOtherLetter(x1, y1)
		if l2 == None:
			continue
		
		portal = chr(l1) + chr(l2)
		
		sx, sy = FindSpaceAround(x1, y1)
		if sx != None:
			grid[y1][x1] = WARP
			grid[y2][x2] = VOID
			AddPortal(portal, sx, sy)
		else:
			sx, sy = FindSpaceAround(x2, y2)
			if sx != None:
				grid[y2][x2] = WARP
				grid[y1][x1] = VOID
				AddPortal(portal, sx, sy)

		pass

#########################################
#########################################

def PartA():
	print("Part A")
	
	LoadTest1()
	# LoadTest2()

	BuildGrid()
	FindPortals()

	PrintGrid(0, 0)
	print(portals)

	print("Answer:", 0)

#########################################
#########################################

def PartB():
	print("Part B")

	print("Answer:", 0)

#########################################
#########################################

if __name__ == "__main__":
	print("Day 20")
	ReadInput()
	PartA()
	PartB()
