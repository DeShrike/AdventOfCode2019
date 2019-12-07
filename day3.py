import math

inputfile = "input-day3.txt"
inputdata = []
grid = []
intersections = []
testing = False

#########################################
#########################################

def ReadInput():
	testing = False
	file = open(inputfile, "r") 
	for line in file:
		inputdata.append(line)
	file.close()

#########################################
#########################################

def SetTestData1():
	testing = True
	inputdata.clear()
	inputdata.append("R75,D30,R83,U83,L12,D49,R71,U7,L72")
	inputdata.append("U62,R66,U55,R34,D71,R55,D58,R83")
	# answer = 159

def SetTestData2():
	testing = True
	inputdata.clear()
	inputdata.append("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51")
	inputdata.append("U98,R91,D20,R16,D67,R40,U7,R15,U6,R7")
	# answer = 135

#########################################
#########################################

def ManhattanDistance(x1, y1, x2, y2):
	return abs(x1 - x2) + abs(y1 - y2)

# for real
gridsizex = 17000
gridsizey = 13000
startx = 4200 # int(gridsize / 2)
starty = 1900 # int(gridsize / 2)

if testing:
	# for testing
	gridsizex = 1000
	gridsizey = 1000
	startx = 100 # int(gridsize / 2)
	starty = 100 # int(gridsize / 2)


def InitGrid():
	grid.clear()
	for x in range(0, gridsizex):
		grid.append([0 for y in range(0, gridsizey)])
	# print(grid)

def LayWireRight(dist, x, y, val):
	for i in range(0, dist):
		x += 1
		if x >= gridsizex:
			print("Grid too small: %d,%d" %  (x, y))
		grid[x][y] |= val

	return x, y

def LayWireLeft(dist, x, y, val):
	for i in range(0, dist):
		x -= 1
		if x < 0:
			print("Grid too small: %d,%d" %  (x, y))
		grid[x][y] |= val

	return x, y

def LayWireUp(dist, x, y, val):
	for i in range(0, dist):
		y += 1
		if y >= gridsizey:
			print("Grid too small: %d,%d" %  (x, y))
		grid[x][y] |= val

	return x, y

def LayWireDown(dist, x, y, val):
	for i in range(0, dist):
		y -= 1
		if y < 0:
			print("Grid too small: %d,%d" %  (x, y))
		grid[x][y] |= val

	return x, y

def LayWire(wire, val):
	print(wire)
	posx = startx
	posy = starty

	largestx = 0
	largesty = 0

	smallestx = gridsizex
	smallesty = gridsizey

	for part in wire.split(','):
		# print(part)
		if part[0] == "R":
			posx, posy = LayWireRight(int(part[1:]), posx, posy, val)
		elif part[0] == "L":
			posx, posy = LayWireLeft(int(part[1:]), posx, posy, val)
		elif part[0] == "U":
			posx, posy = LayWireUp(int(part[1:]), posx, posy, val)
		elif part[0] == "D":
			posx, posy = LayWireDown(int(part[1:]), posx, posy, val)
		else:
			print("Invalid code: ", part)

		if posx > largestx:
			largestx = posx
		if posy > largesty:
			largesty = posy

		if posx < smallestx:
			smallestx = posx
		if posy < smallesty:
			smallesty = posy

	print("Largest = %d, %d" % (largestx, largesty))
	print("Smallest = %d, %d" % (smallestx, smallesty))

def MoveTo(dist, x, y, goalx, goaly, dx, dy):
	steps = 0
	for i in range(0, dist):
		x += dx
		y += dy
		steps += 1
		if x == goalx and y == goaly:
			break

	return x, y, steps


def CountStepsTo(goalx, goaly, wire):
	posx = startx
	posy = starty
	totalsteps = 0
	for part in wire.split(','):
		# print(part)
		steps = 0
		if part[0] == "R":
			posx, posy, steps = MoveTo(int(part[1:]), posx, posy, goalx, goaly, 1, 0)
		elif part[0] == "L":
			posx, posy, steps = MoveTo(int(part[1:]), posx, posy, goalx, goaly, -1, 0)
		elif part[0] == "U":
			posx, posy, steps = MoveTo(int(part[1:]), posx, posy, goalx, goaly, 0, 1)
		elif part[0] == "D":
			posx, posy, steps = MoveTo(int(part[1:]), posx, posy, goalx, goaly, 0, -1)
		else:
			print("Invalid code: ", part)
		totalsteps += steps
		if posx == goalx and posy == goaly:
			break
	return totalsteps

#########################################
#########################################

def PartA():
	print("Part A")
	InitGrid()
	LayWire(inputdata[0], 1)
	LayWire(inputdata[1], 2)

	smallest_distance = 100000
	for x in range(0, gridsizex):
		for y in range(0, gridsizey):
			if grid[x][y] == 3:
				print("Intersection at %d,%d" % (x, y))
				intersections.append([x, y])
				distance = ManhattanDistance(startx, starty, x, y)
				if distance > 0 and distance < smallest_distance:
					smallest_distance = distance
	# print(grid)
	print("Answer:", smallest_distance)

#########################################
#########################################

def PartB():
	print("Part B")

	smallest = 10000000
	for i in intersections:
		steps1 = CountStepsTo(i[0], i[1], inputdata[0])
		steps2 = CountStepsTo(i[0], i[1], inputdata[1])

		if steps1 + steps2 < smallest:
			smallest = steps1 + steps2

	print("Answer:", smallest)

#########################################
#########################################

if __name__ == "__main__":
	print("Day 3")
	ReadInput()
	# SetTestData1()
	# SetTestData2()
	PartA()
	PartB()
