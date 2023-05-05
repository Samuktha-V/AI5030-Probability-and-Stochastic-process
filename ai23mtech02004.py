#importing essential libraries
import numpy as np
from fractions import Fraction

#initalising the sample space of dice 1
dice_1=[1,2,3,4,5,6]
#initalising the sample space of dice 2
dice_2=[1,1,2,2,3,3]
#initialising the dicionary to store the probabilty of each event. 
#Here, the key of the dictionary 'prob' represents the desired sum and the corresponding value represents the number of such occurences
prob={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}

#calculating the sample space 
sample_space=[]
for i in range(len(dice_1)):
  for j in range(len(dice_2)):
    sample_space.append((dice_1[i],dice_2[j]))
#total number of events in the sample space
n_S=len(sample_space)

#computing the events probability 
for i in range(len(dice_1)):
  for j in range(len(dice_2)):
    sum=dice_1[i]+dice_2[j]
    key=sum
    prob[key]=prob[key]+1

#printing the desired probablities
print("When the above two given dice are rolled \n")
for i in range(2,10):
  print(" The probablity of getting sum ",i," is",Fraction(prob[i],n_S))

