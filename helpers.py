import csv
import operator
import random
import time
import classes
import numpy
import math
import plotly.plotly as py
import plotly.graph_objs as go

def open_cargo_csv(file):
    # create list to put cargo1 classes in
    split_list = []

    # put cargo-elements of list 1 in class cargo1
    csvfile = open(file, 'r')
    for line in csvfile:
    	split = line.split(';')
    	var0 = split[0]
    	var1 = int(split[1])
    	var2 = float(split[2][:-1])
    	split_list.append(classes.cargo1(var0, var1, var2))
    return split_list

def open_spacecrafts_csv(file):
    # create empty list for spacecrafts
    open_list = []

    # put spacecrafts in empty list
    csvfile = open(file, 'r')
    for line in csvfile:
        split = line.split(';')
        var0 = split[0]
        var1 = int(split[1])
        var2 = float(split[2])
        open_list.append(classes.spacecraft(var0, var1, var2))
    return open_list

def open_alles(cargolist, item):
    ''' opens cargolist and spacecraft list '''
    # create list to put cargo1 classes in
    cargo1_list = open_cargo_csv(cargolist)

    # sort cargo1_list's kg from high to low and create new sorted list
    cargo_sorted = sorted(cargo1_list, key=operator.attrgetter(item), reverse=True)

    # create a list with the four spacecrafts put into classes in it
    spacecraft_list = open_spacecrafts_csv('Spacecrafts.csv')

    # create lists of spacecrafts to put cargo-classes in
    spacecrafts = [[], [], [], [], []]

    return cargo_sorted, spacecraft_list, spacecrafts

def greedy_fill(list1, list2, list3, item, item2):
    ''' fill list3 with items of list2, based on variable item. When full go to next. If item2!=false, also take the other variable in account'''
    if (item2 == False):
        for j in range(len(list3)-1):
            # define availability in spacecraft
            mass_av = getattr(list1[j], item)
            for i in range(len(list2)):
                # check if cargo-item is already placed
                if (getattr(list2[i], item) != 'nan'):
                    if (getattr(list2[i], item) <= mass_av):
                        list3[j].append(classes.cargo1(list2[i].number, list2[i].kg, list2[i].m3))
                        mass_av -= getattr(list2[i], item)
                        setattr(list2[i], item, 'nan')
        # create leftover list and put in spacecraft list without nan
        for k in range(len(list2)):
            if (getattr(list2[k], item) != 'nan'):
                list3[len(list3)-1].append(list2[k])
        return list3
    else:
        for j in range(len(list3)-1):
            # define availability in spacecraft
            mass_av = getattr(list1[j], item)
            av_1 = getattr(list1[j], item2)
            for i in range(len(list2)):
                # check if cargo-item is already placed
                if (getattr(list2[i], item) != 'nan'):
                    if (getattr(list2[i], item) <= mass_av and getattr(list2[i], item2) <= av_1):
                        list3[j].append(classes.cargo1(list2[i].number, list2[i].kg, list2[i].m3))
                        mass_av -= getattr(list2[i], item)
                        av_1 -= getattr(list2[i], item2)
                        setattr(list2[i], item, 'nan')
        # create leftover list and put in spacecraft list without nan
        for k in range(len(list2)):
            if (getattr(list2[k], item) != 'nan'):
                list3[len(list3)-1].append(list2[k])
        return list3

def random_fill(list1, list2, list3):
    ''' places elements of list2 randomly in array of lists list3 '''
    for i in range(len(list2)):
        # select random list to put item in
        number_list = range(len(list3))
        index = random.choice(number_list)
        sum_kg = sum(c.kg for c in list3[index]); sum_m3 = sum(c.m3 for c in list3[index]);
        kg_item = getattr(list2[i], "kg"); m3_item = getattr(list2[i], "m3");
        # check for kg and m3 restriction
        if (sum_kg + kg_item > getattr(list1[index], "kg") or sum_m3 + m3_item > getattr(list1[index], "m3")):
            # put in leftover list if item doesn't fit in the selected list
            list3[len(list3)-1].append(list2[i])
        else:
            list3[index].append(list2[i])


def swap(a, b):
    ''' function that swaps to elements '''
    return b, a

def swap_two(list1, rand_arr, cap_kg, cap_m3):
    ''' swap items from list1 and check if this is possible with cap1 and cap2 '''
    length = len(list1)
    # calculate scorefunction before swapping
    score_old = val_leftover(list1[length-1])
    # swap
    list1[rand_arr[0]][rand_arr[2]], list1[rand_arr[1]][rand_arr[3]] = swap(list1[rand_arr[0]][rand_arr[2]], list1[rand_arr[1]][rand_arr[3]])
    return list1, score_old

