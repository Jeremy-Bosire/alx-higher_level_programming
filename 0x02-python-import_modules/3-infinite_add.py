#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    k = 0
    sum = 0
    for i in argv:
        if i == argv[0]:
            continue
        k = int(i)
        sum = sum + k
    print(sum)
