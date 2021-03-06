from helpers_clean import *

## 10: FUNCTIONS FOR PART D + E
def greedy_fleet_with_check(spacecraft_list, cargolist):
    ''' fills fleet with all the cargo (exercise d and e)'''

    # create lists to put cargo-classes in
    spacecrafts_fleet = []
    numbers_fleet = []

    leftover_list = cargolist
    count = 0
    while len(leftover_list) != 0:
        count += 1
        temp_spacecrafts = [[], []]
        temp_number = []
        temp_cargo = leftover_list
        greedy = greedy_fill_fleet_with_check(spacecraft_list, temp_cargo, temp_spacecrafts, temp_number, 'm3', 'kg')
        leftover_list = temp_spacecrafts[len(temp_spacecrafts)-1]
        spacecrafts_fleet.append(temp_spacecrafts)
        numbers_fleet.append(greedy[1])

    # delete the leftoverlists
    spacecrafts_fleet = delete_leftover(spacecrafts_fleet)

    return spacecrafts_fleet, numbers_fleet

def greedy_fleet(spacecraft_list, cargolist):
    ''' fills fleet with all the cargo (exercise d and e)'''

    # create lists to put cargo-classes in
    spacecrafts_fleet = []

    leftover_list = cargolist
    count = 0
    while len(leftover_list) != 0:
        count += 1
        temp_spacecrafts = [[], []]
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
        # print "fleet", k
        for j in range(len(spacecrafts_fleet[k])):
            kg = 0
            m3 = 0
            # print "spacecraft", j
            for i in range(len(spacecrafts_fleet[k][j])):
                # print "cargo", i
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