def check_swap(list1, rand_arr, cap_kg, cap_m3, score_old):
    ''' function that checks for all the swap restrictions '''
    length = len(list1)
    sum_kg1 = sum_kg(list1[0:length])
    sum_m31 = sum_m3(list1[0:length])
    score_new = val_leftover(list1[length-1])
    check_swap = 0
    for i in rand_arr[0:2]:
        # check if list selected list is leftover list
        if (i < (length-1) and (sum_kg1[i] > cap_kg[i] or sum_m31[i] > cap_m3[i])):
            # print 'not ok'
            check_swap = 1
        # only swap when score gets better (smaller)
        if (score_new > score_old):
            check_swap = 1
    # swap back when restrictions aren't hold on to
    if (check_swap == 1):
        # print 'SWAPPING BACK'
        list1[rand_arr[0]][rand_arr[2]], list1[rand_arr[1]][rand_arr[3]] = swap(list1[rand_arr[0]][rand_arr[2]], list1[rand_arr[1]][rand_arr[3]])
    score_return = val_leftover(list1[length-1])
    # return swap (yes/no) and score after running swap_two
    return [check_swap, score_return]

def print_names(lijst):
    name_arr = []
    for i in range(len(lijst)):
        name_arr.append(lijst[i].name)
    name_arr.append('leftover')
    return name_arr

def sum_kg(lijst):
    ''' function to calculate total kg's per spacecrafts '''
    kg_sum = []
    for i in range(len(lijst)):
        kg_sum.append(sum(c.kg for c in lijst[i]))
    return kg_sum

def sum_m3(lijst):
    ''' function to calculate total kg's per spacecrafts '''
    m3_sum = []
    for i in range(len(lijst)):
        m3_sum.append(sum(c.m3 for c in lijst[i]))
    return m3_sum

def val_leftover(lijst):
    ''' score functie'''
    sum_valtot = sum(c.valtot for c in lijst)
    return sum_valtot

def print_kg(list1, list2):
    ''' print kg's per spacecraft '''
    for j in range(4):
    	print list1[j].name
    	for i in range(len(list2[j])):
    		print list2[j][i].kg

def print_m3(list1, list2):
    ''' print kg's per spacecraft '''
    for j in range(4):
    	print spacecraft_list[j].name
    	for i in range(len(spacecrafts[j])):
    		print spacecrafts[j][i].m3

def random1(array):
    ''' returns two random selected items (indices) out of two randomly selected lists from array '''
    # array to return randomly selected indices
    retour = []
    # create array to randomly select a list and select two items that cannot be equal
    number_list = range(len(array))
    retour.append(random.choice(number_list))
    number_list.remove(retour[0])
    retour.append(random.choice(number_list))
    # randomly an item from the two selected lists
    retour.append(random.choice(range(len(array[retour[0]]))))
    retour.append(random.choice(range(len(array[retour[1]]))))
    return retour

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

# swap_random kan in principe weg: vervangen door check_swap_random en swap_random2
# def swap_random(list1, array1, cap_kg, cap_m3):
#     numb_swaps = 0
#     ''' swaps a randomly selected amount of items of a specified list, with an item of another list, if possible '''
#     len_ar = len(array1)
#     len_lst = len(list1)
#     # create array with randomly selected items from specified list
#     random_arr = []
#     for i in range(len_ar):
#         random_arr.append(list1[len_lst-1][array1[i]])
#     random_arr

#     # calculate sums and score of items from specified list
#     sum_kg_rand = sum(c.kg for c in random_arr)
#     sum_m3_rand = sum(c.m3 for c in random_arr)
#     score_rand = sum(c.valtot for c in random_arr)

#     # calculate free m3 and kg per list of list1
#     sum_kg1 = sum_kg(list1[0:len_lst])
#     sum_m31 = sum_m3(list1[0:len_lst])
#     score_old = val_leftover(list1[len_lst-1])

#     # overige capaciteit, kg en m3 per spacecraft:
#     kg_over = []
#     m3_over = []
#     for i in range(len(cap_kg)):
#         kg_over.append(cap_kg[i]- sum_kg1[i])
#         m3_over.append(cap_m3[i]- sum_m31[i])

#     # loop through lists to check if there exists an element the random elements can be swapped with
#     get_item = False
#     control = 0
#     for i in range(len_lst-1):
#         if control != 1:
#             for j in range(len(list1[i])):
#                 # check if swapping would not break the restrictions
#                 if (kg_over[i] + list1[i][j].kg >= sum_kg_rand and m3_over[i] + list1[i][j].m3 >= sum_m3_rand):
#                     # check for annealing (true) or hillclimber
#                     # check if score random elements is better than selected
#                     if (list1[i][j].valtot < score_rand):
#                         get_item = True
#                         num = i
#                         item = j
#                         control = 1
#                         break;
#     # swap if possible
#     if (get_item == True):

