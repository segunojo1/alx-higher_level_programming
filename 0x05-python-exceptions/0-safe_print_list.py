#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    nums = 0
    for i in range(0, x):
        try:
            print("{}".format(my_list[i]), end="")
            nums += 1
        except IndexError:
            break
    print("\n")
    return count 

# safe_print_list([1,2,3,4,5], 3)
