#Programmer: Mew,I

mark = 120

if mark >= 0 and mark <= 100:
    print("Valid mark")
else:
    print("Invalid mark")

if mark < 0 and mark > 100:
    print("Invalid mark")

#if, if_else, nested if
#if
mark = 45

if mark >= 45:
    print("Competent")
print("Completed")

# if, if_else, nested if
# if_else
mark = 45

if mark >= 50:
    print("Competent")
else:
    print("Not yet competent")
    
# if, if_else, nested if
# nested if
mark = 75

if mark >= 0 and mark <= 100:
    if mark >= 50:
        print("Competent")
    else:
        print("Not yet competent")
else:
    print("Invalid")