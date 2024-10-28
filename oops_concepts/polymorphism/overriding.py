class A:
    def fun_A(self):
        print('hello welcome to python')

class B(A):
    def fun_A(self):
        print('hello welcome to javascript')

obj=B()
obj.fun_A()



#Q  1, create a parent class shapes with a fun area() that returns 0
#   2, create a child class rectangle that passes two values length and width with fun area()
#   3, create a child class circle that passes radius with the fun area()

class shapes:
    def area(self):
        return 0

class rectangle(shapes):
    def __init__(self,length,width):
        self.leng=length
        self.wid=width
    def area(self):
        return self.leng*self.wid

class circle(shapes):
    def __init__(self,radius):
        self.r=radius
    def area(self):
        return 3.14*self.r**2


obj1=shapes()
print(obj1.area())

obj2=rectangle(4,2)
print(obj2.area())

obj3=circle(2)
print(obj3.area())