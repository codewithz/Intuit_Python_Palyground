name="Zartab"
print(dir(name))

class Point:
    color="Red"
    def __init__(self,x,y):
        print("Point() invoked")
        self.x=x
        self.y=y

    def draw(self):
        print(f"Point({self.x},{self.y})")

    def __str__(self):
        return f"Point({self.x},{self.y})"


#---------------------------------------------------

p=Point(1,2)
print(p)

print(isinstance(p,object))




# https://rszalski.github.io/magicmethods/