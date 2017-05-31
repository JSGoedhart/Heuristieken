import csv
import operator
import random
import time
import classes
import numpy
import math
import plotly.plotly as py
import plotly.graph_objs as go


## 1 FUNCTIONS TO OPEN CSV FILES
def open_cargo_csv(file):
    ''' Argument: csv file.
    Split elements per line
    Return split_list.
    '''
    # Create list to put cargo1 classes in
    split_list = []

    # Put cargo-elements of list 1 in class cargo1
    csvfile = open(file, 'r')

    for line in csvfile:
    	split = line.split(';')
    	var0 = split[0]
    	var1 = int(split[1])
    	var2 = float(split[2][:-1])
    	split_list.append(classes.cargo1(var0, var1, var2))

    return split_list

def open_spacecrafts_csv(file):
    ''' Argument: csv file.
    Split elements per line.
    Return open_list.
    '''
    # Create empty list for spacecrafts
    open_list = []

    # Put spacecrafts in empty list
    csvfile = open(file, 'r')

    for line in csvfile:
        split = line.split(';')
        var0 = split[0]
        var1 = int(split[1])
        var2 = float(split[2])
        open_list.append(classes.spacecraft(var0, var1, var2))

    return open_list

def open_alles(cargolist, item):
    ''' Arguments: cargolist and item.
    Run open_cargo_csv on cargolist.
    Sort list on basis of item.
    Return cargo_sorted, spacecraft_list and spacecrafts.
    '''
    # Create list to put cargo1 classes in
    cargo1_list = open_cargo_csv(cargolist)

    # Sort cargo1_list's kg from high to low and create new sorted list
    cargo_sorted = sorted(cargo1_list, key=operator.attrgetter(item), reverse=True)

    # Create a list with the four spacecrafts put into classes in it
    spacecraft_list = open_spacecrafts_csv('Spacecrafts.csv')

    # Create lists of spacecrafts to put cargo-classes in
    spacecrafts = [[], [], [], [], []]

    return cargo_sorted, spacecraft_list, spacecrafts

## MAIN FUNCTION
def main(cargolist, startpunt, algorithm, coolingscheme, item, runtime):
    '''Arguments: cargolist, startpunt, algorithm, coolingscheme, item, runtime.
    Generate starting point for cargolist and run algorithm for selected time.
    If startpunt is false, then starting point is random.
    Starting point is greedy when item is not false.
    Return score, xtime and score_end.
    '''

    # Create necessary arrays by running open_alles on cargolist.
    necessary_arrays = open_alles(cargolist, item)
    cargo_sorted = necessary_arrays[0]; spacecraft_list = necessary_arrays[1];
    spacecrafts = necessary_arrays[2];

    # Create arrays with capacities
    cap = capacities(spacecraft_list)
    cap_kg = cap[0]; cap_m3 = cap[1]

    # Generete starting point, random, greedy on kg or greedy on m3.
    if algorithm == random_fill:
        random_fill(spacecraft_list, cargo_sorted, spacecrafts)
    else:
        if item == 'kg':
            greedy_fill(spacecraft_list, cargo_sorted, spacecrafts, 'kg', 'm3')
        else:
            greedy_fill(spacecraft_list, cargo_sorted, spacecrafts, 'm3', 'kg')
    # if item == False:
    #     random_fill(spacecraft_list, cargo_sorted, spacecrafts)
    # elif item == 'kg':
    #     greedy_fill(spacecraft_list, cargo_sorted, spacecrafts, 'kg', 'm3')
    # elif item == 'm3':
    #     greedy_fill(spacecraft_list, cargo_sorted, spacecrafts, 'm3', 'kg')

    # Run algorithm for selected time
    if coolingscheme == False:
        algorit = algorithm(runtime, spacecrafts, cap_kg, cap_m3)
    else:
        algorit = algorithm(runtime, spacecrafts, cap_kg, cap_m3, coolingscheme)

    # Create names for array with score and running time
    score = algorit[0]
    xtime = numpy.linspace(0, runtime, len(score))
    score_end = algorit[3]
    return score, xtime, score_end

def print_names(lijst):
    '''Argument: lijst.
    Return name_arr.
    '''

    # Create empty list for array of names.
    name_arr = []

    # Append names of list to empty array.
    for i in range(len(lijst)):
        name_arr.append(lijst[i].name)
    name_arr.append('leftover')

    return name_arr

## 3 FUNCTIONS TO CALCULATE AND PRINT SUMS/SCORES
def sum_kg(lijst):
    '''Argument: lijst.
    Calculate total kg per spacecraft.
    Return kg_sum.
    '''
    # Create empty list for sum of kg's.
    kg_sum = []

    for i in range(len(lijst)):
        kg_sum.append(sum(c.kg for c in lijst[i]))
    return kg_sum

