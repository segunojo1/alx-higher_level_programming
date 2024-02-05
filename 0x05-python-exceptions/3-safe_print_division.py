#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        division = a / b
    except (ZeroDivisionError, TypeError, ValueError):
        division = None
        return division
    finally:
        print("Inside result: {}".format(divison))
        return divison
