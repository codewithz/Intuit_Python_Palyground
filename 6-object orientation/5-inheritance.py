class Animal:
    def eat(self):
        print("EAT")
# ----------------------------------------------------------------

#  Animal : Parent or Base Class
#  Mammal , Fish : Child Class or Derived Class

# class Child(Parent):

# -----------------------------------------------------------------

class Mammal(Animal):

    def walk(self):
        print("WALK")

# ------------------------------------

class Fish(Animal):

    def swim(self):
        print("SWIM")

# ---------------- DRY - Don't Repeat Yourself --------------------------

m=Mammal()
m.eat()
m.walk()

print("-----------------------------------------")
f=Fish()
f.eat()
f.swim()