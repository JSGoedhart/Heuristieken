import csv
import operator
import random
import time
import classes
from helpers import *
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from plotly.graph_objs import Scatter, Figure, Layout, Bar
import numpy

# create list to put cargo1 classes in
cargo1_list = open_cargo_csv('CargoList1.csv')

# sort cargo1_list's kg from high to low and create new sorted list
cargo1_sorted = sorted(cargo1_list, key=operator.attrgetter('kg'), reverse=True)

# create a list with the four spacecrafts put into classes in it
spacecraft_list = open_spacecrafts_csv('Spacecrafts.csv')
# spacecraft_list_sorted = sorted(spacecraft_list, key=operator.attrgetter('kg'), reverse=True)

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

print cap_kg
print cap_m3

print 'spacecrafts:',  print_names(spacecraft_list)
print 'total kg in spacecrafts before:', sum_kg(spacecrafts1)
print 'total m3 in spacecrafts before:', sum_m3(spacecrafts1)
print 'score before:', val_leftover(spacecrafts1[LEN-1])
print ''

# run hillclimbing 1 algorithm for selected time
program_starts = time.time()
t_run = 1
t_end = time.time() + t_run
# create variable to count number of swaps and array for scores
numb_swaps = 0
swapsa = 0; swapsb = 0; swapsc = 0;
score = []
t_start = time.time()
while time.time() < t_end:
	# randomly select two indices of lists and two items to swap between, put in array
	rand_arr = random1(spacecrafts1)
	# run hillclimbing algorithm with rand_arr
	values = swap_two(spacecrafts1, rand_arr, cap_kg, cap_m3)
	# count number of swaps
	numb_swaps += values[0]
	# put score in array
	score.append(values[1])
	if (time.time() - t_start <= 1):
		swapsa += values[0]
	elif (time.time() - t_start > 1 and time.time() - t_start <= 2):
		swapsb += values[0]
	else:
		swapsc += values[0]

# plot score against running time
xtime = numpy.linspace(0, t_run, len(score))
scatter1 = plot([Scatter(x=xtime, y=score)])

# bar1 = plot({
# "data": [
#     Bar(x=['0-1 sec','1-2 sec','2-5 sec'],y=[swapsa, swapsb, swapsc])
# ]
# })

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

program_starts = time.time()
t_run2 = 0.2
t_start = time.time()
t_end = time.time() + t_run2
numb_swaps2 = 0
score2 = []
swaps1 = 0; swaps2 = 0; swaps3 = 0;
while time.time() < t_end:
	rand_ar2 = random2(spacecrafts2, [1,2,3])
	values = swap_random(spacecrafts2, rand_ar2, cap_kg, cap_m3)
	numb_swaps2 += values[0]
	score2.append(values[1])
	if (time.time() - t_start <= 0.01):
		swaps1 += values[0]
	elif (time.time() - t_start > 0.01 and time.time() - t_start <= 0.02):
		swaps2 += values[0]
	else:
		swaps3 += values[0]

xtime2 = numpy.linspace(0, t_run2, len(score2))
scatter2 = plot([Scatter(x=xtime2, y=score2)])

# bar2 = plot({
# "data": [
#     Bar(x=['0-0.01 sec','0.01-0.02 sec','0.02-1 sec'],y=[swaps1, swaps2, swaps3])
# ]
# })

print 'Values for HILLCLIMBING 2:'
print 'spacecrafts:',  print_names(spacecraft_list)
print 'total kg in spacecrafts before:', sum_kg(spacecrafts2)
print 'total m3 in spacecrafts before:', sum_m3(spacecrafts2)
print 'score after:', val_leftover(spacecrafts2[LEN-1])
print 'number of swaps: ', numb_swaps2