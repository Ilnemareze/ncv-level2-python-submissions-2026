# Programmer: Mew, I
# Task1: This program takes 2 inputs, lenght and width.
#        It calculates the area using the 2 inputs and area
#        formulae.  The output will consist of 2 decimal
#        places and the unit of measurement.

# Input
length = float(input("Length:"))
width = float(input("Width:"))

# Processing
area = (length * width)

#Output
print("Area:", f"{area:.2f}", "square meters")