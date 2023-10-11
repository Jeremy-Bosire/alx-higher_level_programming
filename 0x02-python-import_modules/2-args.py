#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    j = 1
    k = len(argv)
    if k == 1:
        print("{} arguments.".format(k-1))
    elif k == 2:
        print("{} argument:".format(k-1))
    else:
        print("{} arguments:".format(k-1))
    for i in argv:
        if k != 1 and i != argv[0]:
            print("{}: {}".format(j, i))
            j = j + 1
