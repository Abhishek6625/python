import sys

my_list = sys.argv
# print(my_list)
print('file name is :',my_list[0])


for file in my_list:
    print(file)


arg_list = sys.argv

if arg_list[1] in arg_list[2]:
    print('found')

else :
    print('not found')    
