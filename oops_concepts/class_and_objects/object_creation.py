class person:
    def create_persion(self,name,age,gender):
        self.n=name
        self.age=age
        self.gender=gender

    def display_persion(self):
        print('name=',self.n)
        print('age=',self.age)
        print('gender=',self.gender)

obj1=person()
obj1.create_persion('akhil',22,'male')

obj2=person()
obj2.create_persion('mannu',21,'male')

obj1.display_persion()
obj2.display_persion()