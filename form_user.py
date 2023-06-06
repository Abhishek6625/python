users = {
    'name' : 'Abhishek kumar',
    'age'  : 24,
    'fav_movies' : "3 editied",
    'fav_singer'  : "Pawan singh"

}

user = {}

name = input("What is your name :")
age = input("what is your age :")
fav_movies = input("your fav movies seprated by ,").split(',')
fav_songs = input("your fav singer separted by ,").split(',')


user['name'] = name
user['age'] = age
user['fav_movies'] = fav_movies
user['fav_song']  = fav_songs

print(user)


for key, value in user.items():
    print(f"{key} : {value}")
