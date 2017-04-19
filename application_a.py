import csv
import operator
from classes import *
# from helpers import *


# # define class for cargo's
# class cargo1:
# 	def __init__(self, number, kg, m3):
# 		self.number = number
# 		self.kg = int(kg)
# 		self.m3 = float(m3)

# create list to put cargo1 classes in
cargo1_list = []

# put cargo-elements of list 1 in class cargo1
csvfile = open('CargoList1.csv', 'r')
for line in csvfile:
	split = line.split(';')
	var0 = split[0]
	var1 = int(split[1])
	var2 = float(split[2][:-1])
	cargo1_list.append(cargo1(var0, var1, var2))

# sort cargo1_list's kg from high to low and create new sorted list
cargo1_sorted = sorted(cargo1_list, key=operator.attrgetter('kg'), reverse=True)

# # define class for spacecrafts
# class spacecraft:
# 	def __init__(self, name, kg, m3):
# 		self.name = name
# 		self.kg = kg
# 		self.m3 = m3

# create a list with the four spacecrafts put into classes in it
spacecraft_list = [spacecraft('cygnus', 2000, 18.9), spacecraft('verne', 2300, 13.1), spacecraft('progress', 2400, 7.6), spacecraft('kounotori', 5200, 14)]

# create lists to put cargo-classes in
spacecrafts = [[], [], [], []]

# put cargo-items in list of spacecraft, when spacecraft is full, go to next
for j in range(0, 4):
	# define available mass in spacecraft
	mass_av = spacecraft_list[j].kg
	for i in range(0, len(cargo1_sorted)):
		# check if cargo-item is already placed
		if (cargo1_sorted[i].kg == 'nan'):
			next
		else:
			# put cargo-item in spacecraft if there is enough space
			if (cargo1_sorted[i].kg <= mass_av):
				spacecrafts[j].append(cargo1(cargo1_sorted[i].number, cargo1_sorted[i].kg, cargo1_sorted[i].m3))
				mass_av -= cargo1_sorted[i].kg
				cargo1_sorted[i].kg = 'nan'
			# when item doesn't fit, try next
			else:
				next
	# print mass_av

# print kg's per spacecraft
for j in range(0, 4):
	print spacecraft_list[j].name
	for i in range(0, len(spacecrafts[j])):
		print spacecrafts[j][i].kg

# hoeveel gewicht en ruimte blijft er over per spacecraft?
for j in range(0, 4):
	print spacecraft_list[j].name
	sum_kg = 0
	sum_m3 = 0
	for i in range(0, len(spacecrafts[j])):
		sum_kg += spacecrafts[j][i].kg
		sum_m3 += spacecrafts[j][i].m3
	print sum_kg
	print sum_m3
