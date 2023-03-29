class Area:
    def find_area(self,x=None,y=None):

        if x!=None and y!=None:
            print(x*y)
        elif x!=None:
            print(x*x)
        else:
            print("Nothing")



object=Area()
object.find_area()
object.find_area(10)
object.find_area(10,20)