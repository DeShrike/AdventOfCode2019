import math

inputfile = "input-day10.txt"
inputdata = []

#########################################
#########################################

def ReadInput():
	inputdata.clear()
	file = open(inputfile, "r") 
	for line in file:
		inputdata.append(line.rstrip("\n"))
	file.close()

#########################################
#########################################

def LoadTest1A():
	inputdata.clear()
	inputdata.append("......#.#.")
	inputdata.append("#..#.#....")
	inputdata.append("..#######.")
	inputdata.append(".#.#.###..")
	inputdata.append(".#..#.....")
	inputdata.append("..#....#.#")
	inputdata.append("#..#....#.")
	inputdata.append(".##.#..###")
	inputdata.append("##...#..#.")
	inputdata.append(".#....####")

	# result = 5,8 => 33

def LoadTest2A():
	inputdata.clear()
	inputdata.append("#.#...#.#.")
	inputdata.append(".###....#.")
	inputdata.append(".#....#...")
	inputdata.append("##.#.#.#.#")
	inputdata.append("....#.#.#.")
	inputdata.append(".##..###.#")
	inputdata.append("..#...##..")
	inputdata.append("..##....##")
	inputdata.append("......#...")
	inputdata.append(".####.###.")

	# result = 1,2 => 35

def LoadTest3A():
	inputdata.clear()
	inputdata.append(".#..#..###")
	inputdata.append("####.###.#")
	inputdata.append("....###.#.")
	inputdata.append("..###.##.#")
	inputdata.append("##.##.#.#.")
	inputdata.append("....###..#")
	inputdata.append("..#.#..#.#")
	inputdata.append("#..#.#.###")
	inputdata.append(".##...##.#")
	inputdata.append(".....#.#..")

	# result = 6,3 => 41


def LoadTest4A():
	inputdata.clear()
	inputdata.append(".#..##.###...#######")
	inputdata.append("##.############..##.")
	inputdata.append(".#.######.########.#")
	inputdata.append(".###.#######.####.#.")
	inputdata.append("#####.##.#.##.###.##")
	inputdata.append("..#####..#.#########")
	inputdata.append("####################")
	inputdata.append("#.####....###.#.#.##")
	inputdata.append("##.#################")
	inputdata.append("#####.##.###..####..")
	inputdata.append("..######..##.#######")
	inputdata.append("####.##.####...##..#")
	inputdata.append(".#####..#.######.###")
	inputdata.append("##...#.##########...")
	inputdata.append("#.##########.#######")
	inputdata.append(".####.#.###.###.#.##")
	inputdata.append("....##.##.###..#####")
	inputdata.append(".#.#.###########.###")
	inputdata.append("#.#.#.#####.####.###")
	inputdata.append("###.##.####.##.#..##")

	# result = 11,&3 => 210

def LoadTest5A():
	inputdata.clear()
	inputdata.append("...#......")
	inputdata.append("..........")
	inputdata.append("....#..#..")
	inputdata.append("..........")
	inputdata.append(".....#....")
	inputdata.append("#...X..#..")
	inputdata.append("..........")
	inputdata.append("..#.......")
	inputdata.append("..........")
	inputdata.append("....#.....")

	# result = 4,5 => 1

def LoadTest6A():
	inputdata.clear()
	inputdata.append(".#....#####...#..")
	inputdata.append("##...##.#####..##")
	inputdata.append("##...#...#.#####.")
	inputdata.append("..#.....X...###..")
	inputdata.append("..#.#.....#....##")

	# result = 8,3 => 1

#########################################
#########################################

def ResetField():
	height = len(inputdata)
	width = len(inputdata[0])
	for x in range(width):
		for y in range(height):
			if inputdata[y][x] == "H":
				s = list(inputdata[y])
				s[x] = "#"
				inputdata[y] = "".join(s)

def CheckAsteroidVisibility(x, y, dx, dy):
	height = len(inputdata)
	width = len(inputdata[0])
	found = False
	while x >= 0 and y >= 0 and x < width and y < height:
		x += dx
		y += dy
		if x < 0 or y < 0 or x >= width or y >= height:
			break
		if inputdata[y][x] == "#":
			if found:
				s = list(inputdata[y])
				s[x] = "H"
				inputdata[y] = "".join(s)
			else:	
				found = True

def CountRemainingAsteroids():
	height = len(inputdata)
	width = len(inputdata[0])
	count = 0
	for x in range(width):
		for y in range(height):
			if inputdata[y][x] == "#":
				count += 1
	return count

