from abc import ABC,abstractmethod


class shapes(ABC): # here ABC is the base class where rhe content is hidden
    @abstractmethod # it is decorater
    def area(self):
        pass # it is use for empty fun

    @abstractmethod
    def perimeter(self):
        pass

class rectangle(shapes):
    def __init__(self,lenh,wid):
        self.leng=lenh
        self.wid=wid
    def area(self):
        return self.wid*self.leng

    def perimeter(self):
        return 2*(self.leng+self.wid)

class circle(shapes):
    def __init__(self,radius):
        self.r=radius
    def area(self):
        return 3.14*self.r**2
    def perimeter(self):
        return 2*3.14*self.r

obj1=rectangle(2,3)
print(obj1.area())
print(obj1.perimeter())

obj2=circle(6)
print(obj2.area())
print(obj2.perimeter())



