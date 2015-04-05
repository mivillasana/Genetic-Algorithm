import math
import random

#Parameter Values
maxValue = 25
a = 0
b = 0
c = 0
d = 0
def f(a,b,c,d):
	return ((a+2*b+3*c+4*d)-30)

#step 1 and 2 Initialization and Evaluation
Chromosome1 = [a,b,c,d] = [random.randrange(maxValue),random.randrange(maxValue),random.randrange(maxValue),random.randrange(maxValue)]
F_obj1 = abs(f(a,b,c,d))
Fitness1 = 1/(1+F_obj1)
Chromosome2 = [a,b,c,d] = [random.randrange(maxValue),random.randrange(maxValue),random.randrange(maxValue),random.randrange(maxValue)]
F_obj2 = abs(f(a,b,c,d))
Fitness2 = 1/(1+F_obj2)
Chromosome3 = [a,b,c,d] = [random.randrange(maxValue),random.randrange(maxValue),random.randrange(maxValue),random.randrange(maxValue)]
F_obj3 = abs(f(a,b,c,d))
Fitness3 = 1/(1+F_obj3)
Chromosome4 = [a,b,c,d] = [random.randrange(maxValue),random.randrange(maxValue),random.randrange(maxValue),random.randrange(maxValue)]
F_obj4 = abs(f(a,b,c,d))
Fitness4 = 1/(1+F_obj4)
Chromosome5 = [a,b,c,d] = [random.randrange(maxValue),random.randrange(maxValue),random.randrange(maxValue),random.randrange(maxValue)]
F_obj5 = abs(f(a,b,c,d))
Fitness5 = 1/(1+F_obj5)
Chromosome6 = [a,b,c,d] = [random.randrange(maxValue),random.randrange(maxValue),random.randrange(maxValue),random.randrange(maxValue)]
F_obj6 = abs(f(a,b,c,d))
Fitness6 = 1/(1+F_obj6)

Total = Fitness1 + Fitness2 + Fitness3 + Fitness4 + Fitness5 + Fitness6

#print step 2 evaluation Evaluation Values
print("Printing Evaluation Values:")
print("Chromosome1 -",F_obj1,end='\n')
print("Chromosome2 -",F_obj2,end='\n')
print("Chromosome3 -",F_obj3,end='\n')
print("Chromosome4 -",F_obj4,end='\n')
print("Chromosome5 -",F_obj5,end='\n')
print("Chromosome6 -",F_obj6,end='\n')

#print step 3 Selection Values
print("\nPrinting Fitness Values:")
print("Chromosome1 -",Fitness1,end='\n')
print("Chromosome2 -",Fitness2,end='\n')
print("Chromosome3 -",Fitness3,end='\n')
print("Chromosome4 -",Fitness4,end='\n')
print("Chromosome5 -",Fitness5,end='\n')
print("Chromosome6 -",Fitness6,end='\n')

#print total fitness Value
print("\nPrinting Total Fitness Values:")
print(Total,end='\n')

#Calculate Probability for each Chromosome
P1 = Fitness1/Total
P2 = Fitness2/Total
P3 = Fitness3/Total
P4 = Fitness4/Total
P5 = Fitness5/Total
P6 = Fitness6/Total

#print Probability Values
print("\nPrinting Probability Values:")
print("Chromosome1 -",P1,end='\n')
print("Chromosome2 -",P2,end='\n')
print("Chromosome3 -",P3,end='\n')
print("Chromosome4 -",P4,end='\n')
print("Chromosome5 -",P5,end='\n')
print("Chromosome6 -",P6,end='\n')
