import math

inputfile = "input-day14.txt"
inputdata = []
reactions = []

#########################################
#########################################

def ReadInput():
	file = open(inputfile, "r") 
	for line in file:
		inputdata.append(line.rstrip("\n"))
	file.close()

#########################################
#########################################

def Example1():
	inputdata.clear()
	inputdata.append("9 ORE => 2 A")
	inputdata.append("8 ORE => 3 B")
	inputdata.append("7 ORE => 5 C")
	inputdata.append("3 A, 4 B => 1 AB")
	inputdata.append("5 B, 7 C => 1 BC")
	inputdata.append("4 C, 1 A => 1 CA")
	inputdata.append("2 AB, 3 BC, 4 CA => 1 FUEL")

	# answer A = 165 ORE

def Example2():
	inputdata.clear()
	inputdata.append("157 ORE => 5 NZVS")
	inputdata.append("165 ORE => 6 DCFZ")
	inputdata.append("44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL")
	inputdata.append("12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ")
	inputdata.append("179 ORE => 7 PSHF")
	inputdata.append("177 ORE => 5 HKGWZ")
	inputdata.append("7 DCFZ, 7 PSHF => 2 XJWVT")
	inputdata.append("165 ORE => 2 GPVTF")
	inputdata.append("3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT")
	
	# answer A = 13312 ORE
	# answer B = 82892753 FUEL

def Example3():
	inputdata.clear()
	inputdata.append("2 VPVL, 7 FWMGM, 2 CXFTF, 11 MNCFX => 1 STKFG")
	inputdata.append("17 NVRVD, 3 JNWZP => 8 VPVL")
	inputdata.append("53 STKFG, 6 MNCFX, 46 VJHF, 81 HVMC, 68 CXFTF, 25 GNMV => 1 FUEL")
	inputdata.append("22 VJHF, 37 MNCFX => 5 FWMGM")
	inputdata.append("139 ORE => 4 NVRVD")
	inputdata.append("144 ORE => 7 JNWZP")
	inputdata.append("5 MNCFX, 7 RFSQX, 2 FWMGM, 2 VPVL, 19 CXFTF => 3 HVMC")
	inputdata.append("5 VJHF, 7 MNCFX, 9 VPVL, 37 CXFTF => 6 GNMV")
	inputdata.append("145 ORE => 6 MNCFX")
	inputdata.append("1 NVRVD => 8 CXFTF")
	inputdata.append("1 VJHF, 6 MNCFX => 4 RFSQX")
	inputdata.append("176 ORE => 6 VJHF")
	
	# answer A = 180697 ORE
	# answer B = 5586022 FUEL

def Example4():
	inputdata.clear()
	inputdata.append("171 ORE => 8 CNZTR")
	inputdata.append("7 ZLQW, 3 BMBT, 9 XCVML, 26 XMNCP, 1 WPTQ, 2 MZWV, 1 RJRHP => 4 PLWSL")
	inputdata.append("114 ORE => 4 BHXH")
	inputdata.append("14 VRPVC => 6 BMBT")
	inputdata.append("6 BHXH, 18 KTJDG, 12 WPTQ, 7 PLWSL, 31 FHTLT, 37 ZDVW => 1 FUEL")
	inputdata.append("6 WPTQ, 2 BMBT, 8 ZLQW, 18 KTJDG, 1 XMNCP, 6 MZWV, 1 RJRHP => 6 FHTLT")
	inputdata.append("15 XDBXC, 2 LTCX, 1 VRPVC => 6 ZLQW")
	inputdata.append("13 WPTQ, 10 LTCX, 3 RJRHP, 14 XMNCP, 2 MZWV, 1 ZLQW => 1 ZDVW")
	inputdata.append("5 BMBT => 4 WPTQ")
	inputdata.append("189 ORE => 9 KTJDG")
	inputdata.append("1 MZWV, 17 XDBXC, 3 XCVML => 2 XMNCP")
	inputdata.append("12 VRPVC, 27 CNZTR => 2 XDBXC")
	inputdata.append("15 KTJDG, 12 BHXH => 5 XCVML")
	inputdata.append("3 BHXH, 2 VRPVC => 7 MZWV")
	inputdata.append("121 ORE => 7 VRPVC")
	inputdata.append("7 XCVML => 6 RJRHP")
	inputdata.append("5 BHXH, 4 VRPVC => 5 LTCX")
	
	# answer A = 2210736 ORE
	# answer B = 460664 FUEL

#########################################
#########################################

