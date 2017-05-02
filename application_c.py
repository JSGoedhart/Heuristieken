import csv
import operator
import random
import time
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

print 'leftover:'
for i in range(0, len(leftover)):
	print leftover[i].m3

# define function to calculate #kg in spacecrafts
def sum_kg(lijst):
	kg_sum = []
	for i in range(0,len(lijst)):
		kg_sum.append(sum(c.kg for c in lijst[i]))
	return kg_sum

def sum_m3(lijst):
	m3_sum = []
	for i in range(0,len(lijst)):
		m3_sum.append(sum(c.m3 for c in lijst[i]))
	return m3_sum


def swap(a, b):
  return b, a

def val_leftover(lijst):
	sum_valtot = sum(c.valtot for c in lijst)
	return sum_valtot

# list with all cargo sorted in spacecrafts and leftover
spacecrafts.append(leftover)

# print original values from greedy algorithm
print 'old values greedy'
sum_kg1_original = sum_kg(spacecrafts[0:len(spacecrafts)])
sum_m31_original = sum_m3(spacecrafts[0:len(spacecrafts)])
sum_valtot_original = val_leftover(spacecrafts[4])

# create arrays with capacities
cap_kg = []
cap_m3 = []
for i in range(0, len(spacecraft_list_sorted)):
	cap_kg.append(spacecraft_list_sorted[i].kg)
	cap_m3.append(spacecraft_list_sorted[i].m3)

# Selecteer twee random nummers uit de leftover lijst
list_1 = range(0,len(leftover))
print list_1
rand_1 = random.choice(list_1)
print rand_1
list_1 = list_1.remove(rand_1)
print list_1
rand_2 = random.choice(list_1)

# select random items uit leftover lijst
item_1 = leftover[rand_1]
item_2 = leftover[rand_2]

# bereken sommaties van deze items
srand_kg = item_1.kg + item_2.kg
srand_m3 = item_1.m3 + item_2.m3
srand_valtot = item_1.valtot + item_2.valtot

print srand_kg
print srand_m3
print srand_valtot
