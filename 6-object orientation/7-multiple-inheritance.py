class Employee:
    def greet(self):
        print("Employee Greet")

class Person:
    def greet(self):
        print("Person Greet")

class Manager(Employee,Person):
    pass


m=Manager()
m.greet()

# -----------------------------------------------

class Flyer:
    def fly(self):
        print("FLY")

class Swimmer:
    def swim(self):
        print("SWIM")

class FlyingFish(Swimmer,Flyer):
    pass

ff=FlyingFish()
ff.swim()
ff.fly()