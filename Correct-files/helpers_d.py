from helpers_clean import *

## 10: FUNCTIONS FOR PART D + E
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

    # delete the leftoverlists
    spacecrafts_fleet = delete_leftover(spacecrafts_fleet)

    return spacecrafts_fleet

def delete_leftover(spacecrafts_fleet_old):
    ''' deletes the leftoverlists in spacecrafts_fleet'''

    spacecrafts_fleet = []
    for i in range(len(spacecrafts_fleet_old)):
        temp_list = []
        for j in range(len(spacecrafts_fleet_old[i])-1):
            temp_list.append(spacecrafts_fleet_old[i][j])
        spacecrafts_fleet.append(temp_list)

    return spacecrafts_fleet

def scorefunction(spacecrafts_fleet, spacecraft_list):
    ''' calculates the total wasted space and gives a score '''

    score_kg = 0
    score_m3 = 0

    # score function:
    for k in range(len(spacecrafts_fleet)):
        for j in range(len(spacecrafts_fleet[k])):
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
        for j in range(len(spacecrafts_fleet[k])):
            if spacecrafts_fleet[k][j]:
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

def random_D_E(leftover_spacecraft, array2):
    ''' returns an random amount of randomly selected items from one list and a random item from another random selected list '''
    # array to return randomly selected indices
    retour = []
    # create array to randomly select a list and select two items that cannot be equal
    amount = random.choice(array2)
    rand_range = range(len(leftover_spacecraft))
    # print rand_range
    for i in range(amount):
        rand_item = random.choice(rand_range)
        retour.append(rand_item)
        rand_range.remove(rand_item)
    return retour

def hillclimbing_D_E(runtime, spacecrafts, leftover_spacecraft, cap_kg, cap_m3):
    ''' swaps elements from the given spacecraft with a random spacecraft, within the given time'''
    score=[]
    program_starts = time.time()
    t_run = runtime
    t_end = time.time() + t_run
    numb_swaps = 0
    while time.time() < t_end:
        if len(leftover_spacecraft)==1:
            # print "one"
            new_spacecrafts = [spacecrafts, leftover_spacecraft]
        else:
            rand_ar2 = random_D_E(leftover_spacecraft, [1,2])
            check_swap = check_swap_random_D_E(spacecrafts, leftover_spacecraft, rand_ar2, cap_kg, cap_m3, False)
            if check_swap != None:
                num = check_swap[1]
                item = check_swap[2]
                random_arr = check_swap[3]
                new_spacecrafts = swap_random_D_E(spacecrafts, leftover_spacecraft, random_arr, num, item)
                numb_swaps += 1
            else:
                new_spacecrafts = [spacecrafts, leftover_spacecraft]
    x = numpy.linspace(0, t_run, len(score))
    return new_spacecrafts, x, numb_swaps

def hillclimbing_fleet(spacecrafts_fleet, spacecraft_list):
    ''' runs hillclimbing_D_E for every array of the five ships '''
    cap = capacities(spacecraft_list)
    cap_kg = cap[0]; cap_m3 = cap[1]
    num_fleet_used = 5

    # loop over last two groups of spacecrafts
    for k in range(num_fleet_used):
        # loop over the last group of spacecrafts
        for j in range(len(spacecrafts_fleet[len(spacecrafts_fleet) - k-1])):
            # select the leftover_spacecraft

            leftover_spacecraft = spacecrafts_fleet[len(spacecrafts_fleet) - k-1][j]

            # check if leftover_spacecraft is nonzero
            if leftover_spacecraft:
                # loop over fleet and swap with leftoverspacecraft
                for i in range(len(spacecrafts_fleet)-k-1):
                    # print i, leftover_spacecraft
                    # print sum_kg(spacecrafts_fleet[i])
                    new_spacecrafts = hillclimbing_D_E(0.1, spacecrafts_fleet[i], leftover_spacecraft, cap_kg, cap_m3)
                    spacecrafts_fleet[i] = new_spacecrafts[0][0]
                    leftover_spacecraft = new_spacecrafts[0][1]
                    # print sum_kg(spacecrafts_fleet[i])
                    # print sum_m3(spacecrafts_fleet[i])
                    # print cap_kg
                    # print cap_m3
    # merge used spacecrafts
    spacecrafts_fleet = merge_used_spacecrafts(spacecrafts_fleet, num_fleet_used, spacecraft_list)
    for i in range(len(spacecrafts_fleet)):
        print "vloot", i
        print sum_kg(spacecrafts_fleet[i])
        print sum_m3(spacecrafts_fleet[i])

    return spacecrafts_fleet