#         numb_swaps += 1
#         # add random elements to list and remove from leftover list
#         list1[num].extend(random_arr)
#         list1[len_lst-1].append(list1[num][item])
#         list1[num].remove(list1[num][item])
#         for i in range(len_ar):
#             list1[len_lst -1].remove(random_arr[i])
#     return [numb_swaps, val_leftover(list1[len_lst-1])]

def capacities(spacecraft_list):
    ''' creates two arrays with capacities of spacecrafts (kg and m3) '''
    cap_kg = []
    cap_m3 = []
    for i in range(len(spacecraft_list)):
        cap_kg.append(spacecraft_list[i].kg)
        cap_m3.append(spacecraft_list[i].m3)
    return cap_kg, cap_m3

def hillclimbing1(runtime, spacecrafts, cap_kg, cap_m3):
    score = []
    program_starts = time.time()
    t_run = runtime
    t_end = time.time() + t_run
    numb_swaps = 0
    t_start = time.time()
    while time.time() < t_end:
        # randomly select two indices of lists and two items to swap between, put in array
        rand_arr = random1(spacecrafts)
        # run hillclimbing algorithm with rand_arr
        check = swap_two(spacecrafts, rand_arr, cap_kg, cap_m3)
        values = check_swap(check[0], rand_arr, cap_kg, cap_m3, check[1])
        # count number of swaps
        numb_swaps += values[0]
        # put score in array
        score.append(values[1])
    x = numpy.linspace(0, t_run, len(score))
    return score, x, numb_swaps

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

def main(cargolist, startpunt, algorithm, coolingscheme, item, runtime):
    ''' function that generates a starting point for cargolist, runs an algorithm on it for selected time and returns the score
    starting point is greedy item when item isn't false, when item is false: starting point is random '''

    # create necessary arrays by running open_alles on cargolist
    necessary_arrays = open_alles(cargolist, item)
    cargo_sorted = necessary_arrays[0]; spacecraft_list = necessary_arrays[1]; spacecrafts = necessary_arrays[2];

    # create arrays with capacities
    cap = capacities(spacecraft_list)
    cap_kg = cap[0]; cap_m3 = cap[1]

    # generete starting point, random, greedy on kg or greedy on m3
    if item == False:
        random_fill(spacecraft_list, cargo_sorted, spacecrafts)
    elif item == 'kg':
        greedy_fill(spacecraft_list, cargo_sorted, spacecrafts, 'kg', 'm3')
    elif item == 'm3':
        greedy_fill(spacecraft_list, cargo_sorted, spacecrafts, 'm3', 'kg')

    # run algorithm for selected time
    if coolingscheme == False:
        algorit = algorithm(runtime, spacecrafts, cap_kg, cap_m3)
    else:
        algorit = algorithm(runtime, spacecrafts, cap_kg, cap_m3, coolingscheme)

    # create names for array with score and running time
    score = algorit[0]
    xtime = numpy.linspace(0, runtime, len(score))
    return score, xtime

def createdata(datalist):
    ''' function that places the input data in a suitable format for plotly '''
    data = []
    for i in range(len(datalist)):
        data.append(go.Scattergl(
            name = datalist[i][0],
            x = datalist[i][1],
            y = datalist[i][2],
            line = dict(
                width = 1.0)));
    return data

def plot(title, range, data, width, height, plotname):
    ''' make a plot with the input data, the given title (string) in the given range (array[a,b]'''
    layout = go.Layout(
        title = title,
        width=width,
        height= height,
        yaxis = dict(
            autotick= False,
            dtick = 5,
            title = 'Score',
            titlefont = dict(
                family = 'Arial, sans-serif',
                size=14),
            range = range),
        xaxis = dict(
            title = 'Time (seconds)',
            titlefont = dict(
                family = 'Arial, sans-serif',
                size=14)),
        showlegend=True,
        legend=dict(x=0.8, y=1.0)
        )
    fig = go.Figure(data=data, layout=layout)

    py.iplot(fig, filename=plotname)

