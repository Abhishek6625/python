class DemoClass:
    a=10
    def showvalue(self):
        self.c=self.a*self.a
        print(self.c)
    def showvalue1(self):
        print("I am Programer")
    def showvalue2(self,a,b):
        print(a+b)

obj=DemoClass()
obj.showvalue()
obj.showvalue1()
obj.showvalue2(20,30)