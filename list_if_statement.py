number = list(range(1, 11))

nums = []
for i in number:
    if  i % 2 == 0:
        nums.append(i)
print(nums)     





event_nums =[i for i in number if i%2 ==0]
print(event_nums)


odd_nums = [i for i in number if i%2 != 0]
print(odd_nums)