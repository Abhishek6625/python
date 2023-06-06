def num_too (l):
    return [str(i) for i in l if (type(i) == int or type(i) == float)]

print(num_too([True, False, [1,2,4],2,1.0,4]))




nums = [1,2,3,4,5,6,7,8,9,10]
new_list = []
for i in nums:
    if i%2 ==0:
        new_list.append(i*2)
    else:
        new_list.append(-i)

print(new_list)      



new_list2 = [i*2 if (i%2 ==0) else -i for i in nums]
print(new_list2)

