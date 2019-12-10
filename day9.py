import math
from IntComputer import *

inputfile = "input-day9.txt"
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


#########################################
#########################################

def PartA():
	global inputdata
	print("Part A")

	test1 = "109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99"
	test2 = "1102,34915192,34915192,7,4,7,99,0"
	test3 = "104,1125899906842624,99"

	# inputdata = [int(x) for x in test1.split(",")]
	# inputdata = [int(x) for x in test2.split(",")]
	# inputdata = [int(x) for x in test3.split(",")]

	computer = IntComputer(inputdata)
	computer.run([1])

	print("Answer:")
	print(computer.outputs)

#########################################
#########################################

def PartB():
	print("Part B")

	computer = IntComputer(inputdata)
	computer.run([2])

	print("Answer:")
	print(computer.outputs)

#########################################
#########################################

if __name__ == "__main__":
	print("Day 9")
	ReadInput()
	PartA()
	PartB()
