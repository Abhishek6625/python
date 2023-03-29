#dates
import datetime
x=datetime.datetime.now()


print(x)

x=datetime.datetime(2023,2,5)
print(x)

x=datetime.datetime.now()
m=x.strftime("%I")

print(m)