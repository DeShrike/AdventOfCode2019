import math
import itertools
from AStar import *

# https://docs.python.org/3/library/itertools.html

inputfile = "input-day18.txt"
inputdata = []
grid = []
gridsizex = 0
gridsizey = 0
posx = 0
posy = 0

WALL = "#"
SPACE = "."

STARTKEY = "@"

keynames = []
keys = {}
keycoords = {}
doors = {}
doorcoords = {}

distances = {}	# Key = (key1, key2), value = (distance, [doorsinpath, ...])

#########################################
#########################################

def ReadInput():
	file = open(inputfile, "r") 
	for line in file:
		inputdata.append(line.rstrip("\n"))
	file.close()

#########################################
#########################################

def LoadSampleA():
	inputdata.clear()
	inputdata.append("########################")
	inputdata.append("#...............b.C.D.f#")
	inputdata.append("#.######################")
	inputdata.append("#.....@.a.B.c.d.A.e.F.g#")
	inputdata.append("########################")
	# Shortest path is 132 steps: b, a, c, d, f, e, g

def LoadSampleB():
	inputdata.clear()
	inputdata.append("#################")
	inputdata.append("#i.G..c...e..H.p#")
	inputdata.append("########.########")
	inputdata.append("#j.A..b...f..D.o#")
	inputdata.append("########@########")
	inputdata.append("#k.E..a...g..B.n#")
	inputdata.append("########.########")
	inputdata.append("#l.F..d...h..C.m#")
	inputdata.append("#################")
	# Shortest paths are 136 steps;
	# one is: a, f, b, j, g, n, h, d, l, o, e, p, c, i, k, m

def LoadSampleC():
	inputdata.clear()
	inputdata.append("########################")
	inputdata.append("#@..............ac.GI.b#")
	inputdata.append("###d#e#f################")
	inputdata.append("###A#B#C################")
	inputdata.append("###g#h#i################")
	inputdata.append("########################")
	# Shortest paths are 81 steps; one is: a, c, f, i, d, g, b, e, h

#########################################
#########################################

def BuildGrid():
	global gridsizex
	global gridsizey
	global posx
	global posy

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
			elif char >= "a" and char <= "z":
				keys[char] = (x, y)
				keycoords[(x, y)] = char
				keynames.append(char)
				grid[y][x] = SPACE
			elif char >= "A" and char <= "Z":
				doors[char] = (x, y)
				doorcoords[(x, y)] = char
				grid[y][x] = SPACE
			elif char == "@":
				posx, posy = x, y
				grid[y][x] = SPACE

	keys["@"] = (posx, posy)
	keycoords[(posx, posy)] = "@"
	keynames.append("@")

#########################################
#########################################

def FindDistances():
	# find distances from one key to another

	for subset in itertools.combinations(keynames, 2):

		l1 = subset[0]
		l2 = subset[1]

		# print(f"L1 {l1}  L2 {l2}")

		x1 = keys[l1][0]
		y1 = keys[l1][1]

		x2 = keys[l2][0]
		y2 = keys[l2][1]

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
		path = astar.run([x1, y1], [x2, y2])

		# print("path:")
		# print(path)

		hasontherkey = 0
		doorsinpath = []
		for p in path:
			pp = (p[0], p[1])
			# print(pp)
			if pp in doorcoords:
				doorsinpath.append(doorcoords[pp])
			# elif pp in keycoords:
			# 	ok = keycoords[pp]
			# 	# print(ok)
			# 	if ok != l1 and ok != l2 and ok != STARTKEY:
			# 		print("true")
			# 		hasontherkey += 1
			# input("press...")

		if hasontherkey < 2:
			distances[subset] = (len(path) - 1, doorsinpath)

#########################################
#########################################

class StepA():

	def __init__(self, key, p):
		self.start = key
		self.length = 0
		self.children = []
		self.parent = p
		self.level = 0
		if self.parent != None:
			self.level = self.parent.level + 1

		print(f"Level {self.level}  ", end = "\r")

	def LockedDoorInPath(self, fromto):
		if fromto not in distances:
			return False
		dist = distances[fromto]
		doorsinpath = dist[1]
		for door in doorsinpath:
			if self.KeyAlreadyGotten(door.lower()) == False:
				return True
		return False

	def BuildPath(self):
		x = self
		string = ""
		while x != None:
			string = x.start + string
			x = x.parent
		return string

	def DoStep(self):
		# print("===========================")
		# print("DoStep ***** From %s" % self.start)
		# print("So far: %s" % self.BuildPath())
		for l in keynames:
			if self.KeyAlreadyGotten(l):
				continue
			
			subset1 = (self.start, l)
			subset2 = (l, self.start)
			if subset1 in distances and self.LockedDoorInPath(subset1) == False:
				ll = distances[subset1][0]
				# print(subset1)
				# print("Step Into %s => length %d" % (l, ll))
				child = StepA(l, self)
				child.length = ll
				self.children.append(child)
			elif subset2 in distances and self.LockedDoorInPath(subset2) == False:
				ll = distances[subset2][0]
				# print(subset2)
				# print("Step Into %s => length %d" % (l, ll))
				child = StepA(l, self)
				child.length = ll
				self.children.append(child)

		if len(self.children) > 0:
			for child in self.children:
				child.DoStep()

			shortest = 100000
			for child in self.children:
				if child.length < shortest: # and child.length > 0:
					shortest = child.length
			
			self.length += shortest
		else:
			# print("No steps left from %s" % self.start)
			pass

		# print(" Length from %s = %d" % (self.start, self.length))

	def KeyAlreadyGotten(self, k):
		if self.start == k:
			return True
		p = self.parent
		while p != None:
			if p.start == k:
				return True
			p = p.parent

		return False

#########################################
#########################################

def PartA():
	print("Part A")

	# LoadSampleA()
	LoadSampleB()
	# LoadSampleC()

	BuildGrid()

	print("Keys:")
	print(keys)
	print(keycoords)

	print("Doors:")
	print(doors)
	print(doorcoords)

	print(f"Start: {posx},{posy}")

	FindDistances()
	print("Disances: %d" % len(distances))
	print(keynames)
	print(distances)

	input("Press....")

	root = StepA(STARTKEY, None)
	root.DoStep()

	answer = root.length

	print("Done          ")
	print("Answer:", answer)

#########################################
#########################################

def PartB():
	print("Part B")

	print("Answer:", 0)

#########################################
#########################################

if __name__ == "__main__":
	print("Day 18")
	ReadInput()
	PartA()
	PartB()
