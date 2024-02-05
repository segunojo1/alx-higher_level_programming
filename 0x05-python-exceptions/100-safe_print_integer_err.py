#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except TypeError as e:
        sys.stderr.write("Exception: {}".format(str(e)))
    except ValueError as e:
        sys.stderr.write("Exception: {}".format(str(e)))
