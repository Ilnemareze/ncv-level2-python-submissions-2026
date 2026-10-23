#Programmer: Mew, I

mark =int(input("Enter the mark:"))
print(mark)

if mark < 0 or mark > 100:
    print("Out of bounds")
elif mark >= 80 and mark <= 100:
    print("Pass with destinction, outstanding!")
elif mark >= 50 and mark <= 74:
    print("Pass, well done.")
else:
    print("Fail, see you next year.")


    