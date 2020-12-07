import math, numpy, random

input_file = open('C:\\Users\\Deep_Mamtora\\Documents\\Advent of Code 2020\\Day3\\day3_input.txt')

map_file = input_file.readlines()


periodicity = len(map_file[10]) -1

x_step = 1
y_step = 2

x_pos = 1
y_pos = 0

count = 0

while y_pos < len(map_file):
	x_pos = x_pos + x_step
	if x_pos%periodicity != 0:
		if x_pos == periodicity:
			x_pos = periodicity
		else:
			x_pos = x_pos%periodicity
	
	y_pos = y_pos + y_step
	
	if y_pos<len(map_file):
		row = map_file[y_pos]
		if row[x_pos-1] =='#':
			count = count+1
			
		
		
			



print(count)
