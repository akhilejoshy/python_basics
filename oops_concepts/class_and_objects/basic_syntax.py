# class class_name:
#     #body of class



class first:
    def hello(self):
        print('welcome to oops')

x=first()
x.hello()

#Q create a class calculater with 4 functions add, sub, mull, div that passes two varible


class calculater:
    def add(self,a,b):
        print(a+b)

    def sub(self,a,b):
        print(a-b)

    def mull(self,a,b):
        print(a*b)

    def div(self,a,b):
        print(a/b)

ans=calculater()
ans.add(1,2)
ans.sub(5,4)
ans.mull(2,4)
ans.div(5,2)