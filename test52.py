import json
file = open("test.json","r")
x=file.read()
finaldata=json.loads(x)
di = dict(finaldata[0])
for  i,j in di.items():
    print( i,"-",j)