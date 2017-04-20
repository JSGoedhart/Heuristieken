import csv
import operator
import random
from classes import *
from helpers import *

# create list to put cargo1 classes in
cargo1_list = open_cargo_csv('CargoList1.csv')

# sort cargo1_list's m3 from high to low and create new sorted list
cargo1_sorted = sorted(cargo1_list, key=operator.attrgetter('m3'), reverse=True)

# create a list with the four spacecrafts put into classes in it
#spacecraft_list = [spacecraft('cygnus', 2000, 18.9), spacecraft('verne', 2300, 13.1), spacecraft('progress', 2400, 7.6), spacecraft('kounotori', 5200, 14)]

spacecraft_list = open_spacecrafts_csv('Spacecrafts.csv')

spacecraft_list_sorted = sorted(spacecraft_list, key=operator.attrgetter('kg'), reverse=True)
# create lists to put cargo-classes in
spacecrafts = [[], [], [], []]

# put cargo-items in list of spacecraft, when spacecraft is full, go to next
for j in range(3, 0, -1):
	# define available mass in spacecraft
	m3_av = spacecraft_list_sorted[j].m3
	for i in range(0, len(cargo1_sorted)):
		# check if cargo-item is already placed
		if (cargo1_sorted[i].m3 == 'nan'):
			next
		else:
			# put cargo-item in spacecraft if there is enough space
			if (cargo1_sorted[i].m3 <= m3_av):
				spacecrafts[j].append(cargo1(cargo1_sorted[i].number, cargo1_sorted[i].kg, cargo1_sorted[i].m3))
				m3_av = m3_av - cargo1_sorted[i].m3
				cargo1_sorted[i].m3 = 'nan'
			# when item doesn't fit, try next
			else:
				next
	# print mass_av

# print kg's per spacecraft
for j in range(0, 4):
	print spacecraft_list[j].name
	for i in range(0, len(spacecrafts[j])):
		print spacecrafts[j][i].m3

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


# verwijder 'nan' uit overgebleven sorted list
cargo1_rest = []

for i in range(0, len(cargo1_sorted)):
	if (cargo1_sorted[i].m3 != 'nan'):
		cargo1_rest.append(cargo1_sorted[i])
	else:
		next

# print cargo1_rest
for i in range(0, len(cargo1_rest)):
	print cargo1_rest[i].m3

# lijst met spacecrafts cargo en overige cargo
spacecrafts.append(cargo1_rest)

print random.choice(spacecrafts[2])









