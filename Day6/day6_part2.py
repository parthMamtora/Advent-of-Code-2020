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


def intersections(board):
	check_string = board[0]
	for j in range(len(board)-1):
		if len(check_string)> 0:
			temp = ''
			for k in range(len(check_string)):

				if check_string[k] in board[j+1]:
					temp = temp + check_string[k]

			check_string = temp


	if len(check_string) == 0:
		return(0)
	else:
		return(len(check_string))



count = 0
for i in range(len(master_list)):
	count = count + intersections(master_list[i])



print(count)
