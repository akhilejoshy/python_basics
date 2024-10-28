# class base:
#     def fun_base(self):
#         print('class base')
#
# class A(base):
#     def fun_A(self):
#         print('class A')
#
# class B(base):
#     def fun_B(self):
#         print('class B')
#
# class C(A,B):
#     def fun_C(self):
#         print('class C')
#
# obj=C()
# obj.fun_base()
# obj.fun_A()
# obj.fun_B()
# obj.fun_C()


#univercity:  uni name,loc
#ug program:  name of ug student,ug course
#pg program:  name of pg students,pg projects
#program_diracter:  directer name


class uni:
    def __init__(self,uni_name,loc):
        self.uni=uni_name
        self.loc=loc
    def uni_disp(self):
        print('University name=',self.uni)
        print('university loc=',self.loc)

class ug_prg(uni):
    def __init__(self,uni_name,loc,ug_student_name,ug_course):
        uni.__init__(self,uni_name,loc)
        self.ugname=ug_student_name
        self.course=ug_course
    def ug_disp(self):
        self.uni_disp()
        print('ug student name=',self.ugname)
        print('ug course=',self.course)

class pg_program(uni):
    def __init__(self,uni_name,loc,pg_student_name,pg_project):
        uni.__init__(self,uni_name,loc)
        self.pgname=pg_student_name
        self.project=pg_project
    def pg_disp(self):
        self.uni_disp()
        print('pg student name=',self.pgname)
        print('pg project=',self.project)

class program_dircter(ug_prg,pg_program):
    def __init__(self,uni_name,loc,ug_student_name,ug_course,pg_student_name,pg_project,directer_name):
        ug_prg.__init__(self,uni_name,loc,ug_student_name,ug_course)
        pg_program.__init__(self,uni_name,loc,pg_student_name,pg_project)
        self.dir=directer_name
    def dir_disp(self):
        self.ug_disp()
        self.pg_disp()
        print('directer name=',self.dir)


direct=program_dircter('ktu','tvm','akhil','cse','chepu','chepara cave','cj')
direct.dir_disp()