import math

inputfile = "input-day5.txt"
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

def RunProgram(theinput):
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
			break
		elif opcode == 1:	# ADD
			mem[op3addr] = val1 + val2
			il = 4
		elif opcode == 2:	# MULTIPLY
			mem[op3addr] = val1 * val2
			il = 4
		elif opcode == 3:	# INPUT
			mem[op1addr] = theinput
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

#########################################
#########################################

#########################################
#########################################

def PartA():
	global mem
	print("Part A")

	mem = [x for x in inputdata]

	RunProgram(1)

	print("Answer:", "the last output")

#########################################
#########################################

def PartB():
	global mem
	print("Part B")

	mem = [x for x in inputdata]

	# test ="3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99"
	# mem = [int(x) for x in test.split(",")]

	RunProgram(5)

	print("Answer:", "the last output")

#########################################
#########################################

if __name__ == "__main__":
	print("Day 5")
	ReadInput()
	PartA()
	PartB()

