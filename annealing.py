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

runtime = 10

# run simulated annealing algorithm with exponential cooling schedule
SA1_exp = annealing1_exponential(runtime, spacecrafts1, cap_kg, cap_m3)

print 'number of iterations: ', SA1_exp[0]

print 'iterations per second: ', SA1_exp[0] / runtime

print 'number of non-improving swaps: ', SA1_exp[1]

print 'Values for SA 1:'
print 'spacecrafts:',  print_names(spacecraft_list)
print 'total kg in spacecrafts before:', sum_kg(spacecrafts1)
print 'total m3 in spacecrafts before:', sum_m3(spacecrafts1)
print 'score after:', val_leftover(spacecrafts1[LEN-1])


print '\n'
print '\n'
