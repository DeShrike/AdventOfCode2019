import math

inputfile = "input-day2.txt"
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

def RunProgram():
	ic = 0
	while True:
		opcode = mem[ic]
		if opcode == 99:
			break
		elif opcode == 1:
			op1addr = mem[ic + 1]
			op2addr = mem[ic + 2]
			op3addr = mem[ic + 3]
			# print("IC: %d - OPCODE: %d | [%d] = [%d] + [%d]" % (ic, opcode, op3addr, op1addr, op2addr))
			mem[op3addr] = mem[op1addr] + mem[op2addr]
		elif opcode == 2:
			op1addr = mem[ic + 1]
			op2addr = mem[ic + 2]
			op3addr = mem[ic + 3]
			# print("IC: %d - OPCODE: %d | [%d] = [%d] * [%d]" % (ic, opcode, op3addr, op1addr, op2addr))
			mem[op3addr] = mem[op1addr] * mem[op2addr]
		else:
			print("Invalid opcode %d at posision %d" % (opcode, ic))
		ic += 4

#########################################
#########################################

def PartA():
	global mem
	print("Part A")

	mem = [x for x in inputdata]
	mem[1] = 12
	mem[2] = 2

	RunProgram()

	print("Answer:", mem[0])

#########################################
#########################################

def PartB():
	global mem
	print("Part B")
	answer = 0
	for noun in range(0, 100):
		for verb in range(0, 100):
			mem = [x for x in inputdata]
			mem[1] = noun
			mem[2] = verb
			RunProgram()

			# print("Noun: %d - Verb: %d - Result: %d" % (noun, verb, mem[0]))

			if mem[0] == 19690720:
				print("Found it !")
				answer = 100 * noun + verb
				break
		if answer != 0:
			break;

	print("Answer:", answer)

#########################################
#########################################

if __name__ == "__main__":
	print("Day 2")
	ReadInput()
	PartA()
	PartB()

