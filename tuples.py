example = ('one', 'two', 'three')

print(example[:2])




mixed = (1,2,3,4.0)
for i in mixed:
    print(i)
    
print(type(mixed))
print(sum(mixed))
print(min(mixed))



name = 'Abhishek','ram', 'Rohit', 'ganesh'

name1, name2, name3, name4 = (name)
# print(type(name))
print(name)



n = ('ram', ['Rohit','ganesh'])
n[1].pop()
n[1].append("Abhishek")
print(n)
