# class a:
#     def fun_a(self):
#         print('class a')
# class b(a):
#     def fun_b(self):
#         print('class b')
# class c(b):
#     def fun_c(self):
#         print('class c')
#
# obj=c()
# obj.fun_a()
# obj.fun_b()
# obj.fun_c()
# from inheritance.single_inheritance import vehicle
# from inheritance.single_inheritance import vehicle


#create 3 class vehicle,car,electric_car
#vehicle;make;model;year
#car;mum_door
#electric_car;battery_capacity

class vehicle:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def vehical_disp(self):
        print('make=',self.make)
        print('model=',self.model)
        print('year=',self.year)

class car(vehicle):
    def __init__(self,make,model,year,num_door):
        vehicle.__init__(self,make,model,year)
        self.door=num_door
    def car_disp(self):
        self.vehical_disp()
        print('number of doors=',self.door)

class electric(car):
    def __init__(self,make,model,year,num_door,battery_capacity):
        car.__init__(self,make,model,year,num_door)
        self.battery=battery_capacity
    def elc_disp(self):
        self.car_disp()
        print('battery capacity=',self.battery)

ob=electric('TATA','kiya',2022,5,2000)
ob.elc_disp()