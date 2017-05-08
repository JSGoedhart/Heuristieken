import csv
import operator
from classes import *
from helpers import *

# create list to put cargo1 classes in
cargo3_list_kg = open_cargo_csv('CargoList3.csv')
cargo3_list_m3 = open_cargo_csv('CargoList3.csv')

# sort cargo3_list's kg from high to low and create new sorted list
cargo3_sorted_kg = sorted(cargo3_list_kg, key=operator.attrgetter('kg'), reverse=True)
cargo3_sorted_m3 = sorted(cargo3_list_m3, key=operator.attrgetter('m3'), reverse=True)

# create a list with the six spacecrafts put into classes in it
spacecraft_list = open_spacecrafts_csv('Spacecrafts2.csv')

spacecraft_list_sorted = sorted(spacecraft_list, key=operator.attrgetter('kg'), reverse=True)
# create lists to put cargo-classes in
spacecrafts_kg = [[], [], [], [], [], [], []]

# run greedy fill, to fill spacecrafts on basis of kg
greedy_fill(spacecraft_list, cargo3_sorted_kg, spacecrafts_kg, 'kg')

# create lists to put cargo-classes in
spacecrafts_m3 = []

leftover_list = cargo3_sorted_m3
count = 0
while len(leftover_list) != 0:
	count += 1 
	temp_spacecrafts = [[], [], [], [], [], [], []]
	temp_cargo = leftover_list
	greedy_fill(spacecraft_list, temp_cargo, temp_spacecrafts, 'm3')
	leftover_list = temp_spacecrafts[6]

	# print the leftoverlist
	# print 'leftoverlist:', count
	# for i in range(len(leftover_list)):
	# 	print leftover_list[i].m3

	spacecrafts_m3.append(temp_spacecrafts)

# for i in range(len(spacecrafts_m3)):
# 	print sum_m3(spacecrafts_m3[i])





# prints all cargo stored in spacecrafts
for k in range(len(spacecrafts_m3)):
	print 'spacecrafts:', k
	for j in range(6):
		print spacecraft_list[j].name
		for i in range(len(spacecrafts_m3[k][j])):
			print spacecrafts_m3[k][j][i].m3


# prints leftover with all NaN
# for i in range(count):
# 	print 'leftoverlist:', i
# 	for j in range(len(spacecrafts_m3[i][6])):
# 		print spacecrafts_m3[i][6][j].m3