def greedy_fill_fleet_with_check(spacecraft_list, cargolist, list3, number, item, item2):
    ''' fills the 5 spacecrafts of the fleet and makes a choice between cygnus and dragon of america'''
    for j in range(len(list3)-1):

        # fill both dragon and cygnus, check which one is better and use the better one
        temp_Dragon = []
        temp_Cygnus = []
        temp_Verne = []
        temp_Progress = []
        temp_Kounotori = []
        temp_TianZhou = []

        temp_cargolist_dragon = cargolist
        temp_cargolist_cygnus = cargolist
        temp_cargolist_Verne = cargolist
        temp_cargolist_Progress = cargolist
        temp_cargolist_Kounotori = cargolist
        temp_cargolist_TianZhou = cargolist

        mass_av_cygnus = getattr(spacecraft_list[5], item)
        av_1_cygnus = getattr(spacecraft_list[5], item2)
        mass_av_dragon = getattr(spacecraft_list[2], item)
        av_1_dragon = getattr(spacecraft_list[2], item2)
        mass_av_Verne = getattr(spacecraft_list[4], item)
        av_1_Verne = getattr(spacecraft_list[4], item2)
        mass_av_Progress = getattr(spacecraft_list[3], item)
        av_1_Progress = getattr(spacecraft_list[3], item2)
        mass_av_Kounotori = getattr(spacecraft_list[1], item)
        av_1_Kounotori = getattr(spacecraft_list[1], item2)
        mass_av_TianZhou = getattr(spacecraft_list[0], item)
        av_1_TianZhou = getattr(spacecraft_list[0], item2)

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
        for i in range(len(temp_cargolist_Kounotori)):
            if (getattr(temp_cargolist_Kounotori[i], item) != 'nan'):
                if(getattr(temp_cargolist_Kounotori[i], item) <= mass_av_Kounotori and getattr(temp_cargolist_Kounotori[i], item2) <= av_1_Kounotori):
                    temp_Kounotori.append(classes.cargo1(temp_cargolist_Kounotori[i].number, temp_cargolist_Kounotori[i].kg, temp_cargolist_Kounotori[i].m3))
                    mass_av_Kounotori -= getattr(temp_cargolist_Kounotori[i], item)
                    av_1_Kounotori -= getattr(temp_cargolist_Kounotori[i], item2)
        for i in range(len(temp_cargolist_Progress)):
            if (getattr(temp_cargolist_Progress[i], item) != 'nan'):
                if(getattr(temp_cargolist_Progress[i], item) <= mass_av_Progress and getattr(temp_cargolist_Progress[i], item2) <= av_1_Progress):
                    temp_Progress.append(classes.cargo1(temp_cargolist_Progress[i].number, temp_cargolist_Progress[i].kg, temp_cargolist_Progress[i].m3))
                    mass_av_Progress -= getattr(temp_cargolist_Progress[i], item)
                    av_1_Progress -= getattr(temp_cargolist_Progress[i], item2)
        for i in range(len(temp_cargolist_Verne)):
            if (getattr(temp_cargolist_Verne[i], item) != 'nan'):
                if(getattr(temp_cargolist_Verne[i], item) <= mass_av_Verne and getattr(temp_cargolist_Verne[i], item2) <= av_1_Verne):
                    temp_Verne.append(classes.cargo1(temp_cargolist_Verne[i].number, temp_cargolist_Verne[i].kg, temp_cargolist_Verne[i].m3))
                    mass_av_Verne -= getattr(temp_cargolist_Verne[i], item)
                    av_1_Verne -= getattr(temp_cargolist_Verne[i], item2)
        for i in range(len(temp_cargolist_TianZhou)):
            if (getattr(temp_cargolist_TianZhou[i], item) != 'nan'):
                if(getattr(temp_cargolist_TianZhou[i], item) <= mass_av_TianZhou and getattr(temp_cargolist_TianZhou[i], item2) <= av_1_TianZhou):
                    temp_TianZhou.append(classes.cargo1(temp_cargolist_TianZhou[i].number, temp_cargolist_TianZhou[i].kg, temp_cargolist_TianZhou[i].m3))
                    mass_av_TianZhou -= getattr(temp_cargolist_TianZhou[i], item)
                    av_1_TianZhou -= getattr(temp_cargolist_TianZhou[i], item2)
        # score check
        kg_dragon = 0
        m3_dragon = 0
        kg_cygnus = 0
        m3_cygnus = 0
        kg_progress = 0
        m3_progress = 0
        kg_tianzhou = 0
        m3_tianzhou = 0
        kg_verne = 0
        m3_verne = 0
        kg_kounotori = 0
        m3_kounotori = 0

        for i in range(len(temp_Dragon)):
            kg_dragon = kg_dragon + temp_Dragon[i].kg
            m3_dragon = m3_dragon + temp_Dragon[i].m3
        procent_kg_dragon = kg_dragon/spacecraft_list[2].kg
        procent_m3_dragon = m3_dragon/spacecraft_list[2].m3
        for i in range(len(temp_Cygnus)):
            kg_cygnus = kg_cygnus + temp_Cygnus[i].kg
            m3_cygnus = m3_cygnus + temp_Cygnus[i].m3
        procent_kg_cygnus = kg_cygnus/spacecraft_list[5].kg
        procent_m3_cygnus = m3_cygnus/spacecraft_list[5].m3
        for i in range(len(temp_Verne)):
            kg_verne = kg_verne + temp_Verne[i].kg
            m3_verne = m3_verne + temp_Verne[i].m3
        procent_kg_verne = kg_verne/spacecraft_list[4].kg
        procent_m3_verne = m3_verne/spacecraft_list[4].m3
        for i in range(len(temp_Kounotori)):
            kg_kounotori = kg_kounotori + temp_Kounotori[i].kg
            m3_kounotori = m3_kounotori + temp_Kounotori[i].m3
        procent_kg_kounotori = kg_kounotori/spacecraft_list[1].kg
        procent_m3_kounotori = m3_kounotori/spacecraft_list[1].m3
        for i in range(len(temp_Progress)):
            kg_progress = kg_progress + temp_Progress[i].kg
            m3_progress = m3_progress + temp_Progress[i].m3
        procent_kg_progress = kg_progress/spacecraft_list[3].kg
        procent_m3_progress = m3_progress/spacecraft_list[3].m3
        for i in range(len(temp_TianZhou)):
            kg_tianzhou = kg_tianzhou + temp_TianZhou[i].kg
            m3_tianzhou = m3_tianzhou + temp_TianZhou[i].m3
        procent_kg_tianzhou = kg_tianzhou/spacecraft_list[0].kg
        procent_m3_tianzhou = m3_tianzhou/spacecraft_list[0].m3

        dragon =  procent_m3_dragon + procent_kg_dragon
        cygnus =  procent_m3_cygnus + procent_kg_cygnus
        tianzhou = procent_m3_tianzhou + procent_kg_tianzhou
        verne = procent_m3_verne + procent_kg_verne
        progress = procent_m3_progress + procent_kg_progress
        kounotori = procent_m3_kounotori + procent_kg_kounotori

        mass_av_cygnus1 = getattr(spacecraft_list[5], item)
        av_1_cygnus1 = getattr(spacecraft_list[5], item2)
        mass_av_dragon1 = getattr(spacecraft_list[2], item)
        av_1_dragon1 = getattr(spacecraft_list[2], item2)
        mass_av_Verne1 = getattr(spacecraft_list[4], item)
        av_1_Verne1 = getattr(spacecraft_list[4], item2)
        mass_av_Progress1 = getattr(spacecraft_list[3], item)
        av_1_Progress1 = getattr(spacecraft_list[3], item2)
        mass_av_Kounotori1 = getattr(spacecraft_list[1], item)
        av_1_Kounotori1 = getattr(spacecraft_list[1], item2)
        mass_av_TianZhou1 = getattr(spacecraft_list[0], item)
        av_1_TianZhou1 = getattr(spacecraft_list[0], item2)

        # vul de spacecraft die beter is (dus meer gevuld)
        # vul dragon:
        if  dragon >= cygnus and dragon >= tianzhou and dragon >= verne and dragon >= progress and dragon >= kounotori:
            number = 2
            for i in range(len(cargolist)):
                # check if cargo-item is already placed
                if (getattr(cargolist[i], item) != 'nan'):
                    if (getattr(cargolist[i], item) <= mass_av_dragon1 and getattr(cargolist[i], item2) <= av_1_dragon1):
                        list3[j].append(classes.cargo1(cargolist[i].number, cargolist[i].kg, cargolist[i].m3))
                        mass_av_dragon1 -= getattr(cargolist[i], item)
                        av_1_dragon1 -= getattr(cargolist[i], item2)
                        setattr(cargolist[i], item, 'nan')
        # anders vul cygnus:
        elif  cygnus > dragon and cygnus >= tianzhou and cygnus >= verne and cygnus >= progress and cygnus >= kounotori:
            number = 5
            for i in range(len(cargolist)):
                # check if cargo-item is already placed
                if (getattr(cargolist[i], item) != 'nan'):
                    if (getattr(cargolist[i], item) <= mass_av_cygnus1 and getattr(cargolist[i], item2) <= av_1_cygnus1):
                        list3[j].append(classes.cargo1(cargolist[i].number, cargolist[i].kg, cargolist[i].m3))
                        mass_av_cygnus1 -= getattr(cargolist[i], item)
                        av_1_cygnus1 -= getattr(cargolist[i], item2)
                        setattr(cargolist[i], item, 'nan')
        elif  verne > dragon and verne  >= tianzhou and verne  > cygnus and verne  >= progress and verne  >= kounotori:
            number = 4
            for i in range(len(cargolist)):
                # check if cargo-item is already placed
                if (getattr(cargolist[i], item) != 'nan'):
                    if (getattr(cargolist[i], item) <= mass_av_Verne1 and getattr(cargolist[i], item2) <= av_1_Verne1):
                        list3[j].append(classes.cargo1(cargolist[i].number, cargolist[i].kg, cargolist[i].m3))
                        mass_av_Verne1 -= getattr(cargolist[i], item)
                        av_1_Verne1 -= getattr(cargolist[i], item2)
                        setattr(cargolist[i], item, 'nan')
        elif  tianzhou > dragon and tianzhou > verne and tianzhou  > cygnus and tianzhou  >= progress and tianzhou  >= kounotori:
            number = 0
            for i in range(len(cargolist)):
                # check if cargo-item is already placed
                if (getattr(cargolist[i], item) != 'nan'):
                    if (getattr(cargolist[i], item) <= mass_av_TianZhou1 and getattr(cargolist[i], item2) <= av_1_TianZhou1):
                        list3[j].append(classes.cargo1(cargolist[i].number, cargolist[i].kg, cargolist[i].m3))
                        mass_av_TianZhou1 -= getattr(cargolist[i], item)
                        av_1_TianZhou1 -= getattr(cargolist[i], item2)
                        setattr(cargolist[i], item, 'nan')
        elif  progress > dragon and progress > verne and progress  > cygnus and progress  > tianzhou and progress  >= kounotori:
            number = 3
            for i in range(len(cargolist)):
                # check if cargo-item is already placed
                if (getattr(cargolist[i], item) != 'nan'):
                    if (getattr(cargolist[i], item) <= mass_av_Progress1 and getattr(cargolist[i], item2) <= av_1_Progress1):
                        list3[j].append(classes.cargo1(cargolist[i].number, cargolist[i].kg, cargolist[i].m3))
                        mass_av_Progress1 -= getattr(cargolist[i], item)
                        av_1_Progress1 -= getattr(cargolist[i], item2)
                        setattr(cargolist[i], item, 'nan')
        else:
            number = 1
            for i in range(len(cargolist)):
                # check if cargo-item is already placed
                if (getattr(cargolist[i], item) != 'nan'):
                    if (getattr(cargolist[i], item) <= mass_av_Kounotori1 and getattr(cargolist[i], item2) <= av_1_Kounotori1):
                        list3[j].append(classes.cargo1(cargolist[i].number, cargolist[i].kg, cargolist[i].m3))
                        mass_av_Kounotori1 -= getattr(cargolist[i], item)
                        av_1_Kounotori1 -= getattr(cargolist[i], item2)
                        setattr(cargolist[i], item, 'nan')

    # create leftover list and put in spacecraft list without nan
    for k in range(len(cargolist)):
        if (getattr(cargolist[k], item) != 'nan'):
            list3[len(list3)-1].append(cargolist[k])
    return list3, number

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

