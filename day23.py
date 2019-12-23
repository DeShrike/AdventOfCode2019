import math
from IntComputer import *
from collections import deque

inputfile = "input-day23.txt"
inputdata = []

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

network = {}
computercount = 50
queus = {}
xbuffers = {}
abuffers = {}
answera = 0
prevnatx = None
prevnaty = None
natx = None
naty = None

def OnOutput(value, ix):
	global answera
	global natx
	global naty

	xb = xbuffers[ix]
	ab = abuffers[ix]

	if ab == None:
		abuffers[ix] = value
	elif xb == None:
		xbuffers[ix] = value
	else:
		if ab == 255:
			print("255 = %d" % value)
			answera = value
			natx = xb
			naty = value
			return

		q = queus[ab]
		q.append((xb, value))
		print(f"ENQUEUED to {ix}: ", end = "")
		print((xb, value))
		abuffers[ix] = None
		xbuffers[ix] = None

#########################################
#########################################

def SetupComputers():
	for ix in range(computercount):
		c = IntComputer(inputdata, OnOutput, ix)
		network[ix] = c
		q = deque()
		queus[ix] = q
		c.run([ix])
		xbuffers[ix] = None
		abuffers[ix] = None

def PartA():
	global answera
	print("Part A")

	SetupComputers()

	notfinisched = True
	while notfinisched:
		notfinisched = False
		for ix in range(computercount):
			c = network[ix]
			q = queus[ix]

			if len(q) == 0:
				c.run([-1])
			else:
				xy = q.popleft()
				print(f"DEQUEUD from {ix} : ", end = "")
				print(xy)
				c.run([xy[0], xy[1]])

			if c.finished == False:
				notfinisched = True
		print("*********************************************** %d" % answera)
		if answera != 0:
			break

	print("Answer:", answera)

#########################################
#########################################

def PartB():
	global prevnatx, prevnaty
	print("Part B")
	
	answerb = 0

	SetupComputers()

	notfinisched = True
	while notfinisched:
		notfinisched = False
		idle = True
		for ix in range(computercount):
			c = network[ix]
			q = queus[ix]

			if len(q) == 0:
				c.run([-1])
			else:
				idle = False
				xy = q.popleft()
				print(f"DEQUEUD from {ix} : ", end = "")
				print(xy)
				c.run([xy[0], xy[1]])

			if c.finished == False:
				notfinisched = True

		if idle:
			print("IDLE")
			if prevnaty == naty:
				answerb = naty
				break
			prevnatx = natx
			prevnaty = naty
			queus[0].append((natx, naty))

	print("Answer:", answerb)

#########################################
#########################################

if __name__ == "__main__":
	print("Day 23")
	ReadInput()
	PartA()
	PartB()
