import math
import itertools
from IntComputer import *

inputfile = "input-day7.txt"
inputdata = []
mem = []

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

def RunProgram(inputs):

	global mem

	print("INPUTS: ", end = "")
	print(inputs)

	inputix = 0
	output = 0

	mem = [x for x in inputdata]

	op1addr = 0
	op2addr = 0
	op3addr = 0

	val1 = 0
	val2 = 0
	val3 = 0

	ip = 0
	il = 0
	while True:
		instruction = mem[ip]

		opcode = instruction % 100
		instruction = (instruction - opcode) / 100
		mode1 = instruction % 10
		instruction = (instruction - mode1) / 10
		mode2 = instruction % 10
		instruction = (instruction - mode2) / 10
		mode3 = instruction % 10

		# print("IP: %d I: %d OPCODE: %d  MODE1: %d MODE2: %d MODE3: %d " % (ip, mem[ip], opcode, mode1, mode2, mode3))

		paramcounts = [0, 3, 3, 1, 1, 2, 2, 3, 3]
		paramcount = paramcounts[0 if opcode == 99 else opcode]
		if paramcount >= 1:
			op1addr = mem[ip + 1]
			val1 = mem[op1addr] if mode1 == 0 else op1addr

		if paramcount >= 2:
			op2addr = mem[ip + 2]
			val2 = mem[op2addr] if mode2 == 0 else op2addr

		if paramcount >= 3:
			op3addr = mem[ip + 3]
			val3 = mem[op3addr] if mode3 == 0 else op3addr

		if opcode == 99:	# QUIT
			il = 1
			print("QUIT")
			break
		elif opcode == 1:	# ADD
			mem[op3addr] = val1 + val2
			il = 4
		elif opcode == 2:	# MULTIPLY
			mem[op3addr] = val1 * val2
			il = 4
		elif opcode == 3:	# INPUT
			inp = inputs[inputix] if inputix < len(inputs) else output
			print("INPUT: %d" % inp)
			mem[op1addr] = inp
			inputix += 1
			il = 2
		elif opcode == 4:	# OUTPUT
			output = val1
			print("OUTPUT: %d" % output)
			il = 2
		elif opcode == 5:	# JUMP IF TRUE
			il = 3
			if val1 != 0:
				ip = val2
				il = 0
		elif opcode == 6:	# JUMP IF FALSE
			il = 3
			if val1 == 0:
				ip = val2
				il = 0
		elif opcode == 7:	# LESS THAN
			mem[op3addr] = 1 if val1 < val2 else 0
			il = 4
		elif opcode == 8:	# EQUALS
			mem[op3addr] = 1 if val1 == val2 else 0
			il = 4
		else:
			print("Invalid opcode %d at position %d" % (opcode, ip))
		ip += il
	
	return output

#########################################
#########################################



#########################################
#########################################

def PartA():
	print("Part A")

	largest = 0
	settings = [0, 1, 2, 3, 4]

	for subset in itertools.permutations(settings):
		print("Settings: ", end = "")
		print(subset)

		trust = 0
		for setting in subset:
			trust = RunProgram([setting, trust])
		
		if trust > largest:
			largest = trust

	print("Answer:", largest)

#########################################
#########################################

ampA = None
ampB = None
ampC = None
ampD = None
ampE = None

def PartB():
	global inputdata
	global ampA
	global ampB
	global ampC
	global ampD
	global ampE

	print("Part B")
	
	test1 = "3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5"
	# test1 results = 139629729
	test2 = "3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10"
	# test2 results = 18216

	# inputdata = [int(x) for x in test1.split(",")]
	# inputdata = [int(x) for x in test2.split(",")]

	largest = 0
	settings = [5, 6, 7, 8, 9]

	for subsettuple in itertools.permutations(settings):

		subset = [x for x in subsettuple]
		# print("Settings: ", end = "")
		# print(subset)

		trust = 0

		ampA = IntComputer(inputdata, name = "ampA")
		ampB = IntComputer(inputdata, name = "ampB")
		ampC = IntComputer(inputdata, name = "ampC")
		ampD = IntComputer(inputdata, name = "ampD")
		ampE = IntComputer(inputdata, name = "ampE")

		ampA.run(subset[0:1] + [trust])
		trust = ampA.lastoutput
		ampB.run(subset[1:2] + [trust])
		trust = ampB.lastoutput
		ampC.run(subset[2:3] + [trust])
		trust = ampC.lastoutput
		ampD.run(subset[3:4] + [trust])
		trust = ampD.lastoutput
		ampE.run(subset[4:5] + [trust])
		trust = ampE.lastoutput

		while True: 
			ampA.run([trust])
			trust = ampA.lastoutput
			ampB.run([trust])
			trust = ampB.lastoutput
			ampC.run([trust])
			trust = ampC.lastoutput
			ampD.run([trust])
			trust = ampD.lastoutput
			ampE.run([trust])
			trust = ampE.lastoutput
			if ampE.finished:
				break;
		
		if trust > largest:
			largest = trust

	print("Answer:", largest)

#########################################
#########################################

if __name__ == "__main__":
	print("Day 7")
	ReadInput()
	PartA()
	PartB()
