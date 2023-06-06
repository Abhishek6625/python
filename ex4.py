def reverse_string(l):
    return [name[::-1] for name in l]

print(reverse_string(['abc','tuv','xyz']))




def revese_str(l):
    new_list = []
    for name in l:
        new_list.append(name[::-1])
        return new_list
    
print(revese_str(['abc','tuv','xyz']))    