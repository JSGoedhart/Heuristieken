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
    
# def fill_spacecrafts:
#     # create a list with the four spacecrafts put into classes in it
#     spacecraft_list = [spacecraft('cygnus', 2000, 18.9), spacecraft('verne', 2300, 13.1), spacecraft('progress', 2400, 7.6), spacecraft('kounotori', 5200, 14)]
#
#     # create lists to put cargo-classes in
#     spacecrafts = [[], [], [], []]
#
#     csvfile = open(file, 'r')
#     for line in csvfile:
#     	split = line.split(';')
#     	var0 = split[0]
#     	var1 = int(split[1])
#     	var2 = float(split[2][:-1])
#     	cargo1_list.append(cargo1(var0, var1, var2))
#
#     # put cargo-items in list of spacecraft, when spacecraft is full, go to next
#     for j in range(0, 4):
#     	# define available mass in spacecraft
#     	mass_av = spacecraft_list[j].kg
#     	for i in range(0, len(cargo1_sorted)):
#     		# check if cargo-item is already placed
#     		if (cargo1_sorted[i].kg == 'nan'):
#     			next
#     		else:
#     			# put cargo-item in spacecraft if there is enough space
#     			if (cargo1_sorted[i].kg <= mass_av):
#     				spacecrafts[j].append(cargo1(cargo1_sorted[i].number, cargo1_sorted[i].kg, cargo1_sorted[i].m3))
#     				mass_av -= cargo1_sorted[i].kg
#     				cargo1_sorted[i].kg = 'nan'
#     			# when item doesn't fit, try next
#     			else:
#     				next
