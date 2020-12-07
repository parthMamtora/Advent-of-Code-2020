import math, random, numpy as np

password_file = open('C:\\Users\\Deep_Mamtora\\Documents\\Advent of Code 2020\\Day2\\day2_input.txt')

passwords = password_file.readlines()

def parsing(pass_string):
	fragments = pass_string.split('-')
	minima = int(fragments[0])
	piece = fragments[1].split(' ')
	maxima = int(piece[0])
	speck = piece[1].split(':')
	letter = speck[0]
	password = piece[2]
	#testing
	count = 0
	for i in range(len(password)):
		if letter == password[i]:
			count = count+1

	if count<=maxima and count>=minima:
		value = True
	else:
		value = False
	return(value)

count = 0
for i in range(len(passwords)):
	if parsing(passwords[i]) == True:
		count = count+1

print(count)
