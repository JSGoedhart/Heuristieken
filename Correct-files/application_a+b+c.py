import csv
import operator
import classes
from helpers import *

# Excercise A: Run the first greedy with the last input element False
# Excercise B: Run the second greedy
# Excercise C: Change Cargolist1.csv to Cargolist2.csv and rund both greedy

# create list to put cargo1 classes in
cargo1_list_kg = open_cargo_csv('CargoList1.csv')
cargo1_list_m3 = open_cargo_csv('CargoList1.csv')

# sort cargo1_list's kg from high to low and create new sorted list
cargo1_sorted_kg = sorted(cargo1_list_kg, key=operator.attrgetter('kg'), reverse=True)
cargo1_sorted_m3 = sorted(cargo1_list_m3, key=operator.attrgetter('m3'), reverse=True)

# create a list with the four spacecrafts put into classes in it
spacecraft_list = open_spacecrafts_csv('Spacecrafts.csv')

# create lists of spacecrafts to put cargo-classes in
spacecrafts_kg = [[], [], [], [], []]

# define global
LEN = len(spacecrafts_kg)

# run greedy fill, to fill spacecrafts on basis of kg
# greedy_fill(spacecraft_list, cargo1_sorted_kg, spacecrafts_kg, 'kg', 'm3')
greedy_fill(spacecraft_list, cargo1_sorted_kg, spacecrafts_kg, 'kg', False)


# print output
print 'Question a: output on basis of kg:'
print 'Spacecrafts:   ',  print_names(spacecraft_list)
print 'Total kg in spacecrafts:', sum_kg(spacecrafts_kg)
print 'Total m3 in spacecrafts:', sum_m3(spacecrafts_kg)
print 'Score:', val_leftover(spacecrafts_kg[LEN-1])
print ''

# create lists of spacescrafts to put cargo-classes in
spacecrafts_m3 = [[], [], [], [], []]

# run greedy fill, to fill spacecrafts on basis of m3
greedy_fill(spacecraft_list, cargo1_sorted_m3, spacecrafts_m3, 'm3', 'kg')

# print output
print 'Question b: output on basis of m3:'
print 'spacecrafts:',  print_names(spacecraft_list)
print 'total kg in spacecrafts:', sum_kg(spacecrafts_m3)
print 'total m3 in spacecrafts:', sum_m3(spacecrafts_m3)
print 'score:', val_leftover(spacecrafts_m3[LEN-1])
print ''
