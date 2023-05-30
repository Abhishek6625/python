lang = "python"

print(lang[2])

print(lang[0 : 4])

print(lang[2:6])

print(lang[-3:4])
print(lang[-2:])


print("Abhishek"[0:5])

print("Abhishek"[0:6:2])

print("Abhishek"[0::2])

print("Abhishek"[::6])

print("Abhishek"[6::-1])


print("Abhishek"[-1::-1])

print("Abhishek"[::-1])


name = input("Enter the name ")
reverse= name[-1::-1]

# print(reverse)

# print(f"reverse of your name is {reverse}")

print(f"reverse of your name is {name[-1::-1]}")
