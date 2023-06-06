import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(200)
print(sys.getrecursionlimit())


i = 0
def demo():
    global i
    i += 1
    print("hello world", i)
    demo()

demo()

