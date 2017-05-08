import csv
import operator
import random
import time
import classes
from helpers import *

# create list to put cargo1 classes in
cargo1_list = open_cargo_csv('CargoList1.csv')

# sort cargo1_list's kg from high to low and create new sorted list
cargo1_sorted = sorted(cargo1_list, key=operator.attrgetter('kg'), reverse=True)

# create a list with the four spacecrafts put into classes in it
spacecraft_list = open_spacecrafts_csv('Spacecrafts.csv')

# create lists of spacecrafts to put cargo-classes in
spacecrafts1 = [[], [], [], [], []]

# global
LEN = len(spacecrafts1)

# run greedy fill, to fill spacecrafts on basis of m3
greedy_fill(spacecraft_list, cargo1_sorted, spacecrafts1, 'kg', 'm3')

# create array with capacities of spacecrafts in kg and m3
cap_kg = []
cap_m3 = []
for i in range(len(spacecraft_list)):
	cap_kg.append(spacecraft_list[i].kg)
	cap_m3.append(spacecraft_list[i].m3)

print 'spacecrafts:',  print_names(spacecraft_list)
print 'total kg in spacecrafts before:', sum_kg(spacecrafts1)
print 'total m3 in spacecrafts before:', sum_m3(spacecrafts1)
print 'score before:', val_leftover(spacecrafts1[LEN-1])
print ''

# run hillclimbing 1 algorithm for selected time
program_starts = time.time()
t_end = time.time() + 1
while time.time() < t_end:
	numb_swaps = 0
	# randomly select two indices of lists and two items to swap between, put in array
	rand_arr = random1(spacecrafts1)
	# run hillclimbing algorithm with rand_arr
	swap_two(spacecrafts1, rand_arr, cap_kg, cap_m3)

	# count number of swaps
	if swap_two != 1:
		numb_swaps += 1

print 'Values for HILLCLIMBING 1:'
print 'spacecrafts:',  print_names(spacecraft_list)
print 'total kg in spacecrafts before:', sum_kg(spacecrafts1)
print 'total m3 in spacecrafts before:', sum_m3(spacecrafts1)
print 'score after:', val_leftover(spacecrafts1[LEN-1])
print 'number of swaps: ', numb_swaps

print '\n'


cargo1_list_2 = open_cargo_csv('CargoList1.csv')

# sort cargo1_list's kg from high to low and create new sorted list
cargo1_sorted_2 = sorted(cargo1_list_2, key=operator.attrgetter('kg'), reverse=True)

# create lists of spacecrafts to put cargo-classes in
spacecrafts2 = [[], [], [], [], []]

# run greedy fill, to fill spacecrafts on basis of m3
greedy_fill(spacecraft_list, cargo1_sorted_2, spacecrafts2, 'kg', 'm3')

print random2(spacecrafts2, [2,3,4])

program_starts = time.time()
t_end = time.time() + 60
while time.time() < t_end:
	numb_swaps2 = 0
	rand_ar2 = random2(spacecrafts2, [2,3,4])
	print rand_ar2
	swap_random(spacecrafts2, rand_ar2, cap_kg, cap_m3)
	if swap_two != 1:
		numb_swaps2 += 1

print 'Values for HILLCLIMBING 2:'
print 'spacecrafts:',  print_names(spacecraft_list)
print 'total kg in spacecrafts before:', sum_kg(spacecrafts2)
print 'total m3 in spacecrafts before:', sum_m3(spacecrafts2)
print 'score after:', val_leftover(spacecrafts2[LEN-1])
print 'number of swaps: ', numb_swaps2
