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
hillcl1 = main('CargoList1.csv', greedy_fill, hillclimbing1, 'm3', 2);
hillcl2 = main('CargoList1.csv', greedy_fill, hillclimbing2, 'm3', 2);

# TEST
trace1 = go.Scatter(
	name = 'Hillclimber 1',
	x = hillcl1[1],
	y = hillcl1[0])

trace2 = go.Scatter(
	name = 'Hillclimber 2',
	x = hillcl2[1],
	y = hillcl2[0])

layout = go.Layout(	
	title = 'List: cargo 1, starting point: greedy m3',
	width=500,
	height= 400,
	yaxis = dict(
		autotick= False,
		dtick = 2,
		title = 'Time (seconds)',
		titlefont = dict(
			family = 'Arial, sans-serif',
			size=12),
		range = [28, 31]),
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

py.iplot(fig, filename='Plot 3')
