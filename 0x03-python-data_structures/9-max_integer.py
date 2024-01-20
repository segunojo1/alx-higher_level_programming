#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    max_num = my_list[0]
    for i in my_list:
        for j in my_list:
            if i > j and i > max_num:
                max_num = i
    return max_num

my_list = [-23, -104, -5, -13, -93]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))
