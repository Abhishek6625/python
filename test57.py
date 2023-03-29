class Student:
    __name="Abhishek"
    def __init__(self):
        print(self.__name)
        self.__displayinfo()
    def __displayinfo(self):
        print("Abhishek pandit")


object=Student()