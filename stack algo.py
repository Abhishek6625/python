import os
lst = []

while 1 :
    print("1. Insert")  # push append
    print("2. Delete")  # pop
    print("3. exit")
    print("4. Peek")  # check the upper value

    select = input("select your choice : ")

    if select == '1':
        value = input("Enter the value : ")
        lst.append(value)

    elif select == '2':
        if len(lst) == 0:
            print("list is empty")
        else:
            removedValue = lst.pop()
            print(removedValue)

    elif select == '4':
        if len(lst) == 0:
            print("list is empty")
        else:
            print(lst[-1])

    elif select == '7':
        print(lst)

    elif select == '3':
        break
    else:
        print("invalid input..")



    print(lst)
    input("Press any key to continue .....")
    os.system("cls")

