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
spacecrafts_kg = [[], [], [], [], [], []]

# run greedy fill, to fill spacecrafts on basis of kg
greedy_fill(spacecraft_list_sorted, cargo3_sorted_kg, spacecrafts_kg, 'kg', 'm3')

# create lists to put cargo-classes in
spacecrafts_fleet = []

leftover_list = cargo3_sorted_m3
count = 0
while len(leftover_list) != 0:
	count += 1 
	temp_spacecrafts = [[], [], [], [], [], []]
	temp_cargo = leftover_list
	greedy_fill(spacecraft_list_sorted, temp_cargo, temp_spacecrafts, 'm3', 'kg')
	leftover_list = temp_spacecrafts[5]
	spacecrafts_fleet.append(temp_spacecrafts)

# # prints all cargo stored in spacecrafts
# for k in range(len(spacecrafts_fleet)):
# 	print 'spacecrafts:', k
# 	for j in range(5):
# 		print spacecraft_list[j].name
# 		for i in range(len(spacecrafts_fleet[k][j])):
# 			print spacecrafts_fleet[k][j][i].m3

score_kg = 0
score_m3 = 0

# score function:
for k in range(len(spacecrafts_fleet)):
	for j in range(5):
		kg = 0
		m3 = 0
		for i in range(len(spacecrafts_fleet[k][j])):
			kg = kg + spacecrafts_fleet[k][j][i].kg
			m3 = m3 + spacecrafts_fleet[k][j][i].m3
		print kg
		print spacecraft_list_sorted[j].kg
		print m3
		print spacecraft_list_sorted[j].m3	
		weighted_kg = kg/spacecraft_list_sorted[j].kg
		weighted_m3 = m3/spacecraft_list_sorted[j].m3
		score_kg = score_kg + (1 - weighted_kg)
		score_m3 = score_m3 + (1 - weighted_m3)

print score_kg
print score_m3

# prints leftover with all NaN
# for i in range(count):
# 	print 'leftoverlist:', i
# 	for j in range(len(spacecrafts_m3[i][6])):
# 		print spacecrafts_m3[i][6][j].m3

# # random swappen

# number_fleet = range(len(spacecrafts_fleet))

# # select fleet
# rand_fleet = random.choice(number_fleet)
# number_spacecrafts = range(len(spacecrafts_fleet[rand_fleet]) - 1)

# # select spacecraft
# rand_spacecraft = random.choice(rand_fleet)

# # select item
# rand_item = random.choice(rand_spacecraft)

# # select fleet 2
# rand_fleet2 = random.choice(spacecrafts_fleet)

# # select spacecraft 2
# rand_spacecraft2 = random.choice(rand_fleet2)

# # select item 2
# rand_item2 = random.choice(rand_spacecraft2)

# spacecrafts_fleet[rand_fleet][rand_spacecraft][rand_item]

# # swap itemns
# spacecrafts_fleet[rand_fleet][rand_spacecraft][rand_item], spacecrafts_fleet[rand_fleet2][rand_spacecraft2][rand_item2] = swap(spacecrafts_fleet[rand_fleet][rand_spacecraft][rand_item], spacecrafts_fleet[rand_fleet2][rand_spacecraft2][rand_item2])

# spacecrafts_fleet[rand_fleet][rand_spacecraft][rand_item]

# # staat dit allemaal al in een functie?????????????






















