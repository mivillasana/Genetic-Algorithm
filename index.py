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
print(F_obj1,end='\n')
print(F_obj2,end='\n')
print(F_obj3,end='\n')
print(F_obj4,end='\n')
print(F_obj5,end='\n')
print(F_obj6,end='\n')

#print step 3 Selection Values
print(Fitness1,end='\n')
print(Fitness2,end='\n')
print(Fitness3,end='\n')
print(Fitness4,end='\n')
print(Fitness5,end='\n')
print(Fitness6,end='\n')
