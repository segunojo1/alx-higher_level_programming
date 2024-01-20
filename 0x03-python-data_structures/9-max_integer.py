#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return "None"
    max_num = 0
    for i in my_list:
        for j in my_list:
            if i > j and i > max_num:
                max_num = i
    return max_num