def CalcVisibleAsteroids(x, y):
	maxdelta = 35
	ResetField()
	# print("Checking %d,%d" % (x, y))
	for dx in range(maxdelta):
		for dy in range(maxdelta):
			if dx == 0 and dy == 0:
				continue

			CheckAsteroidVisibility(x, y, dx, dy)
			CheckAsteroidVisibility(x, y, -dx, dy)
			CheckAsteroidVisibility(x, y, dx, -dy)
			CheckAsteroidVisibility(x, y, -dx, -dy)

	count = CountRemainingAsteroids() - 1
	# PrintField()
	# print("aantal: %d" % count)
	return count

def PrintField():
	print("")
	for line in inputdata:
		print(line)
	print("")
	input("Press...")

#########################################
#########################################

def PartA():
	print("Part A")

	# LoadTest1A()
	# LoadTest2A()
	# LoadTest3A()
	# LoadTest4A()

	bestx = -1
	besty = -1
	bestcount = -1

	height = len(inputdata)
	width = len(inputdata[0])
	for x in range(width):
		for y in range(height):
			if inputdata[y][x] == "#":
				count = CalcVisibleAsteroids(x, y)
				if count > bestcount:
					bestx, besty, bestcount = x, y, count

	print("Answer: (%d,%d) -> %d" % (bestx, besty, bestcount))

#########################################
#########################################

class PolarCoord():
	
	r = 0
	theta = 0

	def __init__(self, _cx, _cy, _x, _y):
		self.x = _x
		self.y = _y

		self.cx = _cx
		self.cy = _cy

		xx = -self.y + self.cy
		yy = self.x - self.cx

		self.r = math.sqrt(xx * xx + yy * yy)
		self.theta = math.atan2(yy, xx)
		if self.theta < 0.0:
			self.theta += math.tau

	def __repr__(self):
		return "(%d, %d)-(%d, %d) = %f %f (%f°)" % (self.cx, self.cy, self.x, self.y, self.r, self.theta, math.degrees(self.theta))

def FindPolarOfPosition(coords, x, y):
	for p in coords:
		if p.x == x and p.y == y:
			return p
	return None

def gcd(x, y):
	'''Greatest Common Divisor''' 
	while(y): 
		x, y = y, x % y 
	return x 

def PartB():
	print("Part B")

	# result from part A
	lposx = 20
	lposy = 20

	# LoadTest4A()
	# lposx = 11
	# lposy = 13

	# LoadTest5A()
	# lposx = 4
	# lposy = 5

	LoadTest6A()
	lposx = 8
	lposy = 3

	polarCoords = []

	height = len(inputdata)
	width = len(inputdata[0])
	for x in range(width):
		for y in range(height):
			if x == lposx and y == lposy:
				continue
			if inputdata[y][x] == "#":
				c = PolarCoord(lposx, lposy, x, y)
				polarCoords.append(c)

	# sorteren op afstand
	polarCoords.sort(key = lambda x: x.theta * 10 + x.r, reverse = False)

	for ix in range(len(polarCoords)):
		p = polarCoords[ix]
		# print("%d = " % (ix + 1), end = "")
		# print(p)

	for p in polarCoords:
		ii = 1

		ddx = (p.x - p.cx)
		ddy = (p.y - p.cy)

		# print(f"DDX: {ddx}  DDY: {ddy}")

		signx = math.copysign(1, ddx)
		signy = math.copysign(1, ddy)

		gecede = gcd(ddx, ddy)
		ddx = (ddx // gecede) * signx
		ddy = (ddy // gecede) * signy

		hit = False

		print(f"DDX: {ddx}  DDY: {ddy}")

		for i in range(1, 20):
			dx = ddx * i
			dy = ddy * i

			print(" DX: %d DY: %d i: %d" % (dx, dy, i))
			print(" X: %d  Y: %d" % (p.cx + dx, p.cy + dy))
			pp = FindPolarOfPosition(polarCoords, p.cx + dx, p.cy + dy)
			if pp != None:
				if hit:
					if pp.theta > math.tau:
						continue
					print(" Adding tau * %d" % i)
					pp.theta += (ii * math.tau)
					ii += 1
				else:
					hit = True
			else:
				# print("Not found")
				pass

			# input("Press...")

	# nu sorteren op angle
	polarCoords.sort(key = lambda x: x.theta, reverse = False)

	for ix in range(len(polarCoords)):
		p = polarCoords[ix]
		print("%d = " % (ix + 1), end = "")
		print(p)

	# n200 = polarCoords[199]
	# print(n200)
	# answer = n200.x * 100 + n200.y
	# print("Answer:", answer)

#########################################
#########################################

if __name__ == "__main__":
	print("Day 10")
	ReadInput()
	# PartA()
	PartB()