def hillclimbing_D_E(runtime, spacecrafts, leftover_spacecraft, number, cap_kg, cap_m3):
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
            check_swap = check_swap_random_D_E(spacecrafts, leftover_spacecraft, rand_ar2, number, cap_kg, cap_m3, False)
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

def hillclimbing_fleet(spacecrafts_fleet, spacecraft_list, numbers):
    ''' runs hillclimbing_D_E for every array of the five ships '''
    cap = capacities(spacecraft_list)
    cap_kg = cap[0]; cap_m3 = cap[1]
    num_fleet_used = 20

    # loop over last two groups of spacecrafts
    for k in range(num_fleet_used):
        # loop over the last group of spacecrafts
        for j in range(len(spacecrafts_fleet[len(spacecrafts_fleet) - k-1])):
            # select the leftover_spacecraft
            leftover_spacecraft = spacecrafts_fleet[len(spacecrafts_fleet) - k-1][j]
            number = numbers[len(numbers)-1-k]
            # check if leftover_spacecraft is nonzero
            if leftover_spacecraft:
                # loop over fleet and swap with leftoverspacecraft
                for i in range(len(spacecrafts_fleet)-k-1):
                    new_spacecrafts = hillclimbing_D_E(0.1, spacecrafts_fleet[i], leftover_spacecraft, number, cap_kg, cap_m3)
                    spacecrafts_fleet[i] = new_spacecrafts[0][0]
                    leftover_spacecraft = new_spacecrafts[0][1]

    # merge used spacecrafts
    spacecrafts_fleet = merge_used_spacecrafts(spacecrafts_fleet, num_fleet_used, spacecraft_list)

    return spacecrafts_fleet


