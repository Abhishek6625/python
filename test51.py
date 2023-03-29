import json
d='{"corse_name":"python","fees":12000,"duration":"2 Months"}'
x=json.loads(d)
print(x)
print(type(x))
for a in x:
    print(a,x[a])