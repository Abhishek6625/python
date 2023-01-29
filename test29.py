l =[]
for a in range(1,101):
    l.append(a)
print(l)


n=[m for m in range(1,101)]
print(n)

n=[m for m in range(1,101) if m%2==0]
print(n)

n="hello"
a=[b for b in n]
print(a)