#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    new_list = []
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
   # for i in range(0, my_list):
    #    if i == idx:
    #del my_list[
    del my_list[idx]
    return my_list
