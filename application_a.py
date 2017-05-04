import csv
import operator
from classes import *
from helpers import *

# create list to put cargo1 classes in
cargo1_list = open_cargo_csv('CargoList1.csv')

print cargo1_list[0].valm3

# sort cargo1_list's kg from high to low and create new sorted list
cargo1_sorted = sorted(cargo1_list, key=operator.attrgetter('kg'), reverse=True)

# create a list with the four spacecrafts put into classes in it
spacecraft_list = open_spacecrafts_csv('Spacecrafts.csv')

print spacecraft_list[0].m3

# create lists to put cargo-classes in
spacecrafts = [[], [], [], []]

# run greedy fill, to fill spacecrafts on basis of kg
greedy_fill(spacecraft_list, cargo1_sorted, spacecrafts, 'kg')

# print kg's per spacecraft
print_kg(spacecraft_list, spacecrafts)

# hoeveel gewicht en ruimte blijft er over per spacecraft?
for j in range(4):
	print spacecraft_list[j].name
	sum_kg = 0
	sum_m3 = 0
	for i in range(len(spacecrafts[j])):
		sum_kg += spacecrafts[j][i].kg
		sum_m3 += spacecrafts[j][i].m3
	print sum_kg
	print sum_m3

