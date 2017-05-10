import csv
import operator
import random
import time
import classes
from helpers import *

print random.uniform(0,1)

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

# run simulated annealing algorithm 1 for selected time
program_starts = time.time()
t_end = time.time() + 1
while time.time() < t_end:
    #store the score before swapping items
    old_score = val_leftover(spacecrafts1[LEN-1])

	# randomly select two indices of lists and two items to swap between, put in array
	rand_arr = random1(spacecrafts1)
	# run hillclimbing algorithm with rand_arr
	swap_two(spacecrafts1, rand_arr, cap_kg, cap_m3)

    #store new score after swapping items
    new_score = val_leftover(spacecrafts1[LEN-1])


print 'Values for SA 1:'
print 'spacecrafts:',  print_names(spacecraft_list)
print 'total kg in spacecrafts before:', sum_kg(spacecrafts1)
print 'total m3 in spacecrafts before:', sum_m3(spacecrafts1)
print 'score after:', val_leftover(spacecrafts1[LEN-1])


print '\n'
