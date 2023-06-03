num = list(range(1,11))

print(num)

p = num.index(2)
print(p)



number =[1, 2, 3, 4, 5, 6, 7, 8]

# print(number.index(1, 4, 5))
def negative_list(l):
    negative = []
    for i in l:
        negative.append(-i)
    return  negative

print(negative_list(number))  

