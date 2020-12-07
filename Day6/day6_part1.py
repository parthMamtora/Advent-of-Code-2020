import math, random, numpy as np 

input_file = open('C:\\Users\\Deep_Mamtora\\Documents\\Advent of Code 2020\\Day6\\day6_input.txt')

customs_string = input_file.read()

customs = []

count = 0
i = 0
while count<len(customs_string):
	customs.append(customs_string.split('\n\n'))
	count = count + len(customs[i])
	i = i+1
print(customs[0][0])