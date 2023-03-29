class A:
    def showData(self):
        print("i m in A class")

class B(A):
    def showData(self):
        print("i m in B class")


object=B()
object.showData()