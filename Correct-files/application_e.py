import csv
import operator
from classes import *
from helpers_clean import *
from helpers_e import *

# create list to put cargo1 classes in
cargo3_list_kg = open_cargo_csv('CargoList3.csv')
cargo3_list_m3 = open_cargo_csv('CargoList3.csv')

# sort cargo3_list's kg from high to low and create new sorted list
cargo3_sorted_kg = sorted(cargo3_list_kg, key=operator.attrgetter('kg'), reverse=True)
cargo3_sorted_m3 = sorted(cargo3_list_m3, key=operator.attrgetter('m3'), reverse=True)

# create a list with the six spacecrafts put into classes in it
spacecraft_list = open_spacecrafts_csv('Spacecrafts_e.csv')

spacecraft_list_sorted = sorted(spacecraft_list, key=operator.attrgetter('m3'), reverse=True)


######## fill just one spacecraft ########

# # run greedy fill, to fill spacecrafts on basis of kg and m3
# spacecrafts_fleet = greedy_fleet(spacecraft_list_sorted, cargo3_sorted_m3)

# # run hillclimbing to reduce wasted space
# spacecrafts_fleet = hillclimbing_fleet(spacecrafts_fleet, spacecraft_list_sorted)

# # run simulated annealing to reduce wasted space
# spacecrafts_fleet = annealing_fleet(spacecrafts_fleet, spacecraft_list_sorted)

# for i in range(len(spacecrafts_fleet)):
#     print "vloot", i
#     for j in range(len(spacecrafts_fleet[i])):
#         print len(spacecrafts_fleet[i][j])

# print spacecrafts_fleet[len(spacecrafts_fleet)-2][0][0].m3

# print sum_kg(spacecrafts_fleet[len(spacecrafts_fleet)-1])
# print sum_m3(spacecrafts_fleet[len(spacecrafts_fleet)-1])
# print sum_kg(spacecrafts_fleet[len(spacecrafts_fleet)-2])
# print sum_m3(spacecrafts_fleet[len(spacecrafts_fleet)-2])

###########


########### chose the best spacecraft every time ########

# chose the best and run greedy
spacecrafts_fleet = greedy_fleet_with_check(spacecraft_list_sorted, cargo3_sorted_m3)

for i in range(len(spacecrafts_fleet)):
	print "vloot", i
	for j in range(len(spacecrafts_fleet[i])):
		print "spacecraft", j
		for k in range(len(spacecrafts_fleet[i][j])):
			print spacecrafts_fleet[i][j][k]

# annealing
spacecrafts_fleet = annealing_fleet(spacecrafts_fleet, spacecraft_list_sorted)

# score
scorefunction(spacecrafts_fleet, spacecraft_list_sorted)