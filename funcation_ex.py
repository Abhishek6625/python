def greater(a,b):
    if a > b :
        return a
    else:
        return b
    
# print(greater(24,43))

num1 = int(input("Enter the First Number"))
num2 = int(input("Enter the Second Number"))

bigger = greater(num1, num2)

print(f"{bigger} is Greater Number")

    