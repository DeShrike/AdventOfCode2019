import math

# https://adventofcode.com/2019

inputfile = "input-day1.txt"
inputdata = []

#########################################
#########################################

def ReadInput():
	file = open(inputfile, "r") 
	for line in file:
		inputdata.append(int(line))
	file.close()

#########################################
#########################################

def CalcFuel(mass):
	return math.floor(mass / 3) - 2

#########################################
#########################################

def PartA():
	print("Part A")
	total = 0
	for m in inputdata:
		f = CalcFuel(m)
		# print(f)
		total += f

	print("Answer:", total)

#########################################
#########################################

def CalcTotalFuel(mass):
	total = 0
	fuel = CalcFuel(mass)
	while fuel > 0:
		total += fuel
		fuel = CalcFuel(fuel)

	return total

def PartB():
	print("Part B")
	total = 0
	for m in inputdata:
		f = CalcTotalFuel(m)
		# print(f)
		total += f

	print("Answer:", total)

#########################################
#########################################

if __name__ == "__main__":
	print("Day 1")
	ReadInput()
	PartA()
	PartB()

