import math
import os
from IntComputer import *

inputfile = "input-day13.txt"
inputdata = []

EMPTY = 0
WALL = 1
BLOCK = 2
PADDLE = 3
BALL = 4

gridsizex = 40
gridsizey = 20
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

def InitGrid():
	grid.clear()
	for y in range(0, gridsizey):
		grid.append([-1 for x in range(0, gridsizex)])

outputix = 0
x = 0
y = 0
ballx = 0
bally = 0
paddlex = 0
paddley = 0
score = 0

def OnOutput(output, ix):
	global x
	global y
	global paddlex
	global paddley
	global ballx
	global bally
	global score
	global outputix

	if outputix == 0:
		x = output
	elif outputix == 1:
		y = output
	else:
		if x == -1 and y == 0:
			score = output
		else:
			grid[y][x] = output
			PrintGrid()
			if output == BALL:
				ballx = x
				bally = y
			elif output == PADDLE:
				paddlex = x
				paddley = y

	outputix = (outputix + 1) % 3

def PrintGrid():
	# os.system("cls")
	# for row in grid:
	# 	for col in row:
	# 		if col == EMPTY:
	# 			print(" ", end = "")
	# 		elif col == WALL:
	# 			print("|", end = "")
	# 		elif col == BALL:
	# 			print("o", end = "")
	# 		elif col == BLOCK:
	# 			print("#", end = "")
	# 		elif col == PADDLE:
	# 			print("_", end = "")
	# 	print("")
	print("SCORE: %d" % score)

#########################################
#########################################

def PartA():
	print("Part A")
	InitGrid()
	game = IntComputer(inputdata, OnOutput, "Game")
	game.run([])

	blockCount = 0
	
	for row in grid:
		for col in row:
			if col == BLOCK:
				blockCount += 1

	print("Answer:", blockCount)

#########################################
#########################################

def PartB():
	print("Part B")
	InitGrid()
	inputdata[0] = 2
	game = IntComputer(inputdata, OnOutput, "Game")
	while True:
		game.run([])
		if game.finished:
			break;
		joy = 0
		if ballx < paddlex:
			joy = -1
		elif ballx > paddlex:
			joy = 1
		
		game.run([joy])

	print("Answer:", score)

#########################################
#########################################

if __name__ == "__main__":
	print("Day 13")
	ReadInput()
	# PartA()
	PartB()
