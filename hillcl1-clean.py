import csv
import operator
import random
import time
import classes
from helpers import *
import plotly.plotly as py
import plotly.graph_objs as go
import numpy

# run main function with cargolist, greedy kg and algorithm: hillclimbing1 for 2 seconds
xy = main('CargoList1.csv', greedy_fill, hillclimbing1, 'kg', 2);

# put x, y -values in array
score = xy[0]; x=xy[1]

# TEST
trace1 = go.Scatter(
	name = 'greedy kg',
	x = x,
	y = score)

layout = go.Layout(
	title = 'Hillclimbing 1, greedy kg and m3',
	width=500,
	height= 400,
	yaxis = dict(
		autotick= False,
		dtick = 2,
		title = 'Time (seconds)',
		titlefont = dict(
			family = 'Arial, sans-serif',
			size=12),
		range = [25, 40]),
	xaxis = dict(
		title = 'Score',
		titlefont = dict(
			family = 'Arial, sans-serif',
			size=12)),
	showlegend=True, 
	legend=dict(x=0.7, y=1.0)
	)

data = [trace1]

fig = go.Figure(data=data, layout=layout)

py.iplot(fig, filename='Greedy Hillclimbing 1, cargo 1')
