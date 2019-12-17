import math
import re

inputfile = "input-day12.txt"
inputdata = []
positions = []
velocities = []
steps = 1000
pairs = [
	[0, 1],
	[0, 2],
	[0, 3],
	[1, 2],
	[1, 3],
	[2, 3]
]
#########################################
#########################################

def ReadInput():
	file = open(inputfile, "r") 
	for line in file:
			inputdata.append(line)
	file.close()

	rx = re.compile("x=(?P<x>[0-9\-]*).*y=(?P<y>[0-9\-]*).*z=(?P<z>[0-9\-]*)")
	rx_dict = {
		'x': re.compile("x=(?P<x>[0-9\-]*)"),
		'y': re.compile("y=(?P<y>[0-9\-]*)"),
		'z': re.compile("z=(?P<z>[0-9\-]*)"),
	}

	positions.clear()
	velocities.clear()

	for line in inputdata:
		match = rx.search(line)
		if match:
			positions.append([int(match["x"]),int(match["y"]),int(match["z"])])
			velocities.append([0, 0, 0])

#########################################
#########################################

def Example1():
	global steps

	positions.clear()
	positions.append([-1, 0, 2])
	positions.append([2, -10, -7])
	positions.append([4, -8, 8])
	positions.append([3, 5, -1])
	
	velocities.clear()
	velocities.append([0, 0, 0])
	velocities.append([0, 0, 0])
	velocities.append([0, 0, 0])
	velocities.append([0, 0, 0])
	
	steps = 10

def Example2():
	global steps

	positions.clear()
	positions.append([-8, -10, 0])
	positions.append([5, 5, 10])
	positions.append([2, -7, 3])
	positions.append([9, -8, -3])

	velocities.clear()
	velocities.append([0, 0, 0])
	velocities.append([0, 0, 0])
	velocities.append([0, 0, 0])
	velocities.append([0, 0, 0])

	steps = 100

#########################################
#########################################

def ApplyGravity(axis):

	for pair in pairs:
		m1 = positions[pair[0]]
		m2 = positions[pair[1]]
		v1 = velocities[pair[0]]
		v2 = velocities[pair[1]]
		# for axis in range(3):
		# 	if m1[axis] != m2[axis]:
		# 		if m1[axis] < m2[axis]:
		# 			v1[axis] += 1
		# 			v2[axis] += -1
		# 		else:
		# 			v1[axis] += -1
		# 			v2[axis] += 1

		if m1[axis] != m2[axis]:
			if m1[axis] < m2[axis]:
				v1[axis] += 1
				v2[axis] += -1
			else:
				v1[axis] += -1
				v2[axis] += 1

def ApplyVelocity(axis):

	for	i in range(len(positions)):
		pos = positions[i]
		grav = velocities[i]
		# pos[0] += grav[0]
		# pos[1] += grav[1]
		# pos[2] += grav[2]
		pos[axis] += grav[axis]

def CalcEnergy():

	total = 0
	for i in range(len(positions)):
		pos = positions[i]
		vel = velocities[i]
		pot = abs(pos[0]) + abs(pos[1]) + abs(pos[2])
		kin = abs(vel[0]) + abs(vel[1]) + abs(vel[2])
		total += pot * kin

	return total

#########################################
#########################################

def CalcRepeatForAxis(axis):
	history = []
	step = 1

	deze = [positions[0][axis], positions[1][axis], positions[2][axis], positions[3][axis],
			velocities[0][axis], velocities[1][axis], velocities[2][axis], velocities[3][axis],
			]
	history.append(deze)
	while True:
		ApplyGravity(axis)
		ApplyVelocity(axis)

		deze = [positions[0][axis], positions[1][axis], positions[2][axis], positions[3][axis],
				velocities[0][axis], velocities[1][axis], velocities[2][axis], velocities[3][axis],
				]

		if deze in history:
			# print(deze)
			print("")
			return step

		history.append(deze)
		step += 1
		print(f"Step {step}   ", end = "\r")

#########################################
#########################################

def PartA():
	print("Part A")
	
	# Example1()
	# Example2()

	for step in range(steps):
		ApplyGravity(0)
		ApplyGravity(1)
		ApplyGravity(2)
		ApplyVelocity(0)
		ApplyVelocity(1)
		ApplyVelocity(2)

		# print("Step %d" % (step + 1))
		# for i in range(4):
		# 	pos = positions[i]
		# 	vel = velocities[i]

		# 	print("Pos: %d %d %d  Vel: %d %d %d" % (pos[0], pos[1], pos[2], vel[0], vel[1], vel[2]))
		
		# input("Press...")

	energy = CalcEnergy()

	print("Answer:", energy)

#########################################
#########################################

def lcm(x, y):
    '''least common multiple : kleinst gemeen veelvoud'''
    a, b = x, y
    while a:
        a, b = b % a, a
    return x // b * y

def PartB():
	print("Part B")

	# Example1()
	# steps = 2772
	# Example2()
	# steps = 4686774924

	a = CalcRepeatForAxis(0)
	print(f"A: {a}")
	b = CalcRepeatForAxis(1)
	print(f"B: {b}")
	c = CalcRepeatForAxis(2)
	print(f"C: {c}")

	print("Answer:", lcm(a, lcm(b, c)))
	# Poging 1: 5125985850732195 Too High
	# Poging 3: 320380285873116 Correct
	
#########################################
#########################################

if __name__ == "__main__":
	print("Day 12")
	ReadInput()
	PartA()
	PartB()
