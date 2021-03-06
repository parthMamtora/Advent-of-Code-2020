import math, random, numpy as np 

input_file = open('C:\\Users\\Deep_Mamtora\\Documents\\Advent of Code 2020\\Day5\\day5_input.txt')


seats = input_file.readlines()


row_id = []
column_id = []

for i in range(len(seats)):
	seat_string = seats[i]
	b = []
	c = []

	for j in range(7):
		b.append(seat_string[j])
	row_id.append(b)
	

	for k in range(7,10):
		c.append(seat_string[k])
	column_id.append(c)	


#determining the seat

def binary_search(seat_list,lower,upper):
	upper_bound = (2**len(seat_list))-1
	lower_bound = 0
	middle = 2**len(seat_list)

	for i in range(len(seat_list)):
		if seat_list[i] == lower:
			middle = (middle)/2
			upper_bound = lower_bound+middle-1
			execution = lower_bound
	
		else:
			middle = (middle)/2
			lower_bound = upper_bound - middle+1
			execution = upper_bound
		

	return(execution)





row = []
col = []
for i in range(len(row_id)):
	rnum = binary_search(row_id[i],'F','B')
	row.append(rnum)

	cnum = binary_search(column_id[i],'L','R')
	col.append(cnum)


dictionary = dict(zip(row,col))

seat_id = []

for i in range(len(row)):
	id_num = 0
	id_num = row[i]*8 + (col[i])
	seat_id.append(id_num)



seat_id.sort()
print(seat_id)







