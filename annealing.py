from __future__ import division
import csv
import operator
import random
import time
import classes
import math
from helpers import *
# from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
# from plotly.graph_objs import Scatter, Figure, Layout, Bar
import numpy

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
#greedy_fill(spacecraft_list, cargo1_sorted, spacecrafts1, 'kg', 'm3')

# run random fill
random_fill(spacecraft_list, cargo1_sorted, spacecrafts1)

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

# create array to plot score function
score = []
# run simulated annealing algorithm 1 for selected time
iteration = 0

accepted = 0

# approximation of the amount of iterations per 10 seconds
max_iterations = 200000
temp_initial = 1
temp_end = 0.0000000000000001

start_time = time.time()
t_run = 21600 # zes uur
t_end = time.time() + t_run
while time.time() < t_end:
    #store the score before swapping items
    old_score = val_leftover(spacecrafts1[LEN-1])

    # increment iterations
    iteration = iteration + 1

    # linear cooling scheme
    #temp_linear = temp_initial - (time.time() - start_time) * (temp_initial - temp_end) / (t_run)

	# exponential cooling scheme
    temp_exp = temp_initial * math.pow((temp_end / temp_initial),((time.time() - start_time) / t_run))


    # random number between 0 and 1 for Boltzmann criterion
    random_num = random.uniform(0,1)

	# randomly select two indices of lists and two items to swap between, put in array
    rand_arr = random1(spacecrafts1)
	# run hillclimbing algorithm with rand_arr
    swap_two(spacecrafts1, rand_arr, cap_kg, cap_m3)

    length = len(spacecrafts1)
    sum_kg1 = sum_kg(spacecrafts1[0:length])
    sum_m31 = sum_m3(spacecrafts1[0:length])
    value = 0
    for i in rand_arr[0:2]:
        # check if list selected list isn't leftover list
        if i < (length-1):
            # check for kg and m3 restriction
            if sum_kg1[i] > cap_kg[i] or sum_m31[i] > cap_m3[i]:
                value = 1

    # swap back if necessary
    if (value == 1):
        swap_two(spacecrafts1, rand_arr, cap_kg, cap_m3)

    #store new score after swapping items
    new_score = val_leftover(spacecrafts1[LEN-1])

    # change in score
    change = new_score - old_score

	# rejection criteria
    if temp_exp > 0:
		# check if new score is worse than old score
	    if old_score < new_score and value == 0:
			# check whether change fails to meet acceptance criteria
			if random_num >= math.exp(-change / temp_exp):
		        # swap items back
				swap_two(spacecrafts1, rand_arr, cap_kg, cap_m3)
			else:
				# increment acceptances
				accepted +=1
    elif old_score < new_score and value == 0:
		swap_two(spacecrafts1, rand_arr, cap_kg, cap_m3)


    # append new score to score function
    score.append(val_leftover(spacecrafts1[LEN-1]))

    # count number of downturns
    check = 0
    if (val_leftover(spacecrafts1[LEN-1]) > old_score):
        check += 1

# # plot score function against time
# xtime = numpy.linspace(0, t_run, len(score))
# scatter = plot([Scatter(x=xtime, y=score)])


print 'number of iterations: ', iteration

print 'iterations per second: ', iteration / t_run

print 'number of non-improving swaps: ', accepted

print 'Values for SA 1:'
print 'spacecrafts:',  print_names(spacecraft_list)
print 'total kg in spacecrafts before:', sum_kg(spacecrafts1)
print 'total m3 in spacecrafts before:', sum_m3(spacecrafts1)
print 'score after:', val_leftover(spacecrafts1[LEN-1])


print '\n'
print '\n'
