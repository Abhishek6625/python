d={
    'course':'Pyhon',
    'fees':8000,
    'duration':'3 Months'

}

c=d.get('course')

print(c)

for n in d.keys():
    print(n)

for a in d.values():
    print(a)

for m,n in d.items():
    print(m,n)

del d['fees']
print(d)

d.pop('duration')
print(d)

d.update({'fees':2000})
print(d)

d.clear()
print(d)