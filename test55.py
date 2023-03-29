class A:
    def displayA(self):
        print("I am Abhishek A")
class B(A):
    def displayB(self):
        print("I am Abhishek B")

class C(B):
    def displayC(self):
        print("I am Abhishek C")

object=C()
object.displayA()
object.displayB()
object.displayC()