from gettext import install


# class maths:
#     def add(self,a,b):
#         print(a+b)
#
#     def add(self,a,b,c):
#         print(a+b+c)
#
# obj=maths()

#--> u can achive method overloding directly but using multiple dispach we can method overloding
#       multipledipach is external package

# pip install multipledispch

from multipledispatch import dispatch
# class maths:
#     @dispatch(int,int)
#     def add(self,a,b):
#         print(a+b)
#     @dispatch(int,int,int)
#     def add(self,a,b,c):
#         print(a+b+c)
#
# obj=maths()
# obj.add(1,2)
# obj.add(1,2,3)


# class datatype_length:
#     @dispatch(str)
#     def length(self,a,count=0):
#         self.a=a
#         for i in a:
#             count+=1
#         self.c = count
#         print(self.c)
#
#     @dispatch(list)
#     def length(self,a,count=0):
#         self.a=a
#         for i in a:
#             count+=1
#         self.c = count
#         print(self.c)
#
#     @dispatch(tuple)
#     def length(self,a,count=0):
#         self.a=a
#         for i in a:
#             count+=1
#         self.c = count
#         print(self.c)
#
#     @dispatch(set)
#     def length(self,a,count=0):
#         self.a=a
#         for i in a:
#             count+=1
#         self.c = count
#         print(self.c)
#
#     @dispatch(dict)
#     def length(self,a,count=0):
#         self.a=a
#         for i in a:
#             count+=1
#         self.c = count
#         print(self.c)
#
#
# obj=datatype_length()0
# obj.length([23,76,766])






