
d = {'a' :1, 'b' : 2, 'a' : 2}

print(d)
print(type(d))



def word_counter(s):
    count = {}
    for char in s:
        count[char] = s.count(char)
    return count

print(word_counter('Abhishek'))    
