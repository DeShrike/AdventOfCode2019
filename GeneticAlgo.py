import random
from random import random as rnd

def CumSum(array):
    result = []
    som = 0
    for x in array:
        som += x
        result.append(som)

    return result

def roulette(cum_sum, chance):
    veriable = list(cum_sum.copy())
    veriable.append(chance)
    veriable = sorted(veriable)
    return veriable.index(chance)

class Individual():

    genes = []
    fitness = 0

    def __init__(self, g):
        self.fitness = 0
        self.genes = [x for x in g]


class GeneticAlgo():

    population = None
    populationssize = 100
    mutationrate = 0.1

    def __init__(self):
        self.population = []
    
    def RunGeneration(self):
        pass
    
    def Select(self):
        som = sum([p.fitness for p in self.population])
        normalizedFitness = sorted( [ self.population[x].fitness / som for x in range(len(self.population)) ], reverse = True)
        cumulativeSum = CumSum(normalizedFitness )

        selected = []
        for x in range(len(self.population)//2):
            selected.append(roulette(cumulativeSum, rnd()))
            while len(set(selected)) != len(selected):
                selected[x] = (roulette(cumulativeSum, rnd()))
            selected = { 'Individuals': [self.population[int(selected[x])]
                for x in range(len(self.population)//2)] 
                ,'Fitness': [self.population[int(selected[x])].fitness
                for x in range(len(self.population) // 2) ] }

    def Mutate(self):
        pass

    def Crossover(self):
        pass
