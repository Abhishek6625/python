sum = 0
num = input("Enter a number :")
for i in range(0, len(num)):
   sum += int(num[i])

print(sum)   






name = input("Enter the name : ")
temp = ""
for i in range(0, len(name)):
   if name[i] not in temp:
      print(f"{name[i]} : {name.count(name[i])}")
      temp += name[i]
    