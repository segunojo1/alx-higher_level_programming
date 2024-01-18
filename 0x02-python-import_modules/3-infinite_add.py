#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argg = 0
    for i in range(1, len(sys.argv)):
        argg += int(sys.argv[i])
    print("{}".format(argg))