def greedy_fleet_with_america_check(spacecraft_list, cargolist):
    ''' fills fleet with all the cargo (exercise d and e)'''

    # create lists to put cargo-classes in
    spacecrafts_fleet = []

    leftover_list = cargolist
    count = 0
    while len(leftover_list) != 0:
        count += 1
        temp_spacecrafts = [[], [], [], [], [], []]
        temp_cargo = leftover_list
        greedy_fill_fleet_with_america_check(spacecraft_list, temp_cargo, temp_spacecrafts, 'm3', 'kg')
        leftover_list = temp_spacecrafts[len(temp_spacecrafts)-1]
        spacecrafts_fleet.append(temp_spacecrafts)

    return spacecrafts_fleet

def greedy_fleet(spacecraft_list, cargolist):
    ''' fills fleet with all the cargo (exercise d and e)'''

    # create lists to put cargo-classes in
    spacecrafts_fleet = []

    leftover_list = cargolist
    count = 0
    while len(leftover_list) != 0:
        count += 1
        temp_spacecrafts = [[], [], [], [], [], []]
        temp_cargo = leftover_list
        greedy_fill_fleet(spacecraft_list, temp_cargo, temp_spacecrafts, 'm3', 'kg')
        leftover_list = temp_spacecrafts[len(temp_spacecrafts)-1]
        spacecrafts_fleet.append(temp_spacecrafts)

    return spacecrafts_fleet

def scorefunction(spacecrafts_fleet, spacecraft_list):
    ''' calculates the total wasted space and gives a score '''

    score_kg = 0
    score_m3 = 0

    # score function:
    for k in range(len(spacecrafts_fleet)):
        for j in range(len(spacecrafts_fleet[k])-1):
            kg = 0
            m3 = 0
            for i in range(len(spacecrafts_fleet[k][j])):
                kg = kg + spacecrafts_fleet[k][j][i].kg
                m3 = m3 + spacecrafts_fleet[k][j][i].m3
            if kg != 0 and m3 != 0:
                weighted_kg = kg/spacecraft_list[j].kg
                weighted_m3 = m3/spacecraft_list[j].m3
                score_kg = score_kg + (1 - weighted_kg)
                score_m3 = score_m3 + (1 - weighted_m3)

    print "kg score:", score_kg
    print "m3 score:", score_m3


    total_kg_spacecrafts = 0
    total_m3_spacecrafts = 0

    total_kg_cargo = 0
    total_m3_cargo = 0

    # score function procent
    for k in range(len(spacecrafts_fleet)):
        for j in range(len(spacecrafts_fleet[k])-1):
            total_kg_spacecrafts = total_kg_spacecrafts + spacecraft_list[j].kg
            total_m3_spacecrafts = total_m3_spacecrafts + spacecraft_list[j].m3
            for i in range(len(spacecrafts_fleet[k][j])):
                total_kg_cargo = total_kg_cargo + spacecrafts_fleet[k][j][i].kg
                total_m3_cargo = total_m3_cargo + spacecrafts_fleet[k][j][i].m3

    # procent filled
    procent_kg = float(total_kg_cargo)/float(total_kg_spacecrafts)
    procent_m3 = total_m3_cargo/total_m3_spacecrafts

    print "kg filled in procent:", procent_kg
    print "m3 filled in procent:", procent_m3

