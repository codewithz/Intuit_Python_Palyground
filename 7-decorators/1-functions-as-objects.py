# Everything in Python is an object

def greet(msg):
    print(msg)


greet("Hello")

some_object=greet
print(type(some_object))
some_object("Hi")