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

# create lists of spacecrafts to put cargo-classes in
spacecrafts_kg = [[], [], [], [], []]

# global
LEN = len(spacecrafts_kg)

# # run greedy fill, to fill spacecrafts on basis of kg
# greedy_fill(spacecraft_list, cargo1_sorted, spacecrafts_kg, 'kg')

# print 'Output on basis of kg:'
# print 'Spacecrafts:   ',  print_names(spacecraft_list)
# print 'Total kg in spacecrafts:', sum_kg(spacecrafts_kg)
# print 'Total m3 in spacecrafts:', sum_m3(spacecrafts_kg)
# print 'Score:', val_leftover(spacecrafts_kg[LEN-1])

spacecrafts_m3 = [[], [], [], [], []]
# sort cargo1_list's kg from high to low and create new sorted list
cargo1_sorted_m3 = sorted(cargo1_list, key=operator.attrgetter('m3'), reverse=True)

# # run greedy fill, to fill spacecrafts on basis of m3
greedy_fill(spacecraft_list, cargo1_sorted_m3, spacecrafts_m3, 'm3')

print 'output on basis of m3:'
print 'spacecrafts:',  print_names(spacecraft_list)
print 'total kg in spacecrafts:', sum_kg(spacecrafts_m3)
print 'total m3 in spacecrafts:', sum_m3(spacecrafts_m3)
print 'score:', val_leftover(spacecrafts_m3[LEN-1])