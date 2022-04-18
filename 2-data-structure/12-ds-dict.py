# Dictionary
# Key-Value Pairs
#  {key:value}
# COntact Book Name-> Number

point={"x":1,"y":2}
print(point)

point=dict(x=1,y=2)
print(point)

point["x"]=10
point["y"]=20
point["z"]=30

print(point)

print("------------- Accessing the Data --------------")

print("X:",point.get("x"))
print("A:",point.get("a",0))

for key in point:
    print(key)

for item in point.items():
    print(item)

for key,value in point.items():
    print(key,"-",value)