#stacks
l= []
while True:
    print("""1 push Elements
2 pop Elements
3 peek Element
4 Display stack
5 exit""")
    c=int(input("Enter number to select : "))
    if c==1:
        n=input("Enter The value:-");
        l.append(n)
        print(l)
    elif c==2:
        if len(l)==0:
            print("Empty stack")
        else:
            p=l.pop()
            print(p)
            print(l)
    elif c==3:
        if len (l)==0:
            print("Empty Stack")
        else:
            print("last stack value:-",l[-1])
    elif c==4:
        print("Display stack",l)
    elif c==5:
        break;
    else:
        print("Invalid opr...")