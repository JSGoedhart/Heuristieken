from classes import *

def open_cargo_csv(file):
    # create list to put cargo1 classes in
    split_list = []

    # put cargo-elements of list 1 in class cargo1
    csvfile = open(file, 'r')
    for line in csvfile:
    	split = line.split(';')
    	var0 = split[0]
    	var1 = int(split[1])
    	var2 = float(split[2][:-1])
    	split_list.append(cargo1(var0, var1, var2))
    return split_list

def open_spacecrafts_csv(file):
    # create empty list for spacecrafts
    open_list = []

    # put spacecrafts in empty list
    csvfile = open(file, 'r')
    for line in csvfile:
        split = line.split(';')
        var0 = split[0]
        var1 = int(split[1])
        var2 = float(split[2])
        open_list.append(spacecraft(var0, var1, var2))
    return open_list

def greedy_fill(list1, list2, list3):

    for j in range(4):
    	# define available mass in spacecraft
    	mass_av = list1[j].kg
    	for i in range(len(list2)):
    		# check if cargo-item is already placed
    		if (list2[i].kg != 'nan'):
    			if (list2[i].kg <= mass_av):
    				list3[j].append(cargo1(list2[i].number, list2[i].kg, list2[i].m3))
    				mass_av -= list2[i].kg
    				list2[i].kg = 'nan'

def print_kg(list1, list2):
    # print kg's per spacecraft
    for j in range(4):
    	print list1[j].name
    	for i in range(len(list2[j])):
    		print list2[j][i].kg

# def availability(list1, list2):
#     for j in range(4):
#     	print list1[j].name
#     	sum_kg = 0
#     	sum_m3 = 0
#     	for i in range(len(list2[j])):
#     		sum_kg += list2[j][i].kg
#     		sum_m3 += list2[j][i].m3
#     	print sum_kg
#     	print sum_m3
