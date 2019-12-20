import math
import os
import itertools
from IntComputer import *

inputfile = "input-day19.txt"
inputdata = []
grid = []
gridsizex = 50
gridsizey = 50
posx = 0
posy = 0

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
			if char == 1:
				print("#", end = "")
			elif char == 0:
				print(".", end = "")
			else:
				print("?", end = "")

		print("")

#########################################
#########################################

def InitGrid():
	grid.clear()
	for y in range(0, gridsizey):
		grid.append([-1 for x in range(0, gridsizex)])

#########################################
#########################################

def PartA():
	global gridsizex
	global gridsizey

	gridsizex = 50
	gridsizex = 50

	print("Part A")

	InitGrid()
	computer = IntComputer(inputdata, None, "Compu")

	for x in range(gridsizex):
		for y in range(gridsizey):
			computer.reset()
			computer.run([x, y])
			grid[y][x] = computer.lastoutput

	count = 0
	for x in range(gridsizex):
		for y in range(gridsizey):
			if grid[y][x] == 1:
				count += 1

	PrintGrid(0, 0)

	print("Answer:", count)

#########################################
#########################################

def TryPartB(ox, oy):

	size = 99
	print(f"Trying Offset {ox}, {oy}")

	computer = IntComputer(inputdata, None, "Compu")

	computer.run([ox, oy])
	if computer.lastoutput == 0:
		print("Fail at corner TL")
		return False
	
	computer.reset()
	computer.run([ox + size, oy])
	if computer.lastoutput == 0:
		print("Fail at corner TR")
		return False

	computer.reset()
	computer.run([ox, oy + size])
	if computer.lastoutput == 0:
		print("Fail at corner BL")
		return False
	
	computer.reset()
	computer.run([ox + size, oy + size])
	if computer.lastoutput == 0:
		print("Fail at corner BR")
		return False

	return True

#########################################
#########################################

def PartB():

	size = 1000
	answer = 0

	print("Part B")

	computer = IntComputer(inputdata, None, "Compu")

	for y, x in itertools.product(range(size), range(size)):
		computer.reset()
		computer.run([x, y])
		if computer.lastoutput == 1:
			if TryPartB(x, y):
				answer = x * 10000 + y
				break

	# poging 1: 7800985 is too high
	# poging 2: 7720975 Correct 
	
	print("Answer:", answer)

#########################################
#########################################

if __name__ == "__main__":
	print("Day 19")
	ReadInput()
	PartA()
	PartB()
