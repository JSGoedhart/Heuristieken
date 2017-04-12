
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
		var0 = int(split[0][4:]);
		var1 = int(split[1]);
		var2 = float(split[2][:-1]);
		# fill dictionary with correct values
		data.append({names[0]: var0, names[1]: var1, names[2]: var2});
		index +=1
	# put dictionary in json format
	json.dump(data, jsonfile, sort_keys=True, indent=10, separators=(',', ': '))

# convert wanted csv file
convert("CargoList1.csv")

cargo = json.loads(open("CargoList1.json").read())

# define available mass of spacecrafts
mass = [2000, 2300, 2400, 5200]

# length of cargolist
lencargo = len(cargo)

# tryout 1: put cargo items in spacecrafts as they appear in the list,
# when a spacecraft is full, head on to the next
start = 1
for j in range(0,4):
	massav = mass[j]
	print j
	for i in range(start, lencargo):
		if int(cargo[i]["kg"]) <= massav:
			print int(cargo[i]["kg"])
			massav -= int(cargo[i]["kg"])
		else:
			# when spacecraft is full, go to next one
			start = i
			j += 1
			break
	print massav

def sort_by_kg(d):
    '''a helper function for sorting'''
    return d['kg']

# sort created jsonfile from high to low (kg)
sort = sorted(cargo, key=lambda k: k.get('kg', 0), reverse=True)

print sort[2]


# create new json file for sorted kg version and put sort in it
jsonfile = open('cargo1sorted.json', 'w')
json.dump(sort, jsonfile, sort_keys=True, indent=10, separators=(',', ': '))


# tryout 2
cargosort = json.loads(open("cargo1sorted.json").read())
print cargosort
