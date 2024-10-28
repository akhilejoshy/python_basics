# class Encapsulation:
#     def __init__(self,name,addr,phn):
#         self.name=name #public data
#         self._addr=addr #protected
#         self.__phn=phn #privete
#
#     def __en_disp(self):
#         print(self.name)

#--> public

# class persion:
#     def __init__(self,name,email):
#         self.name=name
#         self.email=email
#
#     def persion_disp(self):
#         print(self.name)
#         print(self.email)
#
# pers=persion('akhil','a@gmail.com')
#
# pers.persion_disp()
#
# pers.name='abhi'
# pers.email='hii@gmail'
#
# pers.persion_disp()

#--> private
# class persion:
#     def __init__(self,name,email):
#         self.__name=name
#         self.__email=email
#
#     def __persion_disp(self):
#         print(self.__name)
#         print(self.__email)
#
# # print(obj.name)
# # obj.persion_disp()
#
# #--> it is the method of giving access to privte datamembers and methods inside a class
# #   _classname__datamember
#
# print(obj._persion__name)
# print(obj._persion__email)
#
# obj._persion__name='appu'
# print(obj._persion__name)
#
# obj._persion__persion_disp()
# obj=persion('akhil','@gmail')

#--> protected
class persion:
    def __init__(self,name,email):
        self._name=name
        self._email=email

    def _persion_disp(self):
        print(self._name)
        print(self._email)

obj=persion('akhil','@gmail')
print(obj._name)
print(obj._email)
obj._name='appu'
obj._email='hii'
obj._persion_disp()