import math, random, numpy as np 

input_file = open('C:\\Users\\Deep_Mamtora\\Documents\\Advent of Code 2020\\Day7\\day7_input.txt')

rules = input_file.readlines()

#parsing
def bagtree(bagdata):
	bagdata = bagdata.replace(' ','')
	bagdata = bagdata.replace('.','')
	bagdata = bagdata.replace('\n','')

	data = bagdata.split('contain')

	if 'bags' in data[0]:
		key = data[0].replace('bags','bag')
	else:
		key = data[0]


	if 'nootherbags' in data[1]:
		values =[[0,0]]
	else:
		value_data = data[1].split(',')
		values = []

		for i in range(len(value_data)):
			num = int(value_data[i][0])

			bag = value_data[i].lstrip(str(num))
			if 'bags' in bag:
				bag = bag.replace('bags','bag')

			values.append([num,bag])


	return(key,values)



#creating dictionary
dictionary = {}
key_list = []
for i in range(len(rules)):
	key, value = bagtree(rules[i])
	dictionary[key] = value
	key_list.append(key)



def lookup(dicton,bagcolor,color):

	bag_list = dicton[bagcolor]
	if bag_list[0][1] == 0:
		return(False)
	else:
		for j in range(len(bag_list)):
			if color in bag_list[j][1]:
				return(True)
			else:
				flag = lookup(dicton,bag_list[j][1],color)
				if flag == True:
					return(True)

	
count = 0
for i in range(len(key_list)):
	a = lookup(dictionary,key_list[i],'shinygoldbag')
	if a == True:
		count = count+1

print(count)