def check_swap_random_D_E(spacecrafts, leftover_spacecraft, array1, number, cap_kg, cap_m3, annealing):
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

    # unfilled space, kg and m3 per spacecraft:
    kg_over = []
    m3_over = []
    kg_over.append(cap_kg[number]- sum_kg1[0])
    m3_over.append(cap_m3[number]- sum_m31[0])

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

    # new leftover list
    new_leftovers = []

    for k in range(num):
        for i in range(len(spacecrafts_fleet[len(spacecrafts_fleet)-1])):
            for j in range(len(spacecrafts_fleet[len(spacecrafts_fleet)-1][i])):
                new_leftovers.append(classes.cargo1(spacecrafts_fleet[len(spacecrafts_fleet)-1][i][j].number, spacecrafts_fleet[len(spacecrafts_fleet)-1][i][j].kg, spacecrafts_fleet[len(spacecrafts_fleet)-1][i][j].m3)) 
                
        # remove spacecrafts filled with leftovers
        spacecrafts_fleet.remove(spacecrafts_fleet[len(spacecrafts_fleet)-1])

    # do greedy again with the used leftovers
    extra_spacecraft_fleet = greedy_fleet(spacecraft_list, new_leftovers)

    spacecrafts_fleet.extend(extra_spacecraft_fleet)

    return spacecrafts_fleet

def annealing_D_E(runtime, spacecrafts, leftover_spacecraft, number, cap_kg, cap_m3, schedule):
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
            new_spacecrafts = [spacecrafts, leftover_spacecraft]
        else:
            # create random array that selects 1 or 2 items from the leftover list
            rand_ar2 = random_D_E(leftover_spacecraft, [1,2])

            check_swap = check_swap_random_D_E(spacecrafts, leftover_spacecraft, rand_ar2, number, cap_kg, cap_m3, True)
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

def annealing_fleet(spacecrafts_fleet, spacecraft_list, numbers):
    ''' runs annealing_D_E for every array of the five ships '''
    cap = capacities(spacecraft_list)
    cap_kg = cap[0]; cap_m3 = cap[1]
    num_fleet_used = 20

    global new_spacecrafts

    # loop over last two groups of spacecrafts
    for k in range(num_fleet_used):
        # loop over the last group of spacecrafts
        for j in range(len(spacecrafts_fleet[len(spacecrafts_fleet) - k-1])):
            # select the leftover_spacecraft
            leftover_spacecraft = spacecrafts_fleet[len(spacecrafts_fleet) - k-1][j]
            number = numbers[len(numbers)-1-k]
            
            # check if leftover_spacecraft is nonzero
            if leftover_spacecraft:
                # loop over fleet and swap with leftoverspacecraft
                for i in range(len(spacecrafts_fleet)-k-1):
                    new_spacecrafts = annealing_D_E(0.1, spacecrafts_fleet[i], leftover_spacecraft, number, cap_kg, cap_m3, 'sigmoidal')
                    spacecrafts_fleet[i] = new_spacecrafts[0][0]
                    leftover_spacecraft = new_spacecrafts[0][1]

    # merge used spacecrafts
    spacecrafts_fleet = merge_used_spacecrafts(spacecrafts_fleet, num_fleet_used, spacecraft_list)

    return spacecrafts_fleet