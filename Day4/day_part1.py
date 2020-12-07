import math, random, numpy as np 

input_file = open('C:\\Users\\Deep_Mamtora\\Documents\\Advent of Code 2020\\Day4\\day4_input.txt')


data = input_file.read()

for i in range(len(data)):
	passports = data.split('\n\n')

attributes = ['pid','hcl','ecl','eyr','byr','iyr','hgt']

count = 0
print(len(passports))
for i in range(len(passports)):
	flag = 1
	for j in range(len(attributes)):
		if attributes[j] in passports[i]:
			flag = flag*1
		else:
			flag = flag * 0


	if flag == 1:
		count = count+1



print(count)
