import csv
import operator
import random
import time
import classes
from helpers_clean import *
import plotly.plotly as py
import plotly.graph_objs as go
import numpy

def sortbardata(scores, minimum, maximum):
    ''' sorts an array of into an array with amount of numbers per category
    each category is defined as: min+steps*stepsize - min + 1 + steps*stepsize
    where stepsize is equal to (max-min)/steps'''
    steps = (maximum - minimum)*2
    data = []
    stepsize = float(maximum - minimum)/float(steps)
    for i in range(len(scores)):
        data.append([0]*(steps+1));
        for j in range(len(scores[i])): 
            for k in range(steps):
                if scores[i][j] >= (minimum + k * stepsize) and scores[i][j] < (minimum + (k+1) * stepsize):
                    data[i][k] += 1
            if scores[i][j] >= (minimum + (steps+1) * stepsize):
                data[i][steps] += 1
    return data, minimum, maximum, steps

def createbardata(data, minimum, maximum, steps, legend):
    ''' places array called data in suitable barchart format for plotly '''
    returndata = []
    # calculate stepsize
    stepsize = float(maximum - minimum)/float(steps)
    # create x-array with categorical names
    x_arr = []
    for k in range(steps):
        s = "-";
        seq = (str(minimum+k*stepsize), str(minimum+(k+1)*stepsize))
        x_arr.append(s.join(seq))
    z = "+"; seq=(str(maximum), str());
    x_arr.append(z.join(seq));

    # put data in suitable format
    for i in range(len(data)):
        returndata.append(go.Bar(
            x = x_arr,
            y = data[i],
            name = legend[i]))

    return returndata, x_arr

def makebarchart(title, data, filename):
    ''' create barchart with title and input data '''
    layout = go.Layout(
        title = title,
        barmode='group')

    fig = go.Figure(data=data, layout=layout)
    py.iplot(fig, filename=filename)


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
    for j in range(10):
        output = main('CargoList1.csv', random_fill, algorithms[i], coolingscheme[i], 'm3', 2);
        score_arr.append(output[2])
    scores.append(score_arr)

# sort data into barchart categories
data_sort = sortbardata(scores, 26, 35)

# put sorted data in barchart format
data = createbardata(data_sort[0], data_sort[1], data_sort[2], data_sort[3], legend)

# make a barchart
makebarchart('Barchart with scores for n=1000 simulations', data[0], 'barchart 1')