def check_swap_random_D_E(spacecrafts, leftover_spacecraft, array1, cap_kg, cap_m3, annealing):
    ''' function that checks for a possible swap between a random array (array1) of a list and an item of list1 '''
    numb_swaps = 0
    ''' checks for restrictions to swaps a randomly selected amount of items of a specified list, with an item of another list, if possible '''
    len_ar = len(array1)
    len_lst = len(spacecrafts)
    # create array with randomly selected items from specified list
    random_arr = []
    for i in range(len_ar):
        random_arr.append(leftover_spacecraft[array1[i]])
    random_arr

    # calculate sums and score of items from specified list
    sum_kg_rand = sum(c.kg for c in random_arr)
    sum_m3_rand = sum(c.m3 for c in random_arr)
    score_rand = sum(c.valtot for c in random_arr)

    # calculate free m3 and kg per list of list1
    sum_kg1 = sum_kg(spacecrafts)
    sum_m31 = sum_m3(spacecrafts)
    old_score = val_leftover(leftover_spacecraft)

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
    for i in range(len_lst):
        if control != 1:
            for j in range(len(spacecrafts[i])):
                # check if swapping would not break the restrictions
                if (kg_over[i] + spacecrafts[i][j].kg >= sum_kg_rand and m3_over[i] + spacecrafts[i][j].m3 >= sum_m3_rand):
                    # check for annealing (true) or hillclimber
                    # check if score random elements is better than selected
                    if (spacecrafts[i][j].valtot < score_rand):
                        get_item = True
                        num = i
                        item = j
                        control = 1
                        new_score = old_score - score_rand + spacecrafts[i][j].valtot
                        change = new_score - old_score
                        break;
                    elif (annealing == True):
                        get_item = 'annealing'
                        num = i
                        item = j
                        control = 1
                        new_score = old_score - score_rand + spacecrafts[i][j].valtot
                        change = new_score - old_score
                        break;


    # return correct values for hillclimber or annealing
    # annealing is true so return change
    if get_item == 'annealing':
        return change, num, item, random_arr
    # swap that improves score has been found (get_item = true)
    elif get_item == True:
        return False, num, item, random_arr

def swap_random_D_E(spacecrafts, leftover_spacecraft, array1, num, item):
    ''' swaps the randomly selected items of array1 with list1[num][item]'''
    # add random elements to list and remove from leftover list
    len_lst = len(spacecrafts)
    len_ar = len(array1)
    spacecrafts[num].extend(array1)
    leftover_spacecraft.append(spacecrafts[num][item])
    spacecrafts[num].remove(spacecrafts[num][item])
    for i in range(len_ar):
        leftover_spacecraft.remove(array1[i])
    return spacecrafts, leftover_spacecraft

def merge_used_spacecrafts(spacecrafts_fleet, num, spacecraft_list):
    ''' merge used spacecrafts, num is amount of spacecraft fleets used'''
    #### merge used spacecrafts ######
    # for k in range(num):
    #     # put all cargo in first spacecraft
    #     for i in range(len(spacecrafts_fleet[len(spacecrafts_fleet)-1-k])):
    #         if i != 0:
    #             leftover_spacecraft = spacecrafts_fleet[len(spacecrafts_fleet)-1-k][i]
    #             if leftover_spacecraft:
    #                 for j in range(len(spacecrafts_fleet[len(spacecrafts_fleet)-1-k][i])):
    #                     spacecrafts_fleet[len(spacecrafts_fleet)-1-k][0].append(classes.cargo1(spacecrafts_fleet[len(spacecrafts_fleet)-k-1][i][j].number, spacecrafts_fleet[len(spacecrafts_fleet)-k-1][i][j].kg, spacecrafts_fleet[len(spacecrafts_fleet)-k-1][i][j].m3))
    #                 spacecrafts_fleet[len(spacecrafts_fleet)-1-k][i].remove(leftover_spacecraft[0])

    # # put all cargo off first spacecraft in first spacecraft of earlier fleet, if possible
    # for k in range(num):        
    #     if not spacecrafts_fleet[len(spacecrafts_fleet)-2-k][4]: 
    #         for i in range(len(spacecrafts_fleet[len(spacecrafts_fleet)-1-k][0])):
    #             spacecrafts_fleet[len(spacecrafts_fleet)-2-k][0].append(classes.cargo1(spacecrafts_fleet[len(spacecrafts_fleet)-k-1][0][i].number, spacecrafts_fleet[len(spacecrafts_fleet)-k-1][0][i].kg, spacecrafts_fleet[len(spacecrafts_fleet)-k-1][0][i].m3))
    #             spacecrafts_fleet[len(spacecrafts_fleet)-1-k][0].remove(spacecrafts_fleet[len(spacecrafts_fleet)-1-k][0][i])

    # # lose all empty groups of spacecrafts
    # for i in range(len(spacecrafts_fleet)):
    #     if not spacecrafts_fleet[i][0] and not spacecrafts_fleet[i][1] and not spacecrafts_fleet[i][2] and not spacecrafts_fleet[i][3] and not spacecrafts_fleet[i][4]:
    #         spacecrafts_fleet.remove(spacecrafts_fleet[i])

    # for i in range(len(spacecrafts_fleet)):
    #     print "vloot", i
    #     print sum_kg(spacecrafts_fleet[i])
    #     print sum_m3(spacecrafts_fleet[i])



    ######## make new leftover and fill greedy again

    # new leftover list
    new_leftovers = []

    for k in range(num):
        for i in range(len(spacecrafts_fleet[len(spacecrafts_fleet)-1])):
            for j in range(len(spacecrafts_fleet[len(spacecrafts_fleet)-1][i])):
                new_leftovers.append(spacecrafts_fleet[len(spacecrafts_fleet)-1][i][j])
        # remove spacecrafts filled with leftovers
        spacecrafts_fleet.remove(spacecrafts_fleet[len(spacecrafts_fleet)-1])

    # do greedy again with the used leftovers
    extra_spacecraft_fleet = greedy_fleet(spacecraft_list, new_leftovers)

    spacecrafts_fleet.extend(extra_spacecraft_fleet)

    ## add extra empty spacecrafts to fill the fleet
    # for i in range(5-len(spacecrafts_fleet[len(spacecrafts_fleet)-1])):
    #     # print i
    #     spacecrafts_fleet[len(spacecrafts_fleet)-1].append([])


    return spacecrafts_fleet

