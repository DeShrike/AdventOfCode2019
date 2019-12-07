import math

inputdata = [240920,789857]

#########################################
#########################################

def isValidA(num):
	last = -1
	double = False
	for d in str(num):
		dd = int(d)
		if dd < last:
			return False
		if dd == last:
			double = True
		last = dd
	return double

#########################################
#########################################

def PartA():
	print("Part A")

	count = 0
	for num in range(inputdata[0], inputdata[1] + 1):
		# if num % 1000 == 0:
		# 	print("Checking %d" % num)
		if isValidA(num):
			count += 1
			# print("Valid: %d" % num)
	print("Answer:", count)

#########################################
#########################################

def isValidB(num):
	counts = [1 for x in range(0, 10)]
	last = -1
	double = False
	for d in str(num):
		dd = int(d)
		if dd < last:
			return False
		if dd == last:
			counts[dd] += 1
			double = True
		last = dd
	return double and (2 in counts)

#########################################
#########################################

def PartB():
	print("Part B")

	count = 0
	for num in range(inputdata[0], inputdata[1] + 1):
		# if num % 1000 == 0:
		# 	print("Checking %d" % num)
		if isValidB(num):
			count += 1
			# print("Valid: %d" % num)
	print("Answer:", count)

#########################################
#########################################

if __name__ == "__main__":
	print("Day 4")
	PartA()
	PartB()

