import math
import random

#Parameter Values
maxValue = 25
a = 0
b = 0
c = 0
d = 0
F_obj = 0
Fit = 0
Total = 0
prob = 0
cummulative = 0
ran = 0
Chromosome = [a,b,c,d]
Chromosomes = [Chromosome,Chromosome,Chromosome,Chromosome,Chromosome,Chromosome]
F_objs= [F_obj,F_obj,F_obj,F_obj,F_obj,F_obj]
Fitness = [Fit,Fit,Fit,Fit,Fit,Fit]
P = [prob,prob,prob,prob,prob,prob]
C = [cummulative,cummulative,cummulative,cummulative,cummulative,cummulative]
R = [ran, ran, ran, ran, ran, ran]
def f(a,b,c,d):
	return ((a+2*b+3*c+4*d)-30)

#step 1, 2, and 3 Initialization, Evaluation and Selection
index = 0
for index in range(len(Chromosomes)):
        Chromosomes[index] = [a,b,c,d] = [random.randrange(maxValue),random.randrange(maxValue),random.randrange(maxValue),random.randrange(maxValue)]
        F_objs[index] = abs(f(a,b,c,d))
        Fitness[index] = 1/(1+F_objs[index])
        print("Chromosomes[",index,"] is: ", Chromosomes[index])
        print("F_obj[",index,"] is: ", F_objs[index])
        print("Fitness[",index,"] is: ", Fitness[index],"\n")
for index in range(len(Chromosomes)):
        Total += Fitness[index]
        
#print total fitness Value
print("\nPrinting Summed Fitness Values:",Total,end='\n\n')

#Calculate Probability for each Chromosome
index = 0
for index in range(len(P)):
       P[index] = Fitness[index]/Total
       print("Probability Value for ",index,"is: ", P[index],"\n")

#Calculate Cummlative probability of selection process
##
##

#Calculate Random number R in the range 0-1 
index = 0
for index in range(len(R)):
       R[index] = random.randrange(0,1,.1)
       print("Random Value for ",index,"is: ", R[index],"\n")
