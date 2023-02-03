# Dictionary

course={
    'php':{'duration':'3 Months','fees':15000},
    'java':{'duration':'2 Months','fees':12000},
     'html':{'duration':'4 Months','fees':20000},

}
print(course)
print(course['java'])
print(course['java'],['fees'])

for a,b in course.items():
    print(a,b)

    print(a,b['duration'],b['fees'])