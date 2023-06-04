def common_find(l1, l2):
    output = []
    for i in l1:
        if i in l2:
            output.append(i)
    return output 

print(common_find([1,2,3,4,5], [1,3,5,6,2]))    
