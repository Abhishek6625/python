user = {'name' : 'Abhishek','age' : 24}
print(user.get('name'))


def cube_finder(n):
    cubes = {}
    for i in range(1, n+1):
        cubes[i]= i**3
    return cubes
    
print(cube_finder(10))
