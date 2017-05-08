import csv
import operator
import random
import time
import classes
from helpers import *

def swap(a, b):
	''' function that swaps to elements '''
	return b, a

# create list to put cargo1 classes in
cargo1_list = open_cargo_csv('CargoList1.csv')

# sort cargo1_list's kg from high to low and create new sorted list
cargo1_sorted = sorted(cargo1_list, key=operator.attrgetter('kg'), reverse=True)

# create a list with the four spacecrafts put into classes in it
spacecraft_list = open_spacecrafts_csv('Spacecrafts.csv')

# create lists of spacecrafts to put cargo-classes in
spacecrafts = [[], [], [], [], []]

# global
LEN = len(spacecrafts)

# run greedy fill, to fill spacecrafts on basis of m3
greedy_fill(spacecraft_list, cargo1_sorted, spacecrafts, 'kg', 'm3')

# create array with capacities of spacecrafts in kg and m3
cap_kg = []
cap_m3 = []
for i in range(len(spacecraft_list)):
	cap_kg.append(spacecraft_list[i].kg)
	cap_m3.append(spacecraft_list[i].m3)

program_starts = time.time()
t_end = time.time() + 10
while time.time() < t_end:
	# randomly select two indices of lists and two items to swap between, put in array
	rand_arr = random1(spacecrafts)
	# run hillclimbing algorithm with rand_arr
	swap_two(spacecrafts, rand_arr, cap_kg, cap_m3)

print 'scorefunctie', val_leftover(spacecrafts[LEN-1])

