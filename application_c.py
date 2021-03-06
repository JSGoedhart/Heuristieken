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

for i in range(4):
	print spacecraft_list_sorted[i].name

# put cargo-items in list of spacecraft, when spacecraft is full, go to next
for j in range(4):
	# define available mass in spacecraft
	m3_av = spacecraft_list_sorted[j].m3
	kg_av = spacecraft_list_sorted[j].kg
	for i in range(len(cargo1_sorted)):
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
for i in range(len(cargo1_sorted)):
	if cargo1_sorted[i].m3 != 'nan':
		leftover.append(cargo1_sorted[i])

print 'leftover:'
for i in range(len(leftover)):
	print leftover[i].m3

# define function to calculate #kg in spacecrafts
def sum_kg(lijst):
	kg_sum = []
	for i in range(len(lijst)):
		kg_sum.append(sum(c.kg for c in lijst[i]))
	return kg_sum

def sum_m3(lijst):
	m3_sum = []
	for i in range(len(lijst)):
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
for i in range(len(spacecraft_list_sorted)):
	cap_kg.append(spacecraft_list_sorted[i].kg)
	cap_m3.append(spacecraft_list_sorted[i].m3)

program_starts = time.time()
t_end = time.time() + 10
while time.time() < t_end:

	print time.time()
	# Selecteer twee random nummers uit de leftover lijst
	list_1 = range(len(leftover))
	print list_1
	rand_1 = random.choice(list_1)
	print rand_1
	list_1.remove(rand_1)
	print list_1
	rand_2 = random.choice(list_1)
	print rand_2

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

	# sums for each spacecrafts
	sum_kg_orig = sum_kg(spacecrafts[0:len(spacecrafts)])
	sum_m3_orig = sum_m3(spacecrafts[0:len(spacecrafts)])
	sum_valtot_orig = val_leftover(spacecrafts[4])

	# create arrays with capacities
	cap_kg = []
	cap_m3 = []
	for i in range(len(spacecraft_list_sorted)):
		cap_kg.append(spacecraft_list_sorted[i].kg)
		cap_m3.append(spacecraft_list_sorted[i].m3)

	# overige capaciteit, kg en m3 per spacecraft:
	kg_over = []
	m3_over = []
	for i in range(len(cap_kg)):
		kg_over.append(cap_kg[i]- sum_kg_orig[i])
		m3_over.append(cap_m3[i]- sum_m3_orig[i])

	print kg_over
	print m3_over

	print 'valtot before:'
	print val_leftover(leftover)

	get_item = False
	control = 1
	# pak onderste element, check if value lager is dan value random leftover, als dit zo is ga je restricties checken, anders ga je door naar het volgende element
	for j in range(4):
		if control != 0:
			for i in reversed(range(0, len(spacecrafts[j]))):
				if (spacecrafts[j][i].valtot < srand_valtot):
					if (kg_over[j] + spacecrafts[j][i].kg >= srand_kg and m3_over[j] + spacecrafts[j][i].m3 >= srand_m3):
						get_item = True
						num = j
						item = i
						control = 0
						break
				else:
					next

	# swap elements from lestover with selected item from spacecrafts if possible
	if get_item == True:
		print num
		print item
		print spacecrafts[num][item].kg
		# swap elements
		spacecrafts.extend((item_1, item_2))
		leftover.append(spacecrafts[num][item])
		spacecrafts[num].remove(spacecrafts[num][item])
		leftover.remove(item_1)
		leftover.remove(item_2)
	else:
		print 'non found'

	print 'valtot after:'
	print val_leftover(leftover)
