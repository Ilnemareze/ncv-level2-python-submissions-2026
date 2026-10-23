# Programmer: Mew, I
# Task2: This program adds four marks and then calculates
#        the average of the four marks.  The average will
#        have 2 decimal places.

#Input
mark1 = float(input("Mark 1:"))
mark2 = float(input("Mark 2:"))
mark3 = float(input("Mark 3:"))
mark4 = float(input("Mark 4:"))

#Processing
average = (mark1 + mark2 + mark3 + mark4)/4

#Output
print("Average:", f"{average:.2f}")