import math
from IntComputer import *

inputfile = "input-day25.txt"
inputdata = []
outputstring = None
lastcommand = None

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

def OnOutput(value, name):
	global outputstring
	global lastcommand
	if value > 255:
		return
	if value == 10:
		print(outputstring)
		lastcommand = outputstring
		outputstring = ""
	else:
		outputstring += chr(value)

#########################################
#########################################

def PartA():
	print("Part A")

	computer = IntComputer(inputdata, OnOutput, "CPU")

	computer.run([])
	while True:
		if computer.finished:
			break
		if lastcommand == "Command?":
			cmd = input("Command:")
			computer.run(AsciiToArray(cmd))

	# FOOD RATION		heavy	0
	# MOUSE				light	1
	# ORNAMENT			light	0
	# CANDY CANE		heavy	1
	# SEMICONDUCTOR		heavy	1
	# MUG				light	0
	# COIN				light	1
	# MUTEX				light	0

	answer = 100667393
	print("Answer:", answer)

#########################################
#########################################

def PartB():
	print("Part B")

	print("Answer:", 0)

#########################################
#########################################

if __name__ == "__main__":
	print("Day 25")
	ReadInput()
	PartA()
	PartB()
