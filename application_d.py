import csv
import operator
from classes import *
from helpers import *

# create list to put cargo1 classes in
cargo3_list_kg = open_cargo_csv('CargoList3.csv')
cargo3_list_m3 = open_cargo_csv('CargoList3.csv')

# sort cargo3_list's kg from high to low and create new sorted list
cargo3_sorted_kg = sorted(cargo3_list_kg, key=operator.attrgetter('kg'), reverse=True)
cargo3_sorted_m3 = sorted(cargo3_list_m3, key=operator.attrgetter('m3'), reverse=True)

# create a list with the six spacecrafts put into classes in it
spacecraft_list = open_spacecrafts_csv('Spacecrafts2.csv')

spacecraft_list_sorted = sorted(spacecraft_list, key=operator.attrgetter('kg'), reverse=True)
# create lists to put cargo-classes in
spacecrafts_kg = [[], [], [], [], [], []]

# run greedy fill, to fill spacecrafts on basis of kg and m3
spacecrafts_fleet = greedy_fleet(spacecraft_list_sorted, cargo3_sorted_m3)

for i in range(len(spacecrafts_fleet)):
	print i

# score
scorefunction(spacecrafts_fleet, spacecraft_list_sorted)

# hillclimbing
hillclimbing = hillclimbing2(10, spacecrafts_fleet[0][0], cap_kg, cap_m3)

def hillclimbing2(runtime, spacecrafts, cap_kg, cap_m3):
    score=[]
    program_starts = time.time()
    t_run = runtime
    t_end = time.time() + t_run
    numb_swaps = 0
    while time.time() < t_end:
        rand_ar2 = random2(spacecrafts, [1,2])
        check_swap = check_swap_random(spacecrafts, rand_ar2, cap_kg, cap_m3, False)
        if check_swap != None:
            num = check_swap[1]
            item = check_swap[2]
            random_arr = check_swap[3]
            scorevalue = swap_random2(spacecrafts, random_arr, num, item)
            numb_swaps += 1
            score.append(scorevalue)
        else:
            score.append(val_leftover(spacecrafts[len(spacecrafts)-1]))
    x = numpy.linspace(0, t_run, len(score))
    return score, x, numb_swaps

def random2(array1, array2):
    ''' returns an random amount of randomly selected items from one list and a random item from another random selected list '''
    # array to return randomly selected indices
    retour = []
    # create array to randomly select a list and select two items that cannot be equal
    amount = random.choice(array2)
    rand_range = range(len(array1[len(array1) - 1]))
    for i in range(amount):
        rand_item = random.choice(rand_range)
        retour.append(rand_item)
        rand_range.remove(rand_item)
    return retour




















