# number guessing random module
import random
a=random.randrange(1,101)
b=int(input("Enter your nomber:-----"))
if b > a:
    print("computer Number",a)
    print("your guess number is too high")
elif a > b:
    print("computer Number",a)
    print("Your guess number is too low")
else:
    print("Computer number",a)
    print("Your guess Number is equal")

