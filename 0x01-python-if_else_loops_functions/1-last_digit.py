#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
string_number = str(number)
last_digit = int(string_number[-1:])
print("The last digit of {} is {}".format(number, last_digit), end=" ")
if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
elif last_digit < 6:
    print("and is less than 6 and not 0")
