import math
from ansi import *

inputfile = "input-day6.txt"
inputdata = []
orbitmap = None

#########################################
#########################################

def ReadInput():
	inputdata.clear()
	file = open(inputfile, "r") 
	for line in file:
		inputdata.append(line.rstrip("\n"))
	file.close()

#########################################
#########################################

def LoadTestDataA():
	inputdata.clear()
	inputdata.append("B)C")
	inputdata.append("C)D")
	inputdata.append("COM)B")
	inputdata.append("D)E")
	inputdata.append("B)G")
	inputdata.append("G)H")
	inputdata.append("D)I")
	inputdata.append("E)J")
	inputdata.append("J)K")
	inputdata.append("K)L")
	inputdata.append("E)F")

	# answer = 42

#########################################
#########################################

def LoadTestDataB():
	inputdata.clear()
	inputdata.append("COM)B")
	inputdata.append("B)C")
	inputdata.append("C)D")
	inputdata.append("D)E")
	inputdata.append("E)F")
	inputdata.append("B)G")
	inputdata.append("G)H")
	inputdata.append("D)I")
	inputdata.append("E)J")
	inputdata.append("J)K")
	inputdata.append("K)L")
	inputdata.append("K)YOU")
	inputdata.append("I)SAN")
	
	# answer = 4

#########################################
#########################################

class Node():
	def __init__(self, _name):
		self.name = _name
		self.orbitters = []
		self.level = 0
		self.parent = None
		self.you = False

	def addOrbitter(self, node):
		# print("Adding %s to %s" % (node.name, self.name))
		self.orbitters.append(node)
		node.level = self.level + 1
		node.parent = self

def FindNode(node, name):
	# print("Finding %s in %s" % (name, "(None)" if node == None else node.name))
	if node == None:
		return None
	if node.name == name:
		return node
	for sat in node.orbitters:
		f = FindNode(sat, name)
		if f != None:
			return f
	return None

def BuildMap():
	global orbitmap
	
	orbitmap = None

	for ix in range(len(inputdata)):
		if inputdata[ix][0:3] == "COM":
			orbitmap = Node("COM")
			break
	lcount = 0
	done = False
	while done == False:
		done = True
		print("Loop %d" % lcount, end = "\r")
		lcount += 1		
		for ix in range(len(inputdata)):
			line = inputdata[ix]
			if line == "":
				continue

			done = False
			main = line.split(")")[0]
			satelite = line.split(")")[1]

			node = FindNode(orbitmap, main)
			if node == None:
				continue
		
			satnode = FindNode(orbitmap, satelite)
			if satnode != None:
				print("%s : Satelite already exists" % line)
				return

			satnode = Node(satelite)
			node.addOrbitter(satnode)
			inputdata[ix] = ""
	print("")

def PrintMap(node):
	sats = ""
	for sat in node.orbitters:
		sats = sats + sat.name + ","
	
	print("   %s [%d]) %s" % (node.name, node.level, sats))

	for sat in node.orbitters:
		PrintMap(sat)

def CountConnections(node):
	c = node.level
	for sat in node.orbitters:
		c = c + CountConnections(sat)
	return c

#########################################
#########################################

def PartA():
	print("Part A")

	print("Building map...")
	BuildMap()
	print("Counting...")
	# PrintMap(orbitmap)
	count = CountConnections(orbitmap)

	print("Answer:", count)

#########################################
#########################################

def PartB():
	print("Part B")

	print("Building map...")
	BuildMap()
	# PrintMap(orbitmap)

	you = FindNode(orbitmap, "YOU")
	san = FindNode(orbitmap, "SAN")
	print("YOU = %s level %d" % (you.name, you.level))
	print("SAN = %s level %d" % (san.name, san.level))

	steps = 0
	add = 1
	p = you.parent
	while p != None:
		steps += add
		p.you = True
		p = p.parent
	
	s = san.parent
	while s != None:
		if s.you:
			add = -1
		steps += add
		s = s.parent

	print("Answer:", steps)

#########################################
#########################################

if __name__ == "__main__":
	print("Day 6")
	ReadInput()
	# LoadTestDataA()
	PartA()
	ReadInput()
	# LoadTestDataB()
	PartB()

