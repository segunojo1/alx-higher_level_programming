#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in my_list:
            if i <= x:
	        print(i)
    except:
        print("Error")

# safe_print_list([1,2,3,4,5], 6)
