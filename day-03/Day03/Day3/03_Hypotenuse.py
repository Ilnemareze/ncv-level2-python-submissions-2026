# Programmer: Mew, I
# Task1: The program inports the math functions.  Two inputs must be supplyed.
#        The power of both numbers are calculated, then the answers of the two
#        numbers are added together and the square root is then calculated on
#        the answer.  The answer will have 2 decimal places and an unit of
#        measurement.  Otherwise if the two numbers are both zero the user will
#        get an error message.

import math

# Input
side_a = float(input("Enter a:"))
side_b = float(input("Enter b:"))

# Processing and output
if side_a > 0 and side_b > 0:
    side_c = math.sqrt((math.pow(side_a, 2)) + (math.pow(side_b, 2)))
    print(f"Side: {side_c:.2f} square meters")
else:
    print("I can not calculate with zero!")
   