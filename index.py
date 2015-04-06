import math
import random

#Parameter Values
maxValue = 25
a = 0
b = 0
c = 0
d = 0
Chromosome = [a,b,c,d]
F_obj = 0
Fit = 0
Total = 0
Chromosomes = [Chromosome,Chromosome,Chromosome,Chromosome,Chromosome,Chromosome]
F_objs= [F_obj,F_obj,F_obj,F_obj,F_obj,F_obj]
Fitness = [Fit,Fit,Fit,Fit,Fit,Fit]
def f(a,b,c,d):
	return ((a+2*b+3*c+4*d)-30)

#step 1 and 2 Initialization and Evaluation
index = 0
for index in range(len(Chromosomes)):
        Chromosomes[index] = [a,b,c,d] = [random.randrange(maxValue),random.randrange(maxValue),random.randrange(maxValue),random.randrange(maxValue)]
        F_objs[index] = abs(f(a,b,c,d))
        Fitness[index] = 1/(1+F_objs[index])
        print("Chromosomes Value for: ",index,"is\n", Chromosomes[index])
        print("F_obj Value for: ",index,"is\n", F_objs[index])
        print("Fitness Value for: ",index,"is\n", Fitness[index])
for index in range(len(Chromosomes)):
        Total += Fitness[index]


#print total fitness Value
print("\nPrinting Total Fitness Values:")
print(Total,end='\n')

#Calculate Probability for each Chromosome
#P1 = Fitness1/Total

