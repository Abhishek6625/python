user_info = {
    'name' : 'Abhishek kumar',
    'age'  : 24,
    'fav_movies' : "3 editied",
    'fav_singer'  : "Pawan singh"

}

user_info['fav_movies'] = ['song1','song2']
print(user_info)


popted = user_info.pop('fav_movies')
print(f"popped item is {popted}")
print(user_info)



popped_item = user_info.popitem()
print(user_info)
print(type(popped_item))