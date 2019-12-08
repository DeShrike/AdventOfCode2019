import math

inputfile = "input-day8.txt"
inputdata = None
width = 25
height = 6
image = None

#########################################
#########################################

def ReadInput():
	global inputdata
	file = open(inputfile, "r") 
	for line in file:
		inputdata = line.rstrip("\n")
	file.close()

#########################################
#########################################

def DecodeImage():
	global image
	image = []
	layer = None
	row = None
	l = len(inputdata)
	for pix in inputdata:
		if layer == None:
			layer = []
			image.append(layer)

		if row == None:
			row = []
			layer.append(row)

		row.append(int(pix))

		if len(row) == width:
			row = None
			if len(layer) == height:
				layer = None

#########################################
#########################################

def PrintImage():
	for l in range(len(image)):
		layer = image[l]
		print("Layer: %d" % l)
		for r in range(len(layer)):
			row = layer[r]
			print("  Row: %d" % r, end = "")
			print("    ", end = "")
			for p in row:
				print(p, end = "")
			print("")

def PrintFinalImage(image):
	for r in range(len(image)):
		row = image[r]
		for p in row:
			# print(" " if p == 2 else p, end = "")
			print(" " if p == 0 else p, end = "")
		print("")

#########################################
#########################################

def CountInLayer(layer, find):
	count = 0
	for row in layer:
		count += row.count(find)
	return count

#########################################
#########################################

def GenerateFinalImage():
	result = image[0]
	for layer in image[1:]:
		for x in range(width):
			for y in range(height):
				ip = result[y][x]
				il = layer[y][x]
				if ip == 2:
					result[y][x] = il
	return result

#########################################
#########################################

def PartA():
	print("Part A")

	DecodeImage()
	# PrintImage()

	smallest = 1000000
	smallestLayer = None
	for layer in image:
		aantal = CountInLayer(layer, 0)
		if aantal < smallest:
			smallest = aantal
			smallestLayer = layer

	answer = CountInLayer(smallestLayer, 1) * CountInLayer(smallestLayer, 2) 

	print("Answer:", answer)

#########################################
#########################################

def PartB():
	print("Part B")

	DecodeImage()
	finalImage = GenerateFinalImage()

	print("Answer:")
	PrintFinalImage(finalImage)

#########################################
#########################################

if __name__ == "__main__":
	print("Day 8")
	ReadInput()
	PartA()
	PartB()
