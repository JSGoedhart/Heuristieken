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

# run greedy fill, to fill spacecrafts on basis of kg and m3
spacecrafts_fleet = greedy_fleet(spacecraft_list_sorted, cargo3_sorted_m3)

# score
scorefunction(spacecrafts_fleet, spacecraft_list_sorted)
























