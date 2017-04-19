import csv
import operator
from classes import *
from helpers import *

# create list to put cargo1 classes in
cargo1_list = open_cargo_csv('CargoList1.csv')

# sort cargo1_list's kg from high to low and create new sorted list
cargo1_sorted = sorted(cargo1_list, key=operator.attrgetter('kg'), reverse=True)

# create a list with the four spacecrafts put into classes in it
#spacecraft_list = [spacecraft('cygnus', 2000, 18.9), spacecraft('verne', 2300, 13.1), spacecraft('progress', 2400, 7.6), spacecraft('kounotori', 5200, 14)]

spacecraft_list = open_spacecrafts_csv('Spacecrafts.csv')

print spacecraft_list[0].m3

# create lists to put cargo-classes in
spacecrafts = [[], [], [], []]

# put cargo-items in list of spacecraft, when spacecraft is full, go to next
for j in range(0, 4):
	# define available mass in spacecraft
	mass_av = spacecraft_list[j].kg
	for i in range(0, len(cargo1_sorted)):
		# check if cargo-item is already placed
		if (cargo1_sorted[i].kg == 'nan'):
			next
		else:
			# put cargo-item in spacecraft if there is enough space
			if (cargo1_sorted[i].kg <= mass_av):
				spacecrafts[j].append(cargo1(cargo1_sorted[i].number, cargo1_sorted[i].kg, cargo1_sorted[i].m3))
				mass_av -= cargo1_sorted[i].kg
				cargo1_sorted[i].kg = 'nan'
			# when item doesn't fit, try next
			else:
				next
	# print mass_av

# print kg's per spacecraft
for j in range(0, 4):
	print spacecraft_list[j].name
	for i in range(0, len(spacecrafts[j])):
		print spacecrafts[j][i].kg

# hoeveel gewicht en ruimte blijft er over per spacecraft?
for j in range(0, 4):
	print spacecraft_list[j].name
	sum_kg = 0
	sum_m3 = 0
	for i in range(0, len(spacecrafts[j])):
		sum_kg += spacecrafts[j][i].kg
		sum_m3 += spacecrafts[j][i].m3
	print sum_kg
	print sum_m3
