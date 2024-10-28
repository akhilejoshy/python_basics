# class A:
#     def fun_A(self):
#         print('class A')
#
# class B(A):
#     def fun_B(self):
#         print('class B')
#
# class C(A):
#     def fun_C(self):
#         print('class C')
#
# obj1=B()
# obj1.fun_A()
# obj1.fun_B()
#
#
# obj2=C()
# obj2.fun_A()
# obj2.fun_C()


#detailL:mame,email,phone
#docter:hospital name:specialization
#engineer:cmp name,designation

class details:
    def __init__(self,name,email,phn):
        self.name=name
        self.email=email
        self.phn=phn
    def detail_disp(self):
        print('name =',self.name)
        print('email=',self.email)
        print('phone number',self.phn)

class docter(details):
    def __init__(self,name,email,phn,hospital_name,specialization):
        super().__init__(name,email,phn)
        self.hos_name=hospital_name
        self.spc=specialization

    def doter_disp(self):
        self.detail_disp()
        print('hospital name=',self.hos_name)
        print('specialization=',self.spc)

class engineer(details):
    def __init__(self,name,email,phn,conpany_name,designation):
        super().__init__(name,email,phn)
        self.conpany_name = conpany_name
        self.desig=designation
    def eng_disp(self):
        self.detail_disp()
        print('company name=',self.conpany_name)
        print('designation=',self.desig)


docr=docter('akhil','akhil@gmail.com',9048300196,'MCM Hospital','Eye')
eng=engineer('akhil','akhil@gmail.com',9048300196,'TCS','Manager')



docr.doter_disp()
print()
eng.eng_disp()