def sum_m3(lijst):
    '''Argument: lijst.
    Calculate total m3 per spacecraft.
    Return m3_sum.
    '''
    # Create empty list for sum of m3's.
    m3_sum = []

    for i in range(len(lijst)):
        m3_sum.append(sum(c.m3 for c in lijst[i]))
    return m3_sum

def val_leftover(lijst):
    '''Argument: lijst.
    Take sum of value function.
    Return sum_valtot.
    '''
    sum_valtot = sum(c.valtot for c in lijst)
    return sum_valtot

def print_kg(list1, list2):
    '''Arguments: list1 and list2.
    Print kg per spacecraft.
    '''

    # Print names and kg per list items for both lists.
    for j in range(4):
        print list1[j].name
        for i in range(len(list2[j])):
            print list2[j][i].kg

def print_m3(list1, list2):
    '''Arguments: list1 and list2.
    Print m3 per spacecraft.
    '''

    # Print names and m3 per list items for both lists.
    for j in range(4):
        print spacecraft_list[j].name
        for i in range(len(spacecrafts[j])):
            print spacecrafts[j][i].m3

def capacities(spacecraft_list):
    '''Argument: spacecraft_list.
    Create two arrays with capacities of spacecrafts for kg and m3.
    Return cap_kg and cap_m3.
    '''

    # Create empty lists of capacities of kg and m3.
    cap_kg = []
    cap_m3 = []

    # Append capacities to empty lists.
    for i in range(len(spacecraft_list)):
        cap_kg.append(spacecraft_list[i].kg)
        cap_m3.append(spacecraft_list[i].m3)
    return cap_kg, cap_m3

## 4 FUNCTIONS FOR STARTING POINT: greedy/ random
def greedy_fill(list1, list2, list3, item, item2):
    '''Arguments: list1, list3, list3, item and item2.
    Fill list3 with items of list2, based on variable item.
    When full go to next. If item2!=false, take other variable into account.
    Return list3.
    '''

    if (item2 == False):
        for j in range(len(list3)-1):

            # define availability in spacecraft
            mass_av = getattr(list1[j], item)
            for i in range(len(list2)):

                # check if cargo-item is already placed
                if (getattr(list2[i], item) != 'nan'):
                    if (getattr(list2[i], item) <= mass_av):
                        list3[j].append(classes.cargo1(list2[i].number,
                         list2[i].kg, list2[i].m3))
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
                    if (getattr(list2[i], item) <= mass_av and getattr(list2[i],
                     item2) <= av_1):
                        list3[j].append(classes.cargo1(list2[i].number,
                         list2[i].kg, list2[i].m3))
                        mass_av -= getattr(list2[i], item)
                        av_1 -= getattr(list2[i], item2)
                        setattr(list2[i], item, 'nan')

        # create leftover list and put in spacecraft list without nan
        for k in range(len(list2)):
            if (getattr(list2[k], item) != 'nan'):
                list3[len(list3)-1].append(list2[k])
        return list3

def random_fill(list1, list2, list3):
    '''Arguments: list1, list2 and list3.
    Place elements of list2 randomly in array of lists list3.
    '''

    for i in range(len(list2)):
        # select random list to put item in
        number_list = range(len(list3))
        index = random.choice(number_list)
        sum_kg = sum(c.kg for c in list3[index]); sum_m3 = sum(c.m3 for c in
         list3[index]);
        kg_item = getattr(list2[i], "kg"); m3_item = getattr(list2[i], "m3");
        # check for kg and m3 restriction
        if (sum_kg + kg_item > getattr(list1[index], "kg")
        or sum_m3 + m3_item > getattr(list1[index], "m3")):
            # put in leftover list if item doesn't fit in the selected list
            list3[len(list3)-1].append(list2[i])
        else:
            list3[index].append(list2[i])

