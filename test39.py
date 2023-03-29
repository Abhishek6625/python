# Function

def simplefunction():
    print("Hello wolrd")


simplefunction()


def sum(a, b):
    print(a + b)


sum(20, 10)
sum(30, 56)

def sum(a,b=2):
    print(a+b)
sum(20)

sum(12, 30)


def square(x):
    return x * x + 2 * x


s = square(5)
print(s)
