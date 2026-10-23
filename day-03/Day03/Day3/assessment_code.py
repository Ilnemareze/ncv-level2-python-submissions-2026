# 7409070054081

# Input
mark1 = int(input("Enter the first mark:"))
mark2 = int(input("Enter the second mark:"))

# Processing
average = (mark1 + mark2)/ 2

# Selection and output
print(f"{average:.2f} mark.")

if average >= 50:
    print("Examination admission GRANTED.")
else:
    print("Examination admission DENIED.")
