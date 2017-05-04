import classes

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

def greedy_fill(list1, list2, list3, item):
    ''' fill list3 with items of list2, based on variable item. When full go to next'''
    for j in range(len(list3)-1):
        # define available mass in spacecraft
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
    # print kg's per spacecraft
    for j in range(4):
    	print list1[j].name
    	for i in range(len(list2[j])):
    		print list2[j][i].kg

def print_m3(list1, list2):
    # print kg's per spacecraft
    for j in range(4):
    	print spacecraft_list[j].name
    	for i in range(len(spacecrafts[j])):
    		print spacecrafts[j][i].m3

# def availability(list1, list2):
#     for j in range(4):
#     	print list1[j].name
#     	sum_kg = 0
#     	sum_m3 = 0
#     	for i in range(len(list2[j])):
#     		sum_kg += list2[j][i].kg
#     		sum_m3 += list2[j][i].m3
#     	print sum_kg
#     	print sum_m3
