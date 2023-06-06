
user_info = {
    'name' : 'Abhishek kumar',
    'age'  : 24,
    'fav_movies' : "3 editied",
    'fav_singer'  : "Pawan singh"

}


if 'name' in user_info:
# if 'Abhsihek' in user_info.values():
    print('present')

else:
    print('not present')





for i in user_info :
    print(i)    
for i in user_info.values():
    print(i)





user_info_value = user_info.values()
print(user_info)
print(type(user_info))


for i in user_info:
    print(user_info[i])




user_items = user_info.items()
print(user_info)
print(type(user_items))




for i, value in user_info.items():
    print(f"key us {i} and vlaue us {value} ")
    print(i)