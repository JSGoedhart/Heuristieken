# Thrown away helpers files

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

swap_random kan in principe weg: vervangen door check_swap_random en swap_random2
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
                # check if swapping would not break the restrictions
                if (kg_over[i] + list1[i][j].kg >= sum_kg_rand and m3_over[i] + list1[i][j].m3 >= sum_m3_rand):
                    # check for annealing (true) or hillclimber
                    # check if score random elements is better than selected
                    if (list1[i][j].valtot < score_rand):
                        get_item = True
                        num = i
                        item = j
                        control = 1
                        break;
    # swap if possible
    if (get_item == True):

        numb_swaps += 1
        # add random elements to list and remove from leftover list
        list1[num].extend(random_arr)
        list1[len_lst-1].append(list1[num][item])
        list1[num].remove(list1[num][item])
        for i in range(len_ar):
            list1[len_lst -1].remove(random_arr[i])
    return [numb_swaps, val_leftover(list1[len_lst-1])]
