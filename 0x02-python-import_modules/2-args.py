#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    k = 0
    j = 1
    for i in argv:
        k = k + 1
    if k == 1:
        print("{} arguements.".format(k-1))
    elif k == 2:
        print("{} arguement:".format(k-1))
    else:
        print("{} arguements:".format(k-1))
    for i in argv:
        if k != 1 and i != argv[0]:
            print("{}: {}".format(j, i))
            j = j + 1
