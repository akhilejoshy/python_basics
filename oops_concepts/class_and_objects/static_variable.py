#Q create a class company with 2 static variables company name and loc
#method 1/employee details/id/name/designation/salary
#method2/ employee display/company name/compny loc/emp name/ id/designation/salary

# class tcs:
#     company_name='TCS'
#     company_loc='Kakkand'
#     def employee_details(self,id,name,designation,salary):
#         self.i=id
#         self.n=name
#         self.d=designation
#         self.s=salary
#
#     def employee_display(self):
#         print('company name=',self.company_name)
#         print('company loc=',self.company_loc)
#         print('employee ID=',self.i)
#         print('employee name=',self.n)
#         print('designationn=',self.d)
#         print('salary=',self.s)
#
# obj1=tcs()
# obj1.employee_details(127,'akhil','manager',2000)
#
# obj1.employee_display()

#Q bank

class sbi:
    bank_name='sbi'
    bank_branch='tsr'
    def accnt_info(self,ac_num,ac_holder,balance=0):
        self.num=ac_num
        self.holder=ac_holder
        self.b=balance

    def deposit(self,amount):
        self.b+=amount

    def withdrow(self,amount):
        if(self.b>=amount):
            self.b-=amount
        else:
            print('insufisent balance')
    def acc_info(self):
        print('bank name=',self.bank_name)
        print('branch=',self.bank_branch)
        print('account number=',self.num)
        print('account holder=',self.holder)
        print('balance=',self.b)
    def check_b(self):
            print('curreāānt balance=',self.b)
a=sbi()
a.accnt_info(123,'akhil')

a.deposit(1500)
a.withdrow(200)
a.acc_info()
a.check_b()

