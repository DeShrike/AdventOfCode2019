import math

inputfile = "input-day16.txt"
inputdata = []
signal = []
steps = 100
basepattern = [0, 1, 0, -1]

#########################################
#########################################

def ReadInput():
	file = open(inputfile, "r") 
	for line in file:
		inputdata.append(line.rstrip("\n"))
	file.close()

def ConvertInput():
	# global vanaf
	# global tot
	signal.clear()
	vanaf = 0
	for d in inputdata[0]:
		signal.append(int(d))
	tot = len(signal)

#########################################
#########################################

def LoadTest():
	inputdata.clear()

	# Test 1: Result = 24176176
	# inputdata.append("80871224585914546619083218645595")

	# Test 2: Result = 73745418
	inputdata.append("19617804207202209144916044189917")

	# Test 3: Result = 52432133
	# inputdata.append("69317163492948606335995924319873")

#########################################
#########################################

def BuildPattern(phase):
	pa = []
	for ix, p in enumerate(basepattern):
		for i in range(phase):
			pa.append(p)
	return pa

def DoFFTPhase(phase):
	sums = [0 for x in signal]
	for ddd in range(len(signal)):
		print("Phase %d  Pos: %d" % (phase, ddd), end = "  \r")
		pattern = BuildPattern(ddd + 1)
		ll = len(pattern)
		# print(pattern)
		patternix = 1	# start 1 shifted
		for ix, s in enumerate(signal):
			sums[ddd] += s * pattern[patternix]
			# print("%d * %d" % (s, pattern[patternix]), end = " + ")
			patternix = (patternix + 1) % ll
		# print("")

	for ix, s in enumerate(sums):
		signal[ix] = abs(s) % 10


def DoFFT():
	for phase in range(steps):
		DoFFTPhase(phase)
	print("")

#########################################
#########################################

def PartA():
	print("Part A")

	# LoadTest()
	ConvertInput()
	DoFFT()

	result = ""
	for i in range(8):
		result += str(signal[i])

	print("Answer:", result)

#########################################
#########################################

def PartB():
	global signal
	print("Part B")

	mul = 10000

	# LoadTest()
	ConvertInput()
	offset = ""
	for i in range(7):
		offset += str(signal[i])
	offset = int(offset)

	print("Offset: %d" % offset)
	
	signal = signal * mul
	signal = signal[offset:]

	print("Signal Length: %d " % len(signal))

	for _ in range(100):
		for i in range(len(signal) - 2, -1, -1):
			signal[i] += signal[i + 1]
			signal[i] %= 10

	result = "".join(map(str, signal[:8]))

	print("Answer:", result)

#########################################
#########################################

if __name__ == "__main__":
	print("Day 16")
	ReadInput()
	PartA()
	PartB()