def greedy_fill_fleet_with_america_check(spacecraft_list, cargolist, list3, item, item2):
    ''' fills the 5 spacecrafts of the fleet and makes a choice between cygnus and dragon of america'''
    for j in range(len(list3)-1):
        # define availability in spacecraft
        mass_av = getattr(spacecraft_list[j], item)
        av_1 = getattr(spacecraft_list[j], item2)

        mass_av_cygnus_real = getattr(spacecraft_list[5], item)
        av_1_cygnus_real = getattr(spacecraft_list[5], item2)

        # fill both dragon and cygnus, check which one is better and use the better one
        if (spacecraft_list[j].name == 'Dragon'):
            temp_Dragon = []
            temp_Cygnus = []
            print "dragon"
        #     print temp_Dragon
        #     print 'volgende:'
            temp_cargolist_dragon = cargolist
            temp_cargolist_cygnus = cargolist
            mass_av_cygnus = getattr(spacecraft_list[5], item)
            av_1_cygnus = getattr(spacecraft_list[5], item2)
            mass_av_dragon = getattr(spacecraft_list[j], item)
            av_1_dragon = getattr(spacecraft_list[j], item2)
            for i in range(len(temp_cargolist_dragon)):
                # check if cargo-item is already placed for dragon
                if (getattr(temp_cargolist_dragon[i], item) != 'nan'):
                    if(getattr(temp_cargolist_dragon[i], item) <= mass_av_dragon and getattr(temp_cargolist_dragon[i], item2) <= av_1_dragon):
                        temp_Dragon.append(classes.cargo1(temp_cargolist_dragon[i].number, temp_cargolist_dragon[i].kg, temp_cargolist_dragon[i].m3))
                        mass_av_dragon -= getattr(temp_cargolist_dragon[i], item)
                        av_1_dragon -= getattr(temp_cargolist_dragon[i], item2)
            for i in range(len(temp_cargolist_cygnus)):
                if (getattr(temp_cargolist_cygnus[i], item) != 'nan'):
                    if(getattr(temp_cargolist_cygnus[i], item) <= mass_av_cygnus and getattr(temp_cargolist_cygnus[i], item2) <= av_1_cygnus):
                        temp_Cygnus.append(classes.cargo1(temp_cargolist_cygnus[i].number, temp_cargolist_cygnus[i].kg, temp_cargolist_cygnus[i].m3))
                        mass_av_cygnus -= getattr(temp_cargolist_cygnus[i], item)
                        av_1_cygnus -= getattr(temp_cargolist_cygnus[i], item2)
            # score checken
            kg_dragon = 0
            kg_cygnus = 0
            m3_dragon = 0
            m3_cygnus = 0
            for i in range(len(temp_Dragon)):
                kg_dragon = kg_dragon + temp_Dragon[i].kg
                m3_dragon = m3_dragon + temp_Dragon[i].m3
            procent_kg_dragon = kg_dragon/spacecraft_list[j].kg
            procent_m3_dragon = m3_dragon/spacecraft_list[j].m3
            for i in range(len(temp_Cygnus)):
                kg_cygnus = kg_cygnus + temp_Cygnus[i].kg
                m3_cygnus = m3_cygnus + temp_Cygnus[i].m3
            procent_kg_cygnus = kg_cygnus/spacecraft_list[5].kg
            procent_m3_cygnus = m3_cygnus/spacecraft_list[5].m3
            print procent_m3_dragon + procent_kg_dragon
            print procent_m3_cygnus + procent_kg_cygnus
            # vul de spacecraft die beter is (dus meer gevuld)
            # vul dragon:
            if ((procent_m3_dragon + procent_kg_dragon) >= (procent_m3_cygnus + procent_kg_cygnus)):
                for i in range(len(cargolist)):
                    # check if cargo-item is already placed
                    if (getattr(cargolist[i], item) != 'nan'):
                        if (getattr(cargolist[i], item) <= mass_av and getattr(cargolist[i], item2) <= av_1):
                            list3[j].append(classes.cargo1(cargolist[i].number, cargolist[i].kg, cargolist[i].m3))
                            mass_av -= getattr(cargolist[i], item)
                            av_1 -= getattr(cargolist[i], item2)
                            setattr(cargolist[i], item, 'nan')
            # anders vul cygnus:
            else:
                for i in range(len(cargolist)):
                    # check if cargo-item is already placed
                    if (getattr(cargolist[i], item) != 'nan'):
                        if (getattr(cargolist[i], item) <= mass_av_cygnus_real and getattr(cargolist[i], item2) <= av_1_cygnus_real):
                            list3[j].append(classes.cargo1(cargolist[i].number, cargolist[i].kg, cargolist[i].m3))
                            mass_av_cygnus_real -= getattr(cargolist[i], item)
                            av_1_cygnus_real -= getattr(cargolist[i], item2)
                            setattr(cargolist[i], item, 'nan')

        # # normal fill
        else:
            for i in range(len(cargolist)):
                # check if cargo-item is already placed
                if (getattr(cargolist[i], item) != 'nan'):
                    if (getattr(cargolist[i], item) <= mass_av and getattr(cargolist[i], item2) <= av_1):
                        list3[j].append(classes.cargo1(cargolist[i].number, cargolist[i].kg, cargolist[i].m3))
                        mass_av -= getattr(cargolist[i], item)
                        av_1 -= getattr(cargolist[i], item2)
                        setattr(cargolist[i], item, 'nan')
    # create leftover list and put in spacecraft list without nan
    for k in range(len(cargolist)):
        if (getattr(cargolist[k], item) != 'nan'):
            list3[len(list3)-1].append(cargolist[k])
    return list3

def greedy_fill_fleet(spacecraft_list, cargolist, list3, item, item2):
    ''' fills the 5 spacecrafts of the fleet and makes a choice between cygnus and dragon of america'''
    for j in range(len(list3)-1):
        # define availability in spacecraft
        mass_av = getattr(spacecraft_list[j], item)
        av_1 = getattr(spacecraft_list[j], item2)

        for i in range(len(cargolist)):
            # check if cargo-item is already placed
            if (getattr(cargolist[i], item) != 'nan'):
                if (getattr(cargolist[i], item) <= mass_av and getattr(cargolist[i], item2) <= av_1):
                    list3[j].append(classes.cargo1(cargolist[i].number, cargolist[i].kg, cargolist[i].m3))
                    mass_av -= getattr(cargolist[i], item)
                    av_1 -= getattr(cargolist[i], item2)
                    setattr(cargolist[i], item, 'nan')
    # create leftover list and put in spacecraft list without nan
    for k in range(len(cargolist)):
        if (getattr(cargolist[k], item) != 'nan'):
            list3[len(list3)-1].append(cargolist[k])
    return list3