## 5: ITERATIVE ALGORITHMS
def hillclimbing1(runtime, spacecrafts, cap_kg, cap_m3):
    '''Arguments: runtime, spacecrafts, cap_kg and cap_m3.
    Run for desegnated runtime.
    Swap two random items from spacecrafts.
    Check whether capacitie restrictions are met, swap back if not.
    If score improves, accept swap. If not, swap back.
    Return score, x, iteration, score_end, numb_swaps.
    '''
    # Counter
    iteration = 0

    # Create empty list for score.
    score = []

    # Start program.
    program_starts = time.time()
    t_run = runtime
    t_end = time.time() + t_run
    numb_swaps = 0
    t_start = time.time()

    while time.time() < t_end:
        # randomly select two indices of lists and two items to swap between,
        # put in array.
        rand_arr = random1(spacecrafts)
        # run hillclimbing algorithm with rand_arr
        check = swap_two(spacecrafts, rand_arr, cap_kg, cap_m3)
        values = check_swap(check[0], rand_arr, cap_kg, cap_m3, check[1])
        # count number of swaps
        numb_swaps += values[0]
        # put score in array
        score.append(values[1])
        iteration += 1
    x = numpy.linspace(0, t_run, len(score))
    score_end = val_leftover(spacecrafts[len(spacecrafts)-1])
    return score, x, iteration, score_end, numb_swaps

def hillclimbing2(runtime, spacecrafts, cap_kg, cap_m3):
    '''Arguments: runtime, spacecrafts, cap_kg and cap_m3.
    Run for desegnated runtime.
    Swap random amounts of random items from spacecrafts.
    Check whether capacitie restrictions are met, swap back if not.
    If score improves, accept swap. If not, swap back.
    Return score, x, iteration, score_end, numb_swaps.
    '''

    # Counter
    iteration = 0

    # Create empty list for score.
    score=[]

    # Start program.
    program_starts = time.time()
    t_run = runtime
    t_end = time.time() + t_run
    numb_swaps = 0

    while time.time() < t_end:
        rand_ar2 = random2(spacecrafts, [1,2])
        check_swap = check_swap_random(spacecrafts, rand_ar2, cap_kg, cap_m3,
         False)

        if check_swap != None:
            num = check_swap[1]
            item = check_swap[2]
            random_arr = check_swap[3]
            scorevalue = swap_random2(spacecrafts, random_arr, num, item)
            numb_swaps += 1
            score.append(scorevalue)
        else:
            score.append(val_leftover(spacecrafts[len(spacecrafts)-1]))
        iteration += 1
    x = numpy.linspace(0, t_run, len(score))
    score_end = val_leftover(spacecrafts[len(spacecrafts)-1])
    return score, x, iteration, score_end, numb_swaps

def annealing1(runtime, spacecrafts, cap_kg, cap_m3, schedule):
    '''Arguments: runtime, spacecrafts, cap_kg, cap_m3 and schedule.
    Run simulated annealing algorithm.
    Swap two items at a time during the desegnated runtime.
    Use exponential or sigmoidal cooling schedule.
    Return score, x, score_end and iteration.
    '''

    # Create empty list for score.
    score = []

     # Initial and end temperatures for cooling schedule.
    temp_initial = 800
    temp_end = 0.0000000001

    LEN = len(spacecrafts)

    # Set counters for iterations and instances of accepted increases in the
    # objective function.
    iteration = 0
    accepted = 0

    LEN = len(spacecrafts)

    # Start timer
    start_time = time.time()
    t_end = time.time() + runtime

    while time.time() < t_end:
        # Store score before swapping items.
        old_score = val_leftover(spacecrafts[LEN - 1])

        if schedule == 'exponential':
            # Exponential cooling schedule
            temp_current = temp_initial * math.pow((temp_end / temp_initial),
            ((time.time() - start_time) / runtime))
        elif schedule == 'sigmoidal':
            # Sigmoidal cooling schedule
            temp_current = temp_end + (temp_initial - temp_end) * (1 / (1 + math.exp(0.3
            * (time.time() - start_time - (runtime / 2)))))

        # Random number between 0 and 1 for rejection criterion.
        random_num = random.uniform(0,1)

        # Randomly select two indices of lists and two items to swap between,
        # put in array.
        rand_arr = random1(spacecrafts)

        # Run hillclimbing algorithm with rand_arr.
        swap_two(spacecrafts, rand_arr, cap_kg, cap_m3)

        sum_kg1 = sum_kg(spacecrafts[0:LEN])
        sum_m31 = sum_m3(spacecrafts[0:LEN])
        value = 0

        for i in rand_arr[0:2]:
            # Check if list selected list isn't leftover list.
            if i < (LEN-1):
                # Check for kg and m3 restriction.
                if sum_kg1[i] > cap_kg[i] or sum_m31[i] > cap_m3[i]:
                    value = 1

        # Swap back if necessary
        if (value == 1):
            swap_two(spacecrafts, rand_arr, cap_kg, cap_m3)

        # Store new score after swapping items.
        new_score = val_leftover(spacecrafts[LEN-1])

        # Change in score
        change = new_score - old_score

        # Rejection criteria
        if temp_current > 0:
            # Check if new score is worse than old score.
            if old_score < new_score and value == 0:
                # Check whether change fails to meet acceptance criteria.
                if random_num >= math.exp(-change / temp_current):
                    # Swap items back
                    swap_two(spacecrafts, rand_arr, cap_kg, cap_m3)
                else:
                    # Increment acceptances
                    accepted +=1
        elif old_score < new_score and value == 0:
            swap_two(spacecrafts, rand_arr, cap_kg, cap_m3)

        # Append new score to score function.
        score.append(val_leftover(spacecrafts[LEN-1]))
        # Increment iterations
        iteration += 1

    x = numpy.linspace(0, runtime, len(score))
    score_end = val_leftover(spacecrafts[len(spacecrafts)-1])

    return score, x, score_end, iteration

