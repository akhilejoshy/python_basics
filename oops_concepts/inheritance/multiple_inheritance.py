# class a:
#     def fun_a(self):
#         print('class a')
#
# class b:
#     def fun_b(self):
#         print('class b')
#
# class c(a,b):
#     def fun_c(self):
#         print('class c')
#
# obj=c()
# obj.fun_a()
# obj.fun_b()
# obj.fun_c()

# school-->parent1
#school_details:school_name,loc
#school_display

#parent-->parent2
#parant_details:parent name,addr
#parent_display

#student-->child
#sttudent_detail:rool num,name,dept
#student disp()

#view complete detail():school,loc,parant name,addr,roll,name,dept

# class school:
#     def school_details(self,school_name,loc):
#         self.sc=school_name
#         self.lo=loc
#     def school_disp(self):
#         print('school name=',self.sc)
#         print('loc=',self.lo)
# class parent:
#     def parent_details(self,pname,addr):
#         self.pname=pname
#         self.addr=addr
#     def parent_disp(self):
#         print('parent name=',self.pname)
#         print('parent addr=',self.addr)
#
# class student(school,parent):
#     def student_details(self,roll_num,name,dept):
#         self.r=roll_num
#         self.name=name
#         self.dept=dept
#     def student_disp(self):
#         print('name=',self.name)
#         print('roll num=',self.r)
#         print('dept=',self.dept)
#     def view_full_detail(self):
#         self.school_disp()
#         self.parent_disp()
#         self.student_disp()
#
# stu=student()
# stu.school_details('luminar','kakkand')
# stu.parent_details('joshy','thrissur')
# stu.student_details(12,'akhil','python')
# # stu.student_disp()
# stu.view_full_detail()

# ## using constructor
# class A:
#     def __init__(self,a,b):
#
# class B:
#     def __init__(self,c,d):
#
# class C(A,B):
#     def __init__(self,a,b,c,d,e,f):
#         A.__init__(self,a,b)
#         B.__init__(self,c,d)
#
# obj=C(1,2,3,4,5,6)


#company:cmpy name,loc
#team leader:leader name,dept
#worker:emp name,designation,salary

class cmpny:
    def __init__(self,company_name,location):
        self.na=company_name
        self.loc=location
    def comp_disp(self):
        print('company name = ',self.na)
        print('company location = ',self.loc)
class team_leader:
    def __init__(self,leader_name,dept):
        self.leader_name=leader_name
        self.dept=dept
    def team_leader_disp(self):
        print('team leader name = ',self.leader_name)
        print('department = ',self.dept)

class worker(cmpny,team_leader):
    def __init__(self,company_name,location,leader_name,dept,emp_name,designation,salary):
        cmpny.__init__(self,company_name,location)
        team_leader.__init__(self,leader_name,dept)
        self.emp_name=emp_name
        self.desi=designation
        self.sal=salary
    def worker_disp(self):
        self.comp_disp()
        self.team_leader_disp()
        print('employe name = ',self.emp_name)
        print('designation = ',self.desi)
        print('salary = ',self.sal)

work=worker('tcs','kakkand','amal','testing','alax','tester',30000)
work.worker_disp()