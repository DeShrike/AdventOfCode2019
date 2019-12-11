import math
from IntComputer import *

inputfile = "input-day11.txt"
inputdata = []
grid = []

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

gridsizex = 0
gridsizey = 0
startx = 0
starty = 0

BLACK = 0
WHITE = 1
LEFT = 0
RIGHT = 1
deltaix = 0
deltas = [(0, -1), (-1, 0), (0, 1), (1, 0)]

def InitGrid():
	grid.clear()
	for y in range(0, gridsizey):
		grid.append([-1 for x in range(0, gridsizex)])
	# print(grid)

#########################################
#########################################

def RunRobot(startColor):
	global deltaix

	minx = 100000
	maxx = 0
	miny = 100000
	maxy = 0

	deltaix = 0

	InitGrid()
	
	posx = startx
	posy = starty

	grid[posy][posx] = startColor

	computer = IntComputer(inputdata)
	color = grid[posy][posx]
	if color == -1:
		color = BLACK
	computer.run([color])
	while True:
		if computer.finished:
			break

		o1 = computer.outputs[-2]
		o2 = computer.outputs[-1]
		# print(o1)
		# print(o2)
		# input("Press...")
		if o1 == BLACK:
			grid[posy][posx] = BLACK
		elif o1 == WHITE:
			grid[posy][posx] = WHITE

		if o2 == LEFT:
			deltaix = (deltaix + 1) % 4
		elif o2 == RIGHT:
			deltaix = (deltaix - 1) % 4
		
		dx = deltas[deltaix][0]
		dy = deltas[deltaix][1]
		posx += dx
		posy += dy

		if posx < minx:
			minx = posx

		if posy < miny:
			miny = posy

		if posx > maxx:
			maxx = posx

		if posy > maxy:
			maxy = posy

		print("POS: %d,%d" % (posx, posy), end = "\r")

		color = grid[posy][posx]
		if color == -1:
			color = BLACK

		computer.run([color])

	# print("X: %d - %d = %d" % (minx, maxx, maxx - minx))
	# print("Y: %d - %d = %d" % (miny, maxy, maxy - miny))

#########################################
#########################################

def PartA():
	global gridsizex
	global gridsizey
	global startx
	global starty

	print("Part A")

	gridsizex = 90
	gridsizey = 60
	startx = 75
	starty = 30

	RunRobot(BLACK)

	print("")
	print("Counting")
	count = 0

	for x in range(gridsizex):
		for y in range(gridsizey):
			c = grid[y][x]
			if c == WHITE or c == BLACK:
				count += 1

	print("Answer:", count)

#########################################
#########################################

def PartB():
	global gridsizex
	global gridsizey
	global startx
	global starty

	print("Part B")

	gridsizex = 70
	gridsizey = 8
	startx = 1
	starty = 1

	RunRobot(WHITE)

	print("")
	print("Answer:")

	for row in grid:
		for col in row:
			if col == -1:
				print(" ", end = "")
			elif col == 1:
				print("#", end = "")
			else:
				print(".", end = "")
		print("")


#########################################
#########################################

if __name__ == "__main__":
	print("Day 11")
	ReadInput()
	PartA()
	PartB()
