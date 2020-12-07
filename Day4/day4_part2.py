import math, random, numpy as np 

input_file = open('C:\\Users\\Deep_Mamtora\\Documents\\Advent of Code 2020\\Day4\\day4_input.txt')


data = input_file.read()

for i in range(len(data)):
	passports = data.split('\n\n')

attributes = ['pid','hcl','ecl','eyr','byr','iyr','hgt']

count = 0
dictionary = []

for i in range(len(passports)):
	
	pass_list =[]
	subpass_list =[]

	pass_list = passports[i].split('\n')
	for j in range(len(pass_list)):
		temp = []
		temp = pass_list[j].split(' ')
		for k in range(len(temp)):
			subpass_list.append(temp[k])


	dictionary.append(subpass_list)


pass_dictionary = {}
for i in range(len(dictionary)):
	key = []
	value = []
	for j in range(len(dictionary[i])):
		obj = []
		obj = dictionary[i][j].split(':')
		key.append(obj[0])
		value.append(obj[1])


	pass_dictionary[i] = dict(zip(key,value))

#test conditions

count = 0
for i in range(len(dictionary)):
	flag = 1
	for j in range(len(attributes)):
		if pass_dictionary[i].get(attributes[j])!= None:
			flag = flag *1
		else:
			flag = 0

	if flag == 1:
		#condtion1
		if int(pass_dictionary[i]['byr'])>=1920 and int(pass_dictionary[i]['byr'])<= 2002:
			flag = flag*1
		else:
			flag = 0


		#condition 2
		if int(pass_dictionary[i]['iyr']) >= 2010 and int(pass_dictionary[i]['iyr'])<= 2020:
			flag = flag*1
		else:
			flag = 0


		#conditionn3
		if int(pass_dictionary[i]['eyr']) >= 2020 and int(pass_dictionary[i]['eyr'])<=2030:
			flag = flag*1
		else:
			flag = 0

		#condition 4
		if len(pass_dictionary[i]['pid']) == 9:
			flag = flag*1
		else:
			flag = 0

		#condition 5
		if len(pass_dictionary[i]['hcl']) == 7:
			if pass_dictionary[i]['hcl'][0] =='#':
				hexa_characters = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
				for j in range(len(pass_dictionary[i]['hcl'])-1):
					if hexa_characters.__contains__(pass_dictionary[i]['hcl'][j+1]):
						flag = flag*1
					else:
						flag = 0
			else:
				flag = 0
		else:
			flag = 0



		#condition 6
		eye_colors =['amb', 'blu', 'brn','gry','grn','hzl','oth']
		check = False
		for k in range(len(eye_colors)):

			if pass_dictionary[i]['ecl']==eye_colors[k]:
				check = True
			else:
				check = False or check
		if check == True:
			flag = flag*1
		else:
			flag = 0


		#condition 7
		if pass_dictionary[i]['hgt'].__contains__('cm') or pass_dictionary[i]['hgt'].__contains__('in'):
			if pass_dictionary[i]['hgt'].__contains__('cm'):
				height = int(pass_dictionary[i]['hgt'].split('cm')[0])
				if height>=150 and height <=193:
					flag = flag*1
				else:
					flag = 0
			else:
				height = int(pass_dictionary[i]['hgt'].split('in')[0])
				if height>=59 and height<=76:
					flag = flag*1
				else:
					flag = 0
		else:
			flag = 0



	if flag == 1:
		count = count+1




print(count)



