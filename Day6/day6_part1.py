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

count = 0
master_list = []
for i in range(len(customs[0])):
	a = customs[0][i].split('\n')
	master_list.append(a)
	string = ''
	for j in range(len(master_list[i])):
		string = string + master_list[i][j]


	count = len(set(string)) + count


print(count)


	
