# Programmer: Mew, I
# Task: This is my first Python program
#        Recieves 2 inputs.
#        Deterrmine the common HCF.
#        Output a sentance with the answer.

# Input
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

# Processing
if num1 < num2:
    factor = num1
else:
    factor = num2
    
while num1 % factor != 0 or num2 % factor != 0:
    factor = factor - 1
    
# Output
print("The highest common factor is ",factor)