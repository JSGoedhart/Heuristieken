
# Convert Cargolist1.csv to json format

import csv
import json

# JSON key indexes
names = ["number", "kg", "m3"]

# converts csv data to json format
def convert(filename):
	csvfilename = filename
	jsonfilename = csvfilename.split('.')[0] + '.json'
	csvfile = open(csvfilename, 'r')
	jsonfile = open(jsonfilename, 'w')
	csv_reader = csv.reader(csvfile, names)

	# declare empty dictionary to put data in
	data = []
	index = 0
	for line in csvfile:
		split = line.split(';');
		var0 = split[0];
		var1 = split[1];
		var2 = split[2][0];
		# fill dictionary with correct values
		data.append({names[0]: var0, names[1]: var1, names[2]: var2});
		index +=1
	# put dictionary in json format
	json.dump(data, jsonfile, sort_keys=True, indent=10, separators=(',', ': '))

# convert wanted csv file
convert("CargoList1.csv")

