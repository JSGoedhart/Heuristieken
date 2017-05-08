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
spacecraft_list_sorted = sorted(spacecraft_list, key=operator.attrgetter('kg'), reverse=True)

# create lists of spacecrafts to put cargo-classes in
spacecrafts1 = [[], [], [], [], []]

# global
LEN = len(spacecrafts1)

# run greedy fill, to fill spacecrafts on basis of m3
greedy_fill(spacecraft_list_sorted, cargo1_sorted, spacecrafts1, 'kg', 'm3')

# create array with capacities of spacecrafts in kg and m3
cap_kg = []
cap_m3 = []
for i in range(len(spacecraft_list_sorted)):
	cap_kg.append(spacecraft_list_sorted[i].kg)
	cap_m3.append(spacecraft_list_sorted[i].m3)

print cap_kg
print cap_m3

print 'spacecrafts:',  print_names(spacecraft_list_sorted)
print 'total kg in spacecrafts before:', sum_kg(spacecrafts1)
print 'total m3 in spacecrafts before:', sum_m3(spacecrafts1)
print 'score before:', val_leftover(spacecrafts1[LEN-1])
print ''

# run hillclimbing 1 algorithm for selected time
program_starts = time.time()
t_end = time.time() + 1
while time.time() < t_end:
	# randomly select two indices of lists and two items to swap between, put in array
	rand_arr = random1(spacecrafts1)
	# run hillclimbing algorithm with rand_arr
	swap_two(spacecrafts1, rand_arr, cap_kg, cap_m3)

print 'Values for HILLCLIMBING 1:'
print 'spacecrafts:',  print_names(spacecraft_list_sorted)
print 'total kg in spacecrafts before:', sum_kg(spacecrafts1)
print 'total m3 in spacecrafts before:', sum_m3(spacecrafts1)
print 'score after:', val_leftover(spacecrafts1[LEN-1])


print '\n'


cargo1_list_2 = open_cargo_csv('CargoList1.csv')

# sort cargo1_list's kg from high to low and create new sorted list
cargo1_sorted_2 = sorted(cargo1_list_2, key=operator.attrgetter('kg'), reverse=True)

# create lists of spacecrafts to put cargo-classes in
spacecrafts2 = [[], [], [], [], []]

# run greedy fill, to fill spacecrafts on basis of m3
greedy_fill(spacecraft_list_sorted, cargo1_sorted_2, spacecrafts2, 'kg', 'm3')

program_starts = time.time()
t_end = time.time() + 1
while time.time() < t_end:
	rand_ar2 = random2(spacecrafts2, [2,3,4])
	swap_random(spacecrafts2, rand_ar2, cap_kg, cap_m3)

print 'Values for HILLCLIMBING 2:'
print 'spacecrafts:',  print_names(spacecraft_list_sorted)
print 'total kg in spacecrafts before:', sum_kg(spacecrafts2)
print 'total m3 in spacecrafts before:', sum_m3(spacecrafts2)
print 'score after:', val_leftover(spacecrafts2[LEN-1])

