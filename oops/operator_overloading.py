'''
class Overloading:
    def __init__(self,x,y):
        self.x = x
        self.y = y


obj = Overloading(10,20)
obj1 = Overloading(20,30)

print(obj + obj1)
'''

class Overloading:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self, other):
        self.other = other

        print(self.x + other.x)
        print(self.y + other.y)

obj = Overloading(10,20)
obj1 = Overloading(20,30)

print(obj + obj1)