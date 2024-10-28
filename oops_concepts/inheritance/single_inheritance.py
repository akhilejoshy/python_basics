# # syntax
# from collections.abc import async_generator
#
#
# class A:#parent class or base class
#     def funA(self):
#         print('class A')
#
# class B(A):#child class or derived class
#     def funB(self):
#         print('class B')
#
# #obj create for child class
# obj=B()
# obj.funA()
# obj.funB()

#Q create a class person

#1,person details(name,age)
#2,person_display()/should print the person name and async_generator

# create a class student that inherits person class
#1,student_details(roll number,department,email id)
#2,student display(name,age,roll number,deppartment,email)

# class person:
#     def person_details(self,name,age):
#         self.name=name
#         self.age=age
#     def person_display(self):
#         print('name= ',self.name)
#         print('age= ',self.age)
#
# class student(person):
#     def student_details(self,roll_num,dep,email):
#         self.roll=roll_num
#         self.dep=dep
#         self.email=email
#     def student_display(self):
#         self.person_display()
#         print('roll number= ',self.roll)
#         print('department= ',self.dep)
#         print('E-mail= ',self.email)
#
# objA=student()
# objA.person_details('akhil',22)
# objA.student_details(127,'CSE','akhil@gmail.com')
# objA.student_display()

#Q create a parent class vehicle
#1 vehicle_detail(make,model,year)
#2,display_info()
# create a childe class car should inherit vehicle
#1 addi_inf(no_of_door,fuel_type)
#2,complete detaile()

# class vehicle:
#     def vehicle_details(self,make,mode,year):
#         self.mk=make
#         self.mo=mode
#         self.yr=year
#     def display_info(self):
#         print('make = ',self.mk)
#         print('model = ',self.mo)
#         print('year = ',self.yr)
#
# class car(vehicle):
#     def addi_info(self,no_of_door,fuel_type):
#         self.no=no_of_door
#         self.fu=fuel_type
#     def complite_details(self):
#         self.display_info()
#         print('no of door = ',self.no)
#         print('fuel type = ',self.fu)
#
# cars=car()
# cars.vehicle_details('toyota','inova',2011)
# cars.addi_info(5,'diesel')
# cars.complite_details()


# class persion:
#     def __init__(self,name,age):
#         self.n=name
#         self.a=age
#     def persion_detail(self):
#         print('name=',self.n)
#         print('age=',self.a)
#
# class student(persion):
#     def __init__(self,name,age,roll_num,dep,email):
#         super().__init__(name,age)
#         self.ro=roll_num
#         self.dp=dep
#         self.em=email
#     def student_display(self):
#         self.persion_detail()
#         print('roll number=',self.ro)
#         print('department=',self.dp)
#         print('email=',self.em)
# stu=student('akhil', 22,127,'cse','ak@.com')
# stu.student_display()



