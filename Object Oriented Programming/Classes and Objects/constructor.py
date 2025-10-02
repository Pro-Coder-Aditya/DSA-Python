# method is call with object
class DemoClass:
    x = 10
    def showValue(self):
        self.z = self.x + self.x
        print(self.z)

    def showValue1(self):
        print("Hello")

    def showValue2(self, a, b):
        print(a + b)

obj = DemoClass()
obj.showValue()
obj.showValue1()
obj.showValue2(20, 30)

print()

# constructor(method) gets call automatically

class Demo:

    def __init__(self):
        print("Hello this is Aditya")

obj = Demo() 