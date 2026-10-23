#Programmer: Mew, I

marks = []
mark = int(input("Enter mark (or -1 to stop):"))

while mark != -1:
    marks.append(mark)
    mark = int(input("Enter mark (or -1 to stop):"))
    
print(f"Our list has {len(marks)} elements")

sum = 0
for x in range(len(marks)):
    mark = (marks[x])
    sum = sum + mark
    
print(f"The sum of all marks = {sum}")

total = 0
for x in range(len(marks)):
    mark = (marks[x])
    total = total + mark

average = total / len(marks)
print(f"The average = {average:.0f}%")