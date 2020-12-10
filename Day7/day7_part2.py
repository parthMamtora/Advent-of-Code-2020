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



def lookup(dicton,bagcolor,num_bags,sums):
	bag_list = dicton[bagcolor]
	if bag_list[0][1] == 0:
		return(sums)
	else:
		list_numbags = num_bags
		for j in range(len(bag_list)):
			sums = sums + bag_list[j][0]*list_numbags
			sums = lookup(dicton,bag_list[j][1],list_numbags*bag_list[j][0],sums)
			
		return(sums)

			

	
count = 0

gold_bags = dictionary['shinygoldbag']

for i in range(len(gold_bags)):
	if gold_bags[i][1]!='shinygoldbag':
		bags_within = lookup(dictionary,gold_bags[i][1],gold_bags[i][0],gold_bags[i][0])
		count = count + bags_within

print(count)

