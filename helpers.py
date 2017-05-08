import classes
import random

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

def swap(a, b):
    ''' function that swaps to elements '''
    return b, a

def swap_two(list1, rand_arr, cap_kg, cap_m3):
    ''' swap items from list1 and check if this is possible with cap1 and cap2 '''
    numb_swaps = 0
    length = len(list1)
    # calculate scorefunction before swapping
    score_old = val_leftover(list1[length-1])
    # swap
    list1[rand_arr[0]][rand_arr[2]], list1[rand_arr[1]][rand_arr[3]] = swap(list1[rand_arr[0]][rand_arr[2]], list1[rand_arr[1]][rand_arr[3]]) 
    # calculate new values of kg, m3 and valtot (score)
    sum_kg1 = sum_kg(list1[0:length])
    sum_m31 = sum_m3(list1[0:length])
    score_new = val_leftover(list1[length-1])
    # print rand_arr
    # print 'scores oud en nieuw', score_old, score_new
    # if (rand_arr[0] < 4):
    #     print 'lijst1, capaciteit en som kg', cap_kg[rand_arr[0]], sum_kg1[rand_arr[0]]
    #     print 'lijst1, capaciteit en som m3', cap_m3[rand_arr[0]], sum_m31[rand_arr[0]]
    # if (rand_arr[1] < 4):
    #     print 'lijst2, capaciteit en som kg', cap_kg[rand_arr[1]], sum_kg1[rand_arr[1]]
    #     print 'lijst2, capaciteit en som m3', cap_m3[rand_arr[1]], sum_m31[rand_arr[1]]

    # check for swaprestrictions for the two selected lists
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
    return check_swap


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

def swap_random(list1, array1, cap_kg, cap_m3):
    numb_swaps = 0
    ''' swaps a randomly selected amount of items of a specified list, with an item of another list, if possible '''
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
    score_old = val_leftover(list1[len_lst-1])

    # overige capaciteit, kg en m3 per spacecraft:
    kg_over = []
    m3_over = []
    for i in range(len(cap_kg)):
        kg_over.append(cap_kg[i]- sum_kg1[i])
        m3_over.append(cap_m3[i]- sum_m31[i])

    # loop through lists to check if there exists an element the random elements can be swapped with
    get_item = False
    control = 0
    for i in range(len_lst-1):
        if control != 1:
            for j in range(len(list1[i])):
                # check if score random elements is better than selected
                if (list1[i][j].valtot < score_old):
                    # check if swapping would not break the restrictions, if not save values and break
                    if (kg_over[i] + list1[i][j].kg >= sum_kg_rand and m3_over[i] + list1[i][j].m3 >= sum_m3_rand):
                        get_item = True
                        num = i
                        item = j
                        control = 1
                        break
    # swap if possible
    if (get_item == True):
        numb_swaps += 1
        # add random elements to list and remove from leftover list
        list1[num].extend(random_arr)
        list1[len_lst-1].append(list1[num][item])
        list1[num].remove(list1[num][item])
        for i in range(len_ar):
            list1[len_lst -1].remove(random_arr[i])
    return numb_swaps
