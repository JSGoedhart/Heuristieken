import csv
import operator
import classes
from helpers import *

# create list to put cargo1 classes in
cargo1_list = open_cargo_csv('CargoList1.csv')

# sort cargo1_list's kg from high to low and create new sorted list
cargo1_sorted = sorted(cargo1_list, key=operator.attrgetter('kg'), reverse=True)

# create a list with the four spacecrafts put into classes in it
spacecraft_list = open_spacecrafts_csv('Spacecrafts.csv')

# create lists to put cargo-classes in
spacecrafts = [[], [], [], []]

# global
LEN = len(spacecrafts)

# run greedy fill, to fill spacecrafts on basis of kg
greedy_fill(spacecraft_list, cargo1_sorted, spacecrafts, 'kg')

print 'output on basis of kg:'
print 'spacecrafts:   ',  print_names(spacecraft_list)
print 'total kg in spacecrafts:', sum_kg(spacecrafts)
print 'total m3 in spacecrafts:', sum_m3(spacecrafts)
print 'score:', val_leftover(spacecrafts[LEN])

# run greedy fill, to fill spacecrafts on basis of m3
greedy_fill(spacecraft_list, cargo1_sorted, spacecrafts, 'm3')

print 'output on basis of m3:'
print 'spacecrafts:   ',  print_names(spacecraft_list)
print 'total kg in spacecrafts:', sum_kg(spacecrafts)
print 'total m3 in spacecrafts:', sum_m3(spacecrafts)
print 'score:', val_leftover(spacecrafts[LEN])