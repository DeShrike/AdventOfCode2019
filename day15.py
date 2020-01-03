import math
import os
import random
from IntComputer import *
from FloodFill import *
from AStar import *

inputfile = "input-day15.txt"
inputdata = []


# inputs
NORTH = 1
SOUTH = 2
WEST = 3
EAST = 4
deltas = [[0, 0],[0, -1],[0, 1], [-1, 0], [1, 0]]

# outputs
WALL = 0
STEPTAKEN = 1
ARRIVED = 2

# grid parts
UNKNOWN = -1
EMPTY = 1
OSYSTEM = 2
OXYGEN = 3

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

gridsizex = 48
gridsizey = 44
grid = []
posx = 0
posy = 0
direction = 0
history = []
osystemx = -1
osystemy = -1
popped = False
dostep = False

def InitGrid():
	grid.clear()
	for y in range(0, gridsizey):
		grid.append([-1 for x in range(0, gridsizex)])

def PrintInfo():
	print("POSITION: %d, %d   OSYSTEM: %d, %d" % (posx, posy, osystemx, osystemy))
	print("HISTORY: ", end = "")
	# print(history)

def PrintGrid(cx, cy):
	os.system("cls")

	width = 80
	height = 22

	vanx = max(int(cx - width / 2), 0)
	vany = max(int(cy - height / 2), 0)

	totx = min(vanx + width, gridsizex - 1)
	toty = min(vany + height, gridsizey - 1)

	for y in range(vany, toty):
		for x in range(vanx, totx):
			char = grid[y][x]
			if char == UNKNOWN:
				print(".", end = "")
			elif char == WALL:
				print("#", end = "")
			elif char == OXYGEN:
				print("o", end = "")
			elif char == EMPTY:
				if x == posx and y == posy:
					print("R", end = "")
				else:
					print(" ", end = "")
			elif char == OSYSTEM:
				print("O", end = "")
		print("")

#########################################
#########################################

def OnOutput(output, ix):
	global posx
	global posy
	global osystemx
	global osystemy
	global dostep
	if output == WALL:
		# print("WALL")
		SetCell(posx, posy, direction, WALL)
	elif output == STEPTAKEN:
		# print("CLEAR")
		SetCell(posx, posy, direction, EMPTY)
		Move(posx, posy, direction)
	elif output == ARRIVED:
		# print("OSYSTEM")
		SetCell(posx, posy, direction, OSYSTEM)
		Move(posx, posy, direction)
		osystemx = posx
		osystemy = posy

	# PrintGrid(posx, posy)
	# PrintInfo()
	# if dostep:
	# 	a = input("Press...")
	# 	if a == "R":
	# 		dostep = False

def Move(x, y, direction):
	global posx
	global posy
	global popped
	global dostep
	newx = x + deltas[direction][0]
	newy = y + deltas[direction][1]
	if newx < 0 or newx >= gridsizex or newy < 0 or newy >= gridsizey:
		print("GRID TOO SMALL (A)")
		return
	posx = newx
	posy = newy

	if posx == gridsizex / 2 and posy == gridsizey / 2:
		dostep = True

	if not popped:
		history.append(direction)
	popped = False

def SetCell(x, y, direction, value):
	newx = x + deltas[direction][0]
	newy = y + deltas[direction][1]
	if newx < 0 or newx >= gridsizex or newy < 0 or newy >= gridsizey:
		print("GRID TOO SMALL (B)")
		return
	grid[newy][newx] = value

def FindCellType(x, y, direction):
	newx = x + deltas[direction][0]
	newy = y + deltas[direction][1]
	if newx < 0 or newx >= gridsizex or newy < 0 or newy >= gridsizey:
		print("GRID TOO SMALL (C)")
		return None
	return grid[newy][newx]

def ReverseDir(direction):
	if direction == NORTH:
		return SOUTH
	if direction == SOUTH:
		return NORTH
	if direction == EAST:
		return WEST
	if direction == WEST:
		return EAST

def DetermineDirection():
	global popped
	global dostep
	dirs = []
	cell = FindCellType(posx, posy, NORTH)
	if cell == UNKNOWN: # or cell == EMPTY:
		dirs.append(NORTH)
	cell = FindCellType(posx, posy, SOUTH)
	if cell == UNKNOWN: # or cell == EMPTY:
		dirs.append(SOUTH)
	cell = FindCellType(posx, posy, EAST)
	if cell == UNKNOWN: # or cell == EMPTY:
		dirs.append(EAST)
	cell = FindCellType(posx, posy, WEST)
	if cell == UNKNOWN: # or cell == EMPTY:
		dirs.append(WEST)

	# print("POSSIBLE DIRECTIONS: ", end = "")
	# print(dirs)

	if len(dirs) == 0:
		popped = True
		dostep = True
		if len(history) == 0:
			return None
		return ReverseDir(history.pop())

	r = random.randint(0, len(dirs) - 1)
	return dirs[r]

def BuildMap():
	global posx
	global posy
	global direction

	posx = int(gridsizex / 2)
	posy = int(gridsizey / 2)
	direction = NORTH

	InitGrid()
	grid[posy][posx] = UNKNOWN

	game = IntComputer(inputdata, OnOutput, "Robot")
	game.run([])

	while True:
		direction = DetermineDirection()
		# if direction == NORTH:
		# 	print("NORTH")
		# elif direction == SOUTH:
		# 	print("SOUTH")
		# elif direction == EAST:
		# 	print("EAST")
		# elif direction == WEST:
		# 	print("WEST")
		if direction == None:
			break
		game.run([direction])

		if game.finished:
			break

	print("Map Created")

def PartA():

	print("Part A")

	BuildMap()

	start = (int(gridsizex / 2), int(gridsizey / 2))
	end = (osystemx, osystemy)

	maze = []
	for y in range(0, gridsizey):
		mline = []
		row = grid[y]
		for pos in row:
			if pos == WALL:
				mline.append(10000)
			else:
				mline.append(0)
		maze.append(mline)

	astar = AStar(maze)
	path = astar.run([start[0], start[1]], [end[0], end[1]])

	for s in path:
		xx = s[0]
		yy = s[1]
		cur = maze[yy][xx]
		if cur == 0:
			maze[yy][xx] = "P"
		else:
			maze[yy][xx] = "W"

	for y, mrow in enumerate(maze):
		for x, mcol in enumerate(mrow):
			if x == start[0] and y == start[1]:
				print("S", end = "")
			elif x == end[0] and y == end[1]:
				print("E", end = "")
			elif mcol == "P":
				print("O", end = "")
			else:
				print("." if mcol > 0 else " ", end = "")
		print("")

	# print(path)

	print("Answer:", len(path) - 1)

#########################################
#########################################

def StepCb(x, y):
	# PrintGrid(gridsizex / 2, gridsizey / 2)
	# input("Press...")
	pass
	
def PartB():
	print("Part B")

	BuildMap()

	grid[osystemy][osystemx] = EMPTY

	ff = FloodFill(grid, StepCb)
	ff.Run2(osystemx, osystemy, EMPTY, OXYGEN)
	
	print("Answer:", ff.steps)

#########################################
#########################################

if __name__ == "__main__":
	print("Day 15")
	ReadInput()
	PartA()
	PartB()
