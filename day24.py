import math
import itertools

inputfile = "input-day24.txt"
inputdata = []
grid = []
gridsizex = 5
gridsizey = 5
deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]

#########################################
#########################################

def ReadInput():
	file = open(inputfile, "r") 
	for line in file:
		inputdata.append(line.rstrip("\n"))
	file.close()

#########################################
#########################################

def BuildGrid():
	grid.clear()
	for l in inputdata:
		cc = []
		for col in l:
			cc.append(0 if col == "." else 1)
		grid.append(cc)
	

def LoadTestData():
	inputdata.clear()

	inputdata.append("....#")
	inputdata.append("#..#.")
	inputdata.append("#..##")
	inputdata.append("..#..")
	inputdata.append("#....")

	# answer = 2129920

#########################################
#########################################
def CountNeighbours(x, y):
	c = 0
	for delta in deltas:
		nx = x + delta[0]
		ny = y + delta[1]
		if nx < 0 or ny < 0 or nx >= gridsizex or ny >= gridsizey:
			pass
		else:
			c += grid[ny][nx]

	return c

def PrintGrid():
	print("===========")
	for line in grid:
		for col in line:
			print("." if col == 0 else "#", end = "")
		print("")

	print("")

def EvolveGrid():
	global grid
	newgrid = []
	for y in range(gridsizey):
		row = [0 for x in range(gridsizex)]
		newgrid.append(row)

	for x, y in itertools.product(range(gridsizex), range(gridsizey)):
		newgrid[y][x] = grid[y][x]
		c = CountNeighbours(x, y)
		if grid[y][x] == 1 and c != 1:
			newgrid[y][x] = 0
		if grid[y][x] == 0 and c in [1, 2]:
			newgrid[y][x] = 1

	grid = newgrid

#########################################
#########################################

def CalcBiodiversity():
	total = 0
	for x, y in itertools.product(range(gridsizex), range(gridsizey)):
		ix = x + y * gridsizex
		total += (2 ** ix) * grid[y][x]
	return total

#########################################
#########################################

# For Part B

class Space():
	
	dimensiondepth = 5
	dimensioncount = dimensiondepth * 2 + 1

	def __init__(self):
		self.dimensions = {}
		prev = None

		for d in range(-self.dimensiondepth, self.dimensiondepth + 1):
			dim = Dimension()
			dim.parent = prev
			dim.level = d
			if prev != None:
				prev.chid = dim
			prev = dim
			self.dimensions[d] = dim

	def GetValue(self, d, x, y):
		dim = self.dimensions[d]
		row = dim.grid[y]
		val = row[x]
		return val

	def SetValue(self, d, x, y, value):
		dim = self.dimensions[d]
		row = dim.grid[y]
		row[x] = value

	def Clone(self):
		newspace = Space()
		for d in range(-self.dimensiondepth, self.dimensiondepth + 1):
			dim = self.dimensions[d]
			for y in range(gridsizey):
				for x in range(gridsizex):
					newspace.SetValue(dim.level, x, y, self.GetValue(dim.level, x, y))
		return newspace

	def BugCount(self):
		c = 0
		for d in range(-self.dimensiondepth, self.dimensiondepth + 1):
			dim = self.dimensions[d]
			c += dim.BugCount()
		return c

	def Evolve(self):

		newspace = self.Clone()
		for d in range(-self.dimensiondepth, self.dimensiondepth + 1):
			dim = self.dimensions[d]
			for y in range(gridsizey):
				for x in range(gridsizex):
					# TODO: 
					pass 
		pass

class Dimension():

	def __init__(self):
		self.level = 0
		self.parent = None
		self.child = None
		self.grid = []
		for y in range(gridsizey):
			row = [0 for x in range(gridsizex)]
			self.grid.append(row)

	def BugCount(self):
		c = 0
		for y in range(gridsizey):
			row = self.grid[y]
			for x in row:
				c += x
		print(f"Level {self.level} = {c} bugs")
		self.PrintGrid()
		return c

	def PrintGrid(self):
		print(f"={self.level}==========")
		for line in self.grid:
			for col in line:
				print("." if col == 0 else "#", end = "")
			print("")

		print("===================")

#########################################
#########################################

def PartA():
	print("Part A")

	answer = 0
	# LoadTestData()

	BuildGrid()
	PrintGrid()

	biohistory = []

	while True:
		EvolveGrid()
		PrintGrid()
		# input("....")
		biodiversity = CalcBiodiversity()
		if biodiversity in biohistory:
			answer = biodiversity
			break
		else:
			biohistory.append(biodiversity)

	print("Answer:", answer)

#########################################
#########################################

def PartB():
	print("Part B")

	LoadTestData()
	BuildGrid()
	PrintGrid()
	space = Space()
	
	for y in range(gridsizey):
		for x in range(gridsizex):
			space.SetValue(0, x, y, grid[y][x])
	
	for minutes in range(10):
		space.Evolve()

	count = space.BugCount()
	print("Answer:", count)

#########################################
#########################################

if __name__ == "__main__":
	print("Day 24")
	ReadInput()
	PartA()
	PartB()
