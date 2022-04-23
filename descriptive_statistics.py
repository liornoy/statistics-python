DATA_FILE_NAME = "DataFile"


def calc_avg():
    f = open(DATA_FILE_NAME, "r")
    lines = f.readlines()
    f.close()
    count = 0
    nums_sum = 0

    for line in lines:
        line = line.strip()
        nums_arr = [int(val) for val in line.split()]
        nums_sum += sum(nums_arr)
        count = count + len(nums_arr)
    return nums_sum / count


def calc_variance():
    f = open(DATA_FILE_NAME, "r")
    lines = f.readlines()
    f.close()
    count = 0
    nums_sum = 0
    nums_sum_p2 = 0
    for line in lines:
        line = line.strip()
        nums_arr = [int(val) for val in line.split()]
        nums_arr_p2 = [pow(int(val), 2) for val in line.split()]
        nums_sum += sum(nums_arr)
        nums_sum_p2 += sum(nums_arr_p2)
        count = count + len(nums_arr)
    avg = nums_sum / count
    res = (nums_sum_p2 - count * pow(avg, 2)) / count
    return res


def get_max_value():
    f = open(DATA_FILE_NAME, "r")
    lines = f.readlines()
    f.close()
    max_val = 0
    flag = False
    for line in lines:
        line = line.strip()
        nums_arr = [int(val) for val in line.split()]
        for n in nums_arr:
            if flag == True:
                if n > max_val:
                    max_val = n
            else:
                max_val = n
                flag = True
    return max_val


def get_min_value():
    f = open(DATA_FILE_NAME, "r")
    lines = f.readlines()
    f.close()
    min_val = 0
    flag = False
    for line in lines:
        line = line.strip()
        nums_arr = [int(val) for val in line.split()]
        for n in nums_arr:
            if flag == True:
                if n < min_val:
                    min_val = n
            else:
                min_val = n
                flag = True
    return min_val


def get_num_percenate(num):
    count = 0
    below = 0
    f = open(DATA_FILE_NAME, "r")
    lines = f.readlines()
    f.close()
    for line in lines:
        line = line.strip()
        nums_arr = [int(val) for val in line.split()]
        for n in nums_arr:
            count = count + 1
            if n < num:
                below = below + 1
    return below / count


def get_percentage(p):
    right = get_max_value()
    left = get_min_value()
    found = False
    while found == False:
        mid_val = (left + right) / 2
        percentage = get_num_percenate(mid_val)
        if p == percentage:
            found = True
        if p < percentage:
            right = mid_val
        else:
            left = mid_val
    return mid_val


nums_avg = calc_avg()
nums_var = calc_variance()
nums_max = get_max_value()
nums_min = get_min_value()
nums_4_percentage = get_percentage(0.4)

print("Avg: ", nums_avg)
print("Variance: ", nums_var)
print("Max: ", nums_max)
print("Min: ", nums_min)
print("0.4 Percentage: ", nums_4_percentage)
