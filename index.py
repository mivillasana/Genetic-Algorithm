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

#step 1 Initialization
Chromosome1 = [a,b,c,d] = [random.randrange(maxValue),random.randrange(maxValue),random.randrange(maxValue),random.randrange(maxValue)]
F_obj1 = abs(f(a,b,c,d))
Chromosome2 = [a,b,c,d] = [random.randrange(maxValue),random.randrange(maxValue),random.randrange(maxValue),random.randrange(maxValue)]
F_obj2 = abs(f(a,b,c,d))
Chromosome3 = [a,b,c,d] = [random.randrange(maxValue),random.randrange(maxValue),random.randrange(maxValue),random.randrange(maxValue)]
F_obj3 = abs(f(a,b,c,d))
Chromosome4 = [a,b,c,d] = [random.randrange(maxValue),random.randrange(maxValue),random.randrange(maxValue),random.randrange(maxValue)]
F_obj4 = abs(f(a,b,c,d))
Chromosome5 = [a,b,c,d] = [random.randrange(maxValue),random.randrange(maxValue),random.randrange(maxValue),random.randrange(maxValue)]
F_obj5 = abs(f(a,b,c,d))
Chromosome6 = [a,b,c,d] = [random.randrange(maxValue),random.randrange(maxValue),random.randrange(maxValue),random.randrange(maxValue)]
F_obj6 = abs(f(a,b,c,d))
print(F_obj1,end='\n')
print(F_obj2,end='\n')
print(F_obj3,end='\n')
print(F_obj4,end='\n')
print(F_obj5,end='\n')
print(F_obj6,end='\n')