def annealing_D_E(runtime, spacecrafts, leftover_spacecraft, cap_kg, cap_m3, schedule):
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
        # store score before swapping items, volgens mij niet nodig
        # old_score = val_leftover(spacecrafts[LEN - 1])

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

        if len(leftover_spacecraft)==1:
            print "one"
            new_spacecrafts = [spacecrafts, leftover_spacecraft]
        else:
            print "two"
            print len(leftover_spacecraft)
            # create random array that selects 1 or 2 items from the leftover list
            rand_ar2 = random_D_E(leftover_spacecraft, [1,2])

            check_swap = check_swap_random_D_E(spacecrafts, leftover_spacecraft, rand_ar2, cap_kg, cap_m3, True)
            if check_swap != None:
                change = check_swap[0]
                num = check_swap[1]
                item = check_swap[2]
                random_arr = check_swap[3]

                # check if a swap with improved score function has been found
                if (change == False):
                    # better score, so swap
                    new_spacecrafts = swap_random_D_E(spacecrafts, leftover_spacecraft, random_arr, num, item)
                # check if annealing criteria allows for swap !!!!!!!!!!!!!!! criteria checken bij len!!!
                elif (random_num < math.exp(-change / temp_current)):
                    new_spacecrafts = swap_random_D_E(spacecrafts, leftover_spacecraft, random_arr, num, item)
            else:
                new_spacecrafts = [spacecrafts, leftover_spacecraft]

                iteration += 1
    x = numpy.linspace(0, runtime, len(score))

    return new_spacecrafts, x, iteration

def annealing_fleet(spacecrafts_fleet, spacecraft_list):
    ''' runs annealing_D_E for every array of the five ships '''
    cap = capacities(spacecraft_list)
    cap_kg = cap[0]; cap_m3 = cap[1]
    num_fleet_used = 3

    global new_spacecrafts

    # loop over last two groups of spacecrafts
    for k in range(num_fleet_used):
        # loop over the last group of spacecrafts
        for j in range(len(spacecrafts_fleet[len(spacecrafts_fleet) - k-1])):
            # select the leftover_spacecraft

            leftover_spacecraft = spacecrafts_fleet[len(spacecrafts_fleet) - k-1][j]

            # check if leftover_spacecraft is nonzero
            if leftover_spacecraft:
                # loop over fleet and swap with leftoverspacecraft
                for i in range(len(spacecrafts_fleet)-k-1):
                    # print i, leftover_spacecraft
                    # print sum_kg(spacecrafts_fleet[i])
                    new_spacecrafts = annealing_D_E(0.1, spacecrafts_fleet[i], leftover_spacecraft, cap_kg, cap_m3, 'sigmoidal')
                    spacecrafts_fleet[i] = new_spacecrafts[0][0]
                    leftover_spacecraft = new_spacecrafts[0][1]
                    # print sum_kg(spacecrafts_fleet[i])
                    # print sum_m3(spacecrafts_fleet[i])
                    # print cap_kg
                    # print cap_m3

    # merge used spacecrafts
    spacecrafts_fleet = merge_used_spacecrafts(spacecrafts_fleet, num_fleet_used, spacecraft_list)

    return spacecrafts_fleet






