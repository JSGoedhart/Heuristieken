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

spacecraft_list_sorted = sorted(spacecraft_list, key=operator.attrgetter('kg'), reverse=True)


######## fill just one spacecraft ########
# # run greedy fill, to fill spacecrafts on basis of kg and m3
# spacecrafts_fleet = greedy_fleet(spacecraft_list_sorted, cargo3_sorted_m3)

##### choice between hillclimbing and simulated annealing
# # run hillclimbing to reduce wasted space
# spacecrafts_fleet = hillclimbing_fleet(spacecrafts_fleet, spacecraft_list_sorted)

# # run simulated annealing to reduce wasted space
# spacecrafts_fleet = annealing_fleet(spacecrafts_fleet, spacecraft_list_sorted)
#####
###########


########### chose the best spacecraft every time ########
# chose the best and run greedy
greedy = greedy_fleet_with_check(spacecraft_list_sorted, cargo3_sorted_kg)

numbers_fleet = greedy[1]
spacecrafts_fleet = greedy[0]

##### choice between hillclimbing and simulated annealing
# annealing
spacecrafts_fleet = annealing_fleet(spacecrafts_fleet, spacecraft_list_sorted, numbers_fleet)

# # run hillclimbing to reduce wasted space
# spacecrafts_fleet = hillclimbing_fleet(spacecrafts_fleet, spacecraft_list_sorted, numbers_fleet)
#####
############

# score
scorefunction(spacecrafts_fleet, spacecraft_list_sorted)