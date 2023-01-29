# list add lists.....

a=[10,20,30,46,57]
a1=[3,4,5,30,43]

t=len(a)

for m,n in zip(a,a1):
    print(m,n)

for h in range(t):
    print(h)
    print(a[h],a1[h])