ex = [[1,2,3],[1,2,3],[1,2,3]]

nested = [[i for i in range(1,4) ] for j in range(3)]

print(nested)



square = {num : num ** 2 for num in range (1, 11)}
print(square)

for a, b in square.items():
    print(f" square of {a} is : {b}")


string = "Abhishek"
word_count = {char:string.count(char) for char in string} 
print(word_count)





odd_even = {i : ('even' if i%2 == 0 else 'odd') for i in range (1, 11)}
print(odd_even)






for i in range(1,11):
    if i%2 == 0:
        print(f"{i} : even")
    else :
        print(f"{i} : odd")    