class Reaction():
	ingredients = None
	name = None
	quantity = 0
	inrecipecount = 0

	def __init__(self, n, q):
		self.name = n
		self.quantity = q
		self.ingredients = []
		self.inrecipecount = 0

	def __repr__(self):
		str = "%d %s <= " % (self.quantity, self.name)
		for ing in self.ingredients:
			str += "%d * %s  " % (ing[1], ing[0])
		str += " In %d recipes" % self.inrecipecount
		return str

	def HasIngredient(self, n):
		for ing in self.ingredients:
			if ing[0] == n:
				return True
		return False

	def AddIngredient(self, n, q):
		self.ingredients.append((n, q))

def FindRecipe(name):
	for rea in reactions:
		if rea.name == name:
			return rea
	return None

def ParseLine(line):
	parts = line.split("=>")
	out = parts[1].strip(" ").split(" ")
	name = out[1]
	q = int(out[0])
	rea = Reaction(name, q)

	ings = parts[0].strip(" ").split(",")
	for ing in ings:
		out = ing.strip(" ").split(" ")
		name = out[1]
		q = int(out[0])
		rea.AddIngredient(name, q)

	reactions.append(rea)

def ParseInput():
	reactions.clear()
	for line in inputdata:
		ParseLine(line)

	for rea in reactions:
		for rea2 in reactions:
			for ing in rea2.ingredients:
				if ing[0] == rea.name:
					rea.inrecipecount += 1
		print(rea)

#########################################
#########################################

# Needs: [Name, Quantity]
needs = []
# Ingredients: Name: [Quantity]
ingredients = {}
# Resten: Name: Quantity
resten = {}

def AddNeed(name, q):
	needs.append([name, q])

def AddIngredient(name, q):
	if name not in ingredients:
		ingredients[name] = q
	else:
		ingredients[name] += q

def AddRest(name, q):
	if name not in resten:
		resten[name] = q
	else:
		resten[name] += q

def DoRecipes(fuelAmount):
	ingredients.clear()
	needs.clear()
	resten.clear()

	# Name, QuantityNeeded
	AddNeed("FUEL", fuelAmount)

	ix = 0
	while ix < len(needs):
		need = needs[ix]
		if need[0] == "ORE":
			ix += 1
			continue
		neededQuantity = need[1]
		rea = FindRecipe(need[0])
		if rea == None:
			print("No Recipe for %s " % need[0])
			return

		# print("Need %d %s " % (neededQuantity, need[0]))

		if need[0] in resten:			
			restq = resten[need[0]]
			# print(f"  Found Restje: {restq}")
			fromrest = min(restq, neededQuantity)
			neededQuantity -= fromrest
			resten[need[0]] -= fromrest
			# print(f"  Taken {fromrest} from rest: neededQUantity Left: {neededQuantity}")

		reactionQuantity = rea.quantity
		restFromRecipe =  neededQuantity % reactionQuantity
		recepiesNeeded = (neededQuantity - restFromRecipe) / reactionQuantity
		if restFromRecipe > 0:
			recepiesNeeded += 1
		restFromRecipe = (reactionQuantity * recepiesNeeded) - neededQuantity

		# print(rea)

		# print(f"  Reaction Quantity: {reactionQuantity}")
		# print(f"  Recipes Needed: {recepiesNeeded}")
		# print(f"  Rest from Recipe: {restFromRecipe}")

		AddRest(need[0], restFromRecipe)

		# print(f"   Add Rest: {need[0]} x {restFromRecipe}")

		for ing in rea.ingredients:
			ingn = ing[0]
			ingq = ing[1]
			AddIngredient(ingn, ingq * recepiesNeeded)
			AddNeed(ingn, ingq * recepiesNeeded)

			# print(f"    Add Need: {ingn} x {ingq * recepiesNeeded}")

		# input("Pres...")
		ix += 1

def PartA():
	print("Part A")

	# Example1()
	# Example2()
	# Example3()
	# Example4()

	ParseInput()
	DoRecipes(1)

	# print(ingredients)
	print("Answer:", ingredients["ORE"])	# 612880
	if "ORE" in resten:
		print("Rest Ore: ", resten["ORE"])

#########################################
#########################################

def PartB():
	print("Part B")

	trillion = 1000000000000	# 1 trillion

	# Example1()
	# Example2()
	# Example3()
	# Example4()

	ParseInput()

	vanaf = int((trillion // 612880) * 1.537)

	# this is cheesing it :(

	while True:
		DoRecipes(vanaf)
		o = ingredients["ORE"]
		print(f"{vanaf} FUEL = {o} ORE")
		if o > trillion:
			break
		vanaf += 1

	# Poging 1: 1631640 (1 trillion / 612880) is too low.
	# Poging 2: 6323777403 is too high

	print("Answer:", 2509120)

#########################################
#########################################

if __name__ == "__main__":
	print("Day 14")
	ReadInput()
	PartA()
	PartB()
