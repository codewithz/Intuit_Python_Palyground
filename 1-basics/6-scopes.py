message="Hello ALl"

def greet(name):
    message="Hello"
    print(name)

def send_email():
    global message;
    message="Hi"


print(message)
greet("Tom")
print(message)
send_email()
print(message)

#  Python doesn't support block scope

