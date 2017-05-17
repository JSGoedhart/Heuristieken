import csv
import operator
import random
import time
import classes
from helpers import *
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from plotly.graph_objs import Scatter, Figure, Layout, Bar
import numpy

cargo1_list_2 = open_cargo_csv('CargoList1.csv')

# sort cargo1_list's kg from high to low and create new sorted list
cargo1_sorted_2 = sorted(cargo1_list_2, key=operator.attrgetter('kg'), reverse=True)

# create a list with the four spacecrafts put into classes in it
spacecraft_list = open_spacecrafts_csv('Spacecrafts.csv')

# create lists of spacecrafts to put cargo-classes in
spacecrafts2 = [[], [], [], [], []]

# global
LEN = len(spacecrafts2)

# run greedy fill, to fill spacecrafts on basis of m3
# greedy_fill(spacecraft_list, cargo1_sorted_2, spacecrafts2, 'kg', 'm3')
random_fill(spacecraft_list, cargo1_sorted_2, spacecrafts2)

# create array with capacities of spacecrafts in kg and m3
cap_kg = []
cap_m3 = []
for i in range(len(spacecraft_list)):
	cap_kg.append(spacecraft_list[i].kg)
	cap_m3.append(spacecraft_list[i].m3)

print 'spacecrafts:',  print_names(spacecraft_list)
print 'total kg in spacecrafts before:', sum_kg(spacecrafts2)
print 'total m3 in spacecrafts before:', sum_m3(spacecrafts2)
print 'score before:', val_leftover(spacecrafts2[LEN-1])
print ''

program_starts = time.time()
t_run2 = 0.50
t_start = time.time()
t_end = time.time() + t_run2
numb_swaps2 = 0
score2 = []
swaps1 = 0; swaps2 = 0; swaps3 = 0;
while time.time() < t_end:
	rand_ar2 = random2(spacecrafts2, [1,2])
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