def annealing2(runtime, spacecrafts, cap_kg, cap_m3, schedule):
    '''Arguments: runtime, spacecrafts, cap_kg, cap_m3 and schedule.
    Run simulated annealing algorithm.
    Swap random amount of items per iteration during the desegnated runtime.
    Use exponential or sigmoidal cooling schedule.
    Return score, x, score_end and iteration.
    '''
    score = []

     # initial and end temperatures for cooling schedule
    temp_initial = 800
    temp_end = 0.0000000001

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

    score_end = val_leftover(spacecrafts[len(spacecrafts)-1])
    x = numpy.linspace(0, runtime, len(score))

    return score, x, iteration, score_end


## 6: SWAP FUNCTIONS
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

def swap_random2(list1, array1, num, item):
    ''' swaps the randomly selected items of array1 with list1[num][item]'''
    # add random elements to list and remove from leftover list
    len_lst = len(list1)
    len_ar = len(array1)
    list1[num].extend(array1)
    list1[len(list1)-1].append(list1[num][item])
    list1[num].remove(list1[num][item])
    for i in range(len_ar):
        list1[len(list1)-1].remove(array1[i])
    return val_leftover(list1[len(list1)-1])


## 7: CHECK_SWAP FUNCTIONS
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

def check_swap_random(list1, array1, cap_kg, cap_m3, annealing):
    ''' function that checks for a possible swap between a random array (array1) of a list and an item of list1 '''
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
                        break;


    # return correct values for hillclimber or annealing
    # annealing is true so return change
    if get_item == 'annealing':
        return change, num, item, random_arr
    # swap that improves score has been found (get_item = true)
    elif get_item == True:
        return False, num, item, random_arr

# 8: FUNCTIONS THAT SELECT RANDOM ITEMS FROM SPACECRAFTS
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

## 9 : FUNCTIONS TO PLOT SCORES
def createdata(datalist):
    ''' function that places the input data in a suitable format for plotly '''
    data = []
    for i in range(len(datalist)):
        data.append(go.Scattergl(
            name = datalist[i][0],
            x = datalist[i][1],
            y = datalist[i][2],
            line = dict(
                width = 1.5)));
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

def sortbardata(scores, minimum, maximum):
    ''' sorts an array of into an array with amount of numbers per category
    each category is defined as: min+steps*stepsize - min + 1 + steps*stepsize
    where stepsize is equal to (max-min)/steps'''
    steps = (maximum - minimum)*2
    data = []
    stepsize = float(maximum - minimum)/float(steps)
    for i in range(len(scores)):
        data.append([0]*(steps+1));
        for j in range(len(scores[i])):
            for k in range(steps):
                if scores[i][j] >= (minimum + k * stepsize) and scores[i][j] < (minimum + (k+1) * stepsize):
                    data[i][k] += 1
            if scores[i][j] >= (minimum + (steps+1) * stepsize):
                data[i][steps] += 1
    return data, minimum, maximum, steps

def createbardata(data, minimum, maximum, steps, legend):
    ''' places array called data in suitable barchart format for plotly '''
    returndata = []
    # calculate stepsize
    stepsize = float(maximum - minimum)/float(steps)
    # create x-array with categorical names
    x_arr = []
    for k in range(steps):
        s = "-";
        seq = (str(minimum+k*stepsize), str(minimum+(k+1)*stepsize))
        x_arr.append(s.join(seq))
    z = "+"; seq=(str(maximum), str());
    x_arr.append(z.join(seq));

    # put data in suitable format
    for i in range(len(data)):
        returndata.append(go.Bar(
            x = x_arr,
            y = data[i],
            name = legend[i]))

    return returndata, x_arr

def makebarchart(title, data, filename):
    ''' create barchart with title and input data '''
    layout = go.Layout(
        title = title,
        barmode='group')

    fig = go.Figure(data=data, layout=layout)
    py.iplot(fig, filename=filename)
