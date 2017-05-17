import csv
import operator
import random
import time
import classes
from helpers import *
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from plotly.graph_objs import Scatter, Figure, Layout, Bar
import numpy
import matplotlib.pyplot as plt

item = ['kg', 'm3', 'm3', 'kg']

# array to put scores for kg and m3 in
score = [[], []]
print score[0]

# run hillclimbing 1 with greedy_kg and greedy_m3 as starting point
for i in [0,1]:
	index = i
	item1 = item[2*i]
	item2 = item[2*i+1]
	# create list to put cargo1 classes in
	cargo1_list = open_cargo_csv('CargoList1.csv')

	# sort cargo1_list's kg from high to low and create new sorted list
	cargo1_sorted = sorted(cargo1_list, key=operator.attrgetter(item1), reverse=True)

	# create a list with the four spacecrafts put into classes in it
	spacecraft_list = open_spacecrafts_csv('Spacecrafts.csv')
	# spacecraft_list_sorted = sorted(spacecraft_list, key=operator.attrgetter('kg'), reverse=True)

	# create lists of spacecrafts to put cargo-classes in
	spacecrafts1 = [[], [], [], [], []]

	# global
	LEN = len(spacecrafts1)

	# create array with capacities of spacecrafts in kg and m3
	cap_kg = []
	cap_m3 = []
	for i in range(len(spacecraft_list)):
		cap_kg.append(spacecraft_list[i].kg)
		cap_m3.append(spacecraft_list[i].m3)


	# run greedy fill, to fill spacecrafts on basis of kg, m3 or random
	greedy_fill(spacecraft_list, cargo1_sorted, spacecrafts1, item1, item2)
	# greedy_fill(spacecraft_list, cargo1_sorted_m3, spacecrafts1, 'm3', 'kg')
	# random_fill(spacecraft_list, cargo1_sorted, spacecrafts1)

	print 'STARTING VALUES FOR GREEDY bases on: ', item1
	print 'spacecrafts:',  print_names(spacecraft_list)
	print 'total kg in spacecrafts before:', sum_kg(spacecrafts1)
	print 'total m3 in spacecrafts before:', sum_m3(spacecrafts1)
	print 'score before:', val_leftover(spacecrafts1[LEN-1])
	print ''

	# run hillclimbing 1 algorithm for selected time
	program_starts = time.time()
	t_run = 2
	t_end = time.time() + t_run
	# create variable to count number of swaps and array for scores
	numb_swaps = 0
	t_start = time.time()
	while time.time() < t_end:
		# randomly select two indices of lists and two items to swap between, put in array
		rand_arr = random1(spacecrafts1)
		# run hillclimbing algorithm with rand_arr
		check = swap_two(spacecrafts1, rand_arr, cap_kg, cap_m3)
		values = check_swap(check[0], rand_arr, cap_kg, cap_m3, check[1])
		# count number of swaps
		numb_swaps += values[0]
		# put score in array
		score[index].append(values[1])

	print 'Values for HILLCLIMBING 1 greedy on: ', item1
	print 'spacecrafts:',  print_names(spacecraft_list)
	print 'total kg in spacecrafts before:', sum_kg(spacecrafts1)
	print 'total m3 in spacecrafts before:', sum_m3(spacecrafts1)
	print 'score after:', val_leftover(spacecrafts1[LEN-1])
	print 'number of swaps: ', numb_swaps
	print ''

# plot score against running time for hillclimbing 1 with greedy as starting point (kg and m3)
xtime0 = numpy.linspace(0, t_run, len(score[0]))
xtime1 = numpy.linspace(0, t_run, len(score[1]))
scatter1 = plot([Scatter(x=xtime0, y=score[0]), Scatter(x=xtime1, y=score[1])])

# plto results for greedy kg and m3 as starting point
f = plt.figure()
greedy_kg, = plt.plot(xtime0, score[0], 'b', label="Starting point: greedy kg")
greedy_m3, = plt.plot(xtime1, score[1], 'r', label="Starting point: greedy m3")
plt.ylabel('Score', {'size':'12'})
plt.xlabel('Time (seconds)', {'size':'12'})
plt.title('Hillclimber 1 with greedy as starting point', {'size':'14'})
plt.legend(handles=[greedy_kg, greedy_m3], prop={'size':10})
f.savefig("Hillclimbing1-greedy", bbox_inches='tight')

