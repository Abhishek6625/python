# tuple
t=(20,30,40,50,80,20)
a=t[2]
print(a)

b=len(t)
print(b)

for a in t:
    print(a)
    #or
for q in range(1):
    print(t[q])
#min
m=min(t)

print(m)

n=max(t)
print(n)

x=t.count(20)
print(x)

y=t.index(50)
print(y)

s=sum(t)
print(s)
v=sum(t,90)
print(v)
