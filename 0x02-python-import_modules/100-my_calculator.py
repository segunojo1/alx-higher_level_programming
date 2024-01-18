#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    operators = ['+', '-', '*', '/']
    if not len(sys.argv) == 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    elif len(sys.argv) == 4:
        if not sys.argv[3] in operators:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
    funcs = {"+": add, "-": sub, "*": mul, "/": div}
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    opp = sys.argv[2]
    res = funcs[opp](a, b)