def annealing1_exponential(runtime, spacecrafts, cap_kg, cap_m3):
    ''' runs simulated annealing algorithm that swaps two items at a time during
     the desegnated runtime (s) using an exponential cooling schedule '''
    score = []

     # initial and end temperatures for cooling schedule
    temp_initial = 1
    temp_end = 0.0000000000000001

    LEN = len(spacecrafts)

    # set counters for iterations and instances of accepted increases in the
    # objective function
    iteration = 0
    accepted = 0

    # start timer
    start_time = time.time()
    t_end = time.time() + runtime

    while time.time() < t_end:
        # store score before swapping items
        old_score = val_leftover(spacecrafts[LEN - 1])

        # exponential cooling schedule
        temp_exp = temp_initial * math.pow((temp_end / temp_initial),
        ((time.time() - start_time) / runtime))

        # random number between 0 and 1 for rejection criterion
        random_num = random.uniform(0,1)

    	# randomly select two indices of lists and two items to swap between, put in array
        rand_arr = random1(spacecrafts)

    	# run hillclimbing algorithm with rand_arr
        swap_two(spacecrafts, rand_arr, cap_kg, cap_m3)

        sum_kg1 = sum_kg(spacecrafts[0:length])
        sum_m31 = sum_m3(spacecrafts[0:length])
        value = 0
        for i in rand_arr[0:2]:
            # check if list selected list isn't leftover list
            if i < (LEN-1):
                # check for kg and m3 restriction
                if sum_kg1[i] > cap_kg[i] or sum_m31[i] > cap_m3[i]:
                    value = 1

        # swap back if necessary
        if (value == 1):
            swap_two(spacecrafts, rand_arr, cap_kg, cap_m3)

        #store new score after swapping items
        new_score = val_leftover(spacecrafts[LEN-1])

        # change in score
        change = new_score - old_score

    	# rejection criteria
        if temp_exp > 0:
    		# check if new score is worse than old score
    	    if old_score < new_score and value == 0:
    			# check whether change fails to meet acceptance criteria
    			if random_num >= math.exp(-change / temp_exp):
    		        # swap items back
    				swap_two(spacecrafts, rand_arr, cap_kg, cap_m3)
    			else:
    				# increment acceptances
    				accepted +=1
        elif old_score < new_score and value == 0:
    		swap_two(spacecrafts, rand_arr, cap_kg, cap_m3)

        # append new score to score function
        score.append(val_leftover(spacecrafts[LEN-1]))

        # increment iterations
        iteration += 1

    # create array with time-values (x-values)
    x = numpy.linspace(0, t_run, len(score))

    return score, x, iteration
    #     # increment iterations
    #     iteration += 1
    # print score
    # # return iteration, accepted

def annealing1_sigmoidal(runtime, spacecrafts, cap_kg, cap_m3):
    ''' runs simulated annealing algorithm that swaps two items at a time during
     the desegnated runtime (s) using a sigmoidal cooling schedule '''
    score = []

     # initial and end temperatures for cooling schedule
    temp_initial = 1
    temp_end = 0.0000000000000001

    LEN = len(spacecrafts)

    # set counters for iterations and instances of accepted increases in the
    # objective function
    iteration = 0
    accepted = 0

    # start timer
    start_time = time.time()
    t_end = time.time() + runtime

    while time.time() < t_end:
        # store score before swapping items
        old_score = val_leftover(spacecrafts[LEN - 1])

        # exponential cooling schedule
        temp_sig = temp_end + (temp_initial - temp_end) * (1 / (1 + math.exp(0.3
        * (time.time() - start_time - (runtime / 2)))))

        # random number between 0 and 1 for rejection criterion
        random_num = random.uniform(0,1)

    	# randomly select two indices of lists and two items to swap between, put in array
        rand_arr = random1(spacecrafts)

    	# run hillclimbing algorithm with rand_arr
        swap_two(spacecrafts, rand_arr, cap_kg, cap_m3)

        length = len(spacecrafts)
        sum_kg1 = sum_kg(spacecrafts[0:length])
        sum_m31 = sum_m3(spacecrafts[0:length])
        value = 0
        for i in rand_arr[0:2]:
            # check if list selected list isn't leftover list
            if i < (length-1):
                # check for kg and m3 restriction
                if sum_kg1[i] > cap_kg[i] or sum_m31[i] > cap_m3[i]:
                    value = 1

        # swap back if necessary
        if (value == 1):
            swap_two(spacecrafts, rand_arr, cap_kg, cap_m3)

        #store new score after swapping items
        new_score = val_leftover(spacecrafts[LEN-1])

        # change in score
        change = new_score - old_score

    	# rejection criteria
        if temp_sig > 0:
    		# check if new score is worse than old score
    	    if old_score < new_score and value == 0:
    			# check whether change fails to meet acceptance criteria
    			if random_num >= math.exp(-change / temp_sig):
    		        # swap items back
    				swap_two(spacecrafts, rand_arr, cap_kg, cap_m3)
    			else:
    				# increment acceptances
    				accepted +=1
        elif old_score < new_score and value == 0:
    		swap_two(spacecrafts, rand_arr, cap_kg, cap_m3)

        # append new score to score function
        score.append(val_leftover(spacecrafts[LEN-1]))
        # increment iterations
        iteration += 1
    # create array with time-values (x-values)
    x = numpy.linspace(0, t_run, len(score))
    return score, x, iteration
    #return iteration, accepted

