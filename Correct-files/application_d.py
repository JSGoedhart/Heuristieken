import csv
import operator
from classes import *
from helpers_clean import *
from helpers_d import *

# create list to put cargo1 classes in
cargo3_list_kg = open_cargo_csv('CargoList3.csv')
cargo3_list_m3 = open_cargo_csv('CargoList3.csv')

# sort cargo3_list's kg from high to low and create new sorted list
cargo3_sorted_kg = sorted(cargo3_list_kg, key=operator.attrgetter('kg'), reverse=True)
cargo3_sorted_m3 = sorted(cargo3_list_m3, key=operator.attrgetter('m3'), reverse=True)

# create a list with the six spacecrafts put into classes in it
spacecraft_list = open_spacecrafts_csv('Spacecrafts2.csv')

# sort spacecrafts
spacecraft_list_sorted = sorted(spacecraft_list, key=operator.attrgetter('kg'), reverse=True)

##### choice between greedy with and greedy without the choice between america spacecraft
# # run greedy fill, to fill spacecrafts on basis of kg and m3
spacecrafts_fleet = greedy_fleet(spacecraft_list_sorted, cargo3_sorted_m3)

# # greedy with choice america
# spacecrafts_fleet = greedy_fleet_with_america_check(spacecraft_list, cargo3_sorted_kg)
#####


##### choice between hillclimbing and simulated annealing
# # run hillclimbing to reduce wasted space
# spacecrafts_fleet = hillclimbing_fleet(spacecrafts_fleet, spacecraft_list_sorted)

# # run simulated annealing to reduce wasted space
spacecrafts_fleet = annealing_fleet(spacecrafts_fleet, spacecraft_list_sorted)
#####

# score
scorefunction(spacecrafts_fleet, spacecraft_list_sorted)






















