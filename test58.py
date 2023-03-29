class Ws:
    def displaynfo(self,name=''):
        print("Hellow world"+name)


object=Ws()
object.displaynfo()
object.displaynfo("python")


class ws:
    def displaynfo(self):
        print("Hellow world")

class IIP(ws):
    def displaynfo(self):
        super().displaynfo()
        print("I am Progremer")

object=IIP()
object.displaynfo()


