import csv
import operator
import random
import time
import classes
from helpers_clean import *
import plotly.plotly as py
import plotly.graph_objs as go
import numpy

# create array with algorithms that should be used, with corresponding coolingschemes if necessary
algorithms = [hillclimbing1, hillclimbing2, annealing1, annealing1, annealing2, annealing2]
coolingscheme = [False, False, 'exponential', 'sigmoidal', 'exponential', 'sigmoidal']
# assign legendnames to each algorithm
legend = ['Hillclimber 1', 'Hillclimber 2', 'Annealing 1 - Exp', 'Annealing 1 - Sigmd', 'Annealing 2 - Exp', 'Annealing 2 - Sigm']

# create array to place endscores of each algorithm in
scores = []

# loop through algorithms
for i in range(len(algorithms)):
    score_arr = []
   
    # run each algorithm n times for selected time, fill randomly 
    for j in range(500):
        output = main('CargoList1.csv', random_fill, algorithms[i], coolingscheme[i], 'm3', 10);
        score_arr.append(output[2])
    scores.append(score_arr)

# sort data into barchart categories
data_sort = sortbardata(scores, 27, 40)

# put sorted data in barchart format
data = createbardata(data_sort[0], data_sort[1], data_sort[2], data_sort[3], legend)

# make a barchart
makebarchart('Scores for n=500 simulations', data[0], 'barchart 1')