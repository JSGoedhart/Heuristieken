import csv
import operator
import random
import time
import classes
from helpers import *
import plotly.plotly as py
import plotly.graph_objs as go
import numpy

# create array with algorithms that should be used
algorithms = [annealing1, annealing2]
coolingscheme = ['sigmoidal', 'sigmoidal']
# assign legendnames to each algorithm
legend = ['Annealing 1 - Sigmd', 'Annealing 2 - Sigm']

# create array to put x- and y-values of each algorithm in
datalist = []

# run each algorithm and save results
for i in range(len(algorithms)):
	# Divide items of cargolist with startingpoint greedy, than run the selected algorithm for the selected time
	output = main('CargoList1.csv', greedy_fill, algorithms[i], coolingscheme[i], 'm3', 30);
	# append legendname and x,y-values to datalist
	datalist.append([legend[i], output[1], output[0]])

# put datalist in plotable format
data = createdata(datalist)

# plot the results of all the used algorithms, with selected range and size
plot('Cargo 1 with starting point greedy m3', [26,60], data, 1000, 600, 'Plot SA2 - SIGM')
