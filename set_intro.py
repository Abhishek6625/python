s = {1,2,3,2}
print(s)
print(type(s))


l = [1,2,3,4,5,6,5,4,5,3,5,6,1,3]

s2 = set(l)
# s2 = list(set(l))
print(s2)


s.add(7)
print(s)


s.remove(2)
print(s)

s.discard(5)
print(s)

s.clear()
print(s)