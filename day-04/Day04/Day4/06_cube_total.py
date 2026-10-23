# Programmer: Mew, I

total = 0

n = int(input("Enter number:"))
        
for x in range(1, n+1):
    cube_root = x ** 3
    print(cube_root, end = " ")
    total = total + cube_root
print(total)
   