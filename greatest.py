def greatest(a,b,c):
    if a > b and a > c :
        return a
    elif b > a and b > c :
        return b
    else:
        return c
    
print(greatest(100,23,54))    




def is_palindrom(word):
    reversed_word = word[::-1]
    if word == reversed_word:
        return True
    else :
        return False
    
print(is_palindrom("naman"))    
print(is_palindrom("Abhishek"))