class Student:
    def __init__(self):
        self.name="harry"
    def getname(self):
        return self.name
    def __set_name__(self, name):
        self.name=name

object=Student()
# object.__set_name__("Abhishek")
name=object.getname()
print(object.name)