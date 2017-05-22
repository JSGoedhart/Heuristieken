import csv
import operator
import random
import time
import classes
from helpers import *
# from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
# from plotly.graph_objs import Scatter, Figure, Layout, Bar
import plotly.plotly as py
import plotly.graph_objs as go
import numpy


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
	cargo1_list = open_cargo_csv('CargoList2.csv')

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
# scatter1 = plot([Scatter(x=xtime0, y=score[0], layout=Layout), Scatter(x=xtime1, y=score[1])])

# TEST
trace1 = go.Scatter(
	name = 'greedy kg',
	x = xtime0,
	y = score[0])

trace2 = go.Scatter(
	name = 'greedy m3', 
	x=xtime0, 
	y=score[1])

layout = go.Layout(
	title = 'Hillclimbing 1, greedy kg and m3',
	width=500,
	height= 400,
	yaxis = dict(
		autotick= False,
		dtick = 0.5,
		title = 'Time (seconds)',
		titlefont = dict(
			family = 'Arial, sans-serif',
			size=12),
		range = [75, 76]),
	xaxis = dict(
		title = 'Score',
		titlefont = dict(
			family = 'Arial, sans-serif',
			size=12)),
	showlegend=True, 
	legend=dict(x=0.7, y=1.0)
	)

data = [trace1, trace2]

fig = go.Figure(data=data, layout=layout)

py.iplot(fig, filename='Greedy Hillclimbing 1, cargo 2')