def annealing1(runtime, spacecrafts, cap_kg, cap_m3, schedule):
    ''' runs simulated annealing algorithm that swaps two items at a time during
     the desegnated runtime (s) using a sigmoidal cooling schedule '''
    score = []

     # initial and end temperatures for cooling schedule
    temp_initial = 800
    temp_end = 1

    LEN = len(spacecrafts)

    # set counters for iterations and instances of accepted increases in the
    # objective function
    iteration = 0
    accepted = 0

    LEN = len(spacecrafts)

    # start timer
    start_time = time.time()
    t_end = time.time() + runtime

    while time.time() < t_end:
        # store score before swapping items
        old_score = val_leftover(spacecrafts[LEN - 1])

        if schedule == 'exponential':
            # exponential cooling schedule
            temp_current = temp_initial * math.pow((temp_end / temp_initial),
            ((time.time() - start_time) / runtime))
        elif schedule == 'sigmoidal':
            # sigmoidal cooling schedule
            temp_current = temp_end + (temp_initial - temp_end) * (1 / (1 + math.exp(0.3
            * (time.time() - start_time - (runtime / 2)))))

        # random number between 0 and 1 for rejection criterion
        random_num = random.uniform(0,1)

    	# randomly select two indices of lists and two items to swap between, put in array
        rand_arr = random1(spacecrafts)

    	# run hillclimbing algorithm with rand_arr
        swap_two(spacecrafts, rand_arr, cap_kg, cap_m3)

        sum_kg1 = sum_kg(spacecrafts[0:LEN])
        sum_m31 = sum_m3(spacecrafts[0:LEN])
        value = 0
        for i in rand_arr[0:2]:
            # check if list selected list isn't leftover list
            if i < (LEN-1):
                # check for kg and m3 restriction
                if sum_kg1[i] > cap_kg[i] or sum_m31[i] > cap_m3[i]:
                    value = 1

        # swap back if necessary
        if (value == 1):
            swap_two(spacecrafts, rand_arr, cap_kg, cap_m3)

        #store new score after swapping items
        new_score = val_leftover(spacecrafts[LEN-1])

        # change in score
        change = new_score - old_score

    	# rejection criteria
        if temp_current > 0:
    		# check if new score is worse than old score
    	    if old_score < new_score and value == 0:
    			# check whether change fails to meet acceptance criteria
    			if random_num >= math.exp(-change / temp_current):
    		        # swap items back
    				swap_two(spacecrafts, rand_arr, cap_kg, cap_m3)
    			else:
    				# increment acceptances
    				accepted +=1
        elif old_score < new_score and value == 0:
    		swap_two(spacecrafts, rand_arr, cap_kg, cap_m3)

        # append new score to score function
        score.append(val_leftover(spacecrafts[LEN-1]))
        # increment iterations
        iteration += 1

    x = numpy.linspace(0, runtime, len(score))

    return score, x, iteration
    # return iteration, accepted

