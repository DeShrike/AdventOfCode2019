import math
from IntComputer import *

inputfile = "input-day21.txt"
inputdata = []
outputstring = ""

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

def AsciiToArray(command):
	cmd = [ord(x) for x in command]
	cmd.append(10)
	return cmd

def OnOutputA(value, ix):
	global outputstring
	if value > 255:
		return
	if value == 10:
		print(outputstring)
		outputstring = ""
	else:
		outputstring += chr(value)

#########################################
#########################################

# J = !(A & B & C) & D

def PartA():
	global outputstring
	print("Part A")

	outputstring = ""
	computer = IntComputer(inputdata, OnOutputA, "JumpComputer")
	computer.run([])

	computer.run(AsciiToArray("NOT A J"))
	computer.run(AsciiToArray("NOT J J"))
	computer.run(AsciiToArray("AND B T"))
	computer.run(AsciiToArray("AND C J"))
	computer.run(AsciiToArray("NOT J J"))
	computer.run(AsciiToArray("AND D J"))
	computer.run(AsciiToArray("WALK"))

	while True:
		if computer.finished:
			break

	print("Answer:", computer.lastoutput)

#########################################
#########################################

# J = (!A & D) | (!B & D) | (!C & D & H)

def PartB():
	global outputstring
	print("Part B")

	outputstring = ""
	computer = IntComputer(inputdata, OnOutputA, "JumpComputer")
	computer.run([])

	computer.run(AsciiToArray("NOT C J"))
	computer.run(AsciiToArray("AND H J"))
	computer.run(AsciiToArray("NOT B T"))
	computer.run(AsciiToArray("OR T J"))
	computer.run(AsciiToArray("NOT A T"))
	computer.run(AsciiToArray("OR T J"))
	computer.run(AsciiToArray("AND D J"))
	computer.run(AsciiToArray("RUN"))

	while True:
		if computer.finished:
			break

	print("Answer:", computer.lastoutput)

#########################################
#########################################

if __name__ == "__main__":
	print("Day 21")
	ReadInput()
	PartA()
	PartB()
