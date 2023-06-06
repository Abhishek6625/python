# d = {'name' : 'unkown', 'age' : 'unkown'}

d = dict.fromkeys(('name','age','hight'), 'unkown')
print(d)

ran = dict.fromkeys(range(1, 11), 'unkown')

print(ran)


d = {'name' : 'unkown', 'age' : 'unkown'}
print(d['name'])
print(d.get('age'))


if 'name' in d:
    print('present')
else:
    print("not present")

# d.clear()   
print(d)



d1 = d.copy()
print(d1)

print(d1 is d)