# SA 2 - SHIT
def check_swap_random(list1, array1, cap_kg, cap_m3, annealing):
    numb_swaps = 0
    ''' checks for restrictions to swaps a randomly selected amount of items of a specified list, with an item of another list, if possible '''
    len_ar = len(array1)
    len_lst = len(list1)
    # create array with randomly selected items from specified list
    random_arr = []
    for i in range(len_ar):
        random_arr.append(list1[len_lst-1][array1[i]])
    random_arr

    # calculate sums and score of items from specified list
    sum_kg_rand = sum(c.kg for c in random_arr)
    sum_m3_rand = sum(c.m3 for c in random_arr)
    score_rand = sum(c.valtot for c in random_arr)

    # calculate free m3 and kg per list of list1
    sum_kg1 = sum_kg(list1[0:len_lst])
    sum_m31 = sum_m3(list1[0:len_lst])
    old_score = val_leftover(list1[len_lst-1])

    # overige capaciteit, kg en m3 per spacecraft:
    kg_over = []
    m3_over = []
    for i in range(len(cap_kg)):
        kg_over.append(cap_kg[i]- sum_kg1[i])
        m3_over.append(cap_m3[i]- sum_m31[i])

    # loop through lists to check if there exists an element the random elements can be swapped with
    get_item = False
    change = True
    control = 0
    for i in range(len_lst-1):
        if control != 1:
            for j in range(len(list1[i])):
                # check if swapping would not break the restrictions
                if (kg_over[i] + list1[i][j].kg >= sum_kg_rand and m3_over[i] + list1[i][j].m3 >= sum_m3_rand):
                    # check for annealing (true) or hillclimber
                    # check if score random elements is better than selected
                    if (list1[i][j].valtot < score_rand):
                        get_item = True
                        num = i
                        item = j
                        control = 1
                        new_score = old_score - score_rand + list1[i][j].valtot
                        change = new_score - old_score
                        break;
                    elif (annealing == True):
                        get_item = 'annealing'
                        num = i
                        item = j
                        control = 1
                        new_score = old_score - score_rand + list1[i][j].valtot
                        change = new_score - old_score


    # return correct values for hillclimber or annealing
    # annealing is true so return change
    if get_item == 'annealing':
        return change, num, item, random_arr
    # swap that improves score has been found (get_item = true)
    elif get_item == True:
        return False, num, item, random_arr

def annealing2(runtime, spacecrafts, cap_kg, cap_m3, schedule):
    ''' runs simulated annealing algorithm that swaps two items at a time during
     the desegnated runtime (s) using a sigmoidal cooling schedule '''
    score = []

     # initial and end temperatures for cooling schedule
    temp_initial = 1
    temp_end = 0.0000000000000001

    LEN = len(spacecrafts)

    # set counters for iterations and instances of accepted increases in the
    # objective function
    iteration = 0
    accepted = 0

    # start timer
    start_time = time.time()
    t_end = time.time() + runtime

    while time.time() < t_end:
        # store score before swapping items
        old_score = val_leftover(spacecrafts[LEN - 1])

        if schedule == 'exponential':
            # exponential cooling schedule
            temp_current = temp_initial * math.pow((temp_end / temp_initial),
            ((time.time() - start_time) / runtime))
        elif schedule == 'sigmoidal':
            # sigmoidal cooling schedule
            temp_current = temp_end + (temp_initial - temp_end) * (1 / (1 + math.exp(0.3
            * (time.time() - start_time - (runtime / 2)))))

        # random number between 0 and 1 for rejection criterion
        random_num = random.uniform(0,1)

        # create random array that selects 1 or 2 items from the leftover list
        rand_ar2 = random2(spacecrafts, [1,2])

        check_swap = check_swap_random(spacecrafts, rand_ar2, cap_kg, cap_m3, True)
        if check_swap != None:
            change = check_swap[0]
            num = check_swap[1]
            item = check_swap[2]
            random_arr = check_swap[3]

            # check if a swap with improved score function has been found
            if (change == False):
                # better score, so swap
                swap_random2(spacecrafts, random_arr, num, item)
            # check if annealing criteria allows for swap !!!!!!!!!!!!!!! criteria checken bij len!!!
            elif (random_num < math.exp(-change / temp_current)):
                swap_random2(spacecrafts, random_arr, num, item)

            # append new score to score function
            score.append(val_leftover(spacecrafts[LEN-1]))
            # increment iterations
            iteration += 1
    x = numpy.linspace(0, runtime, len(score))

    return score, x, iteration

def swap_random2(list1, array1, num, item):
    ''' swaps the randomly selected items of array1 with list1[num][item]'''
    # add random elements to list and remove from leftover list
    len_lst = len(list1)
    len_ar = len(array1)
    list1[num].extend(array1)
    list1[len_lst-1].append(list1[num][item])
    list1[num].remove(list1[num][item])
    for i in range(len_ar):
        list1[len_lst -1].remove(array1[i])
    return val_leftover(list1[len_lst-1])
