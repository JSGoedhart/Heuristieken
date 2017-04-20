import csv
import operator
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

for i in range(0,4):
	print spacecraft_list_sorted[i].name

# put cargo-items in list of spacecraft, when spacecraft is full, go to next
for j in range(0, 4):
	# define available mass in spacecraft
	m3_av = spacecraft_list_sorted[j].m3
	kg_av = spacecraft_list_sorted[j].kg
	for i in range(0, len(cargo1_sorted)):
		# check if cargo-item is already placed
		if (cargo1_sorted[i].m3 == 'nan'):
			next
		else:
			# put cargo-item in spacecraft if there is enough space
			if (cargo1_sorted[i].m3 <= m3_av and cargo1_sorted[i].kg <= kg_av):
				spacecrafts[j].append(cargo1(cargo1_sorted[i].number, cargo1_sorted[i].kg, cargo1_sorted[i].m3))
				m3_av = m3_av - cargo1_sorted[i].m3
				kg_av = kg_av - cargo1_sorted[i].kg
				cargo1_sorted[i].m3 = 'nan'
			# when item doesn't fit, try next
			else:
				next

leftover = []
# create leftover list from cargo1_sorted without nan
for i in range(0, len(cargo1_sorted)):
	if cargo1_sorted[i].m3 != 'nan':
		leftover.append(cargo1_sorted[i])

for i in range(0, len(leftover)):
	print leftover[i].m3

# define function to calculate #kg in spacecrafts
def sum_kg(lijst):
	kg_sum = []
	for i in range(0,4):
		kg_sum.append(sum(c.kg for c in lijst[i]))
	return kg_sum

def sum_m3(lijst):
	m3_sum = []
	for i in range(0,4):
		m3_sum.append(sum(c.m3 for c in lijst[i]))
	return m3_sum

val_leftover = sum(c.valtot for c in leftover)

# list with all cargo sorted in spacecrafts and leftover
spacecrafts.append(leftover)