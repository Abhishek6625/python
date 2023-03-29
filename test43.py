#random module
import random
n=random.randint(2,8)
print(n)

n1=random.randrange(2,8)
print(n1)

l=[10,20,30,40]
n2=random.choice(l)
print(n2)

r=random.random()
print(r)

l1=[10,30,50,40]
random.shuffle(l1)
print(l1)

u=random.uniform(3,9)
print(u)