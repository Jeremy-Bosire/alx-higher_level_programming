#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
string_number = str(number)
last_digit = int(string_number[-1:])
print("Last digit of {} is".format(number), end=" ")
if number >= 0:
    if last_digit > 5:
        print("{} and is greater than 5".format(last_digit))
    elif last_digit == 0:
        print("{} and is 0".format(last_digit))
    elif last_digit < 6:
        print("{} and is less than 6 and not 0".format(last_digit))
elif number < 0:
    last_digit = "-" + str(last_digit)
    last_digit = int(last_digit)
    if last_digit == 0:
        print("{} and is 0".format(last_digit))
    elif last_digit < 6:
        print("{} and is less than 6 and not 0".format(last_digit))
