class Point:
    color="Red"
    def __init__(self,x,y):
        print("Point() invoked")
        self.x=x
        self.y=y

    def draw(self):
        print(f"Point({self.x},{self.y})")

#---------------------------------------
print(Point.color)

p=Point(10,20)
p.draw()
print(p.color)
p.color="Yellow"
print(p.color)

print(Point.color)
print("---------------- p1 ----------------")
p1=Point(3,4)
p1.draw()
print(p1.color)
p1.color='Green'
print(p1.color)