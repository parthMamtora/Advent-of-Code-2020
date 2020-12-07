import math, random, numpy as np

input_file = open('C:\\Users\\Deep_Mamtora\\Documents\\Advent of Code 2020\\day1_input.txt')

numbers = input_file.readlines()
num =[]
for i in range(len(numbers)):
	num.append(int(numbers[i]))

dictionary = {}
for i in range(len(num)):
	dictionary[num[i]] = True

for i in range(len(num)):
	compliment = 2020-num[i]
	for j in range(i,len(num)):
		flag = compliment -num[j]
		if dictionary.get(flag)!=None:
			print(num[i]*num[j]*flag)



