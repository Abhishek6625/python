def squre_list(a):
    squre = []
    for i in a:
        squre.append(i ** 2)
    return squre

number = list(range(1, 11))

print(squre_list(number))