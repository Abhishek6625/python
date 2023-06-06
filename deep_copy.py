import copy 


my_list = [10,20,30,40,50]
# new_list = my_list
new_list = copy.copy(my_list)

print(new_list)
print("-"*50)
print('Id of newlist :',id(my_list[0]))
print('Id of secondlist :',id(my_list[1]))
print('Id of thirdlist :',id(my_list[2]))
print('Id of fourthlist :',id(my_list[3]))
print('Id of fivethlist :',id(my_list[4]))

print("-"*50)

new_list[1] = 600
# new_list[1] = 'Abhi'
print(my_list)
print(new_list)



