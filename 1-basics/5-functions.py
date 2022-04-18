print("------------------- Normal Function ----------------")

def greet():
    print("Hi There")
    print("Welcome Aboard")


greet()

print("------------------- Function with Parameters ----------------")

def greeting(first_name,last_name):
    print(f"{first_name} {last_name}")

greeting("Zartab","Nakhwa")
greeting("John","Doe")

print("------------------- Function with Return Type ----------------")

#  Types of Functions

# 1. Performs a Task
# 2. Do some processing and return a value

# 1. Perform a Task
def greet(name):
    print(f"Hello {name}")

greet("Test Name")

# -----------------------------------------

def get_greeting(name):
    return f"Hi {name}";

message=get_greeting("Alex")

#  Send it in an email
#  Print on log
# Store in DB
# Send over network

print("DEBUG:",message)

print("---------------- Keyword Arguments----------------")

def increment(number,by):
    added_values=number+by
    return  added_values

result=increment(number=5,by=4)
print(result)

print("------------ Default Arguments-----------------------")

def increment_number(number,by=1):
    return  number+by;

result=increment_number(10)
print(result)

result=increment_number(10,4)
print(result)

print("---------------- Varying Arguments [xargs]---------------")

def multiply(*numbers):
    print(numbers,type(numbers))
    total=1
    for number in numbers:
        total=total*number
    return total

print(multiply(1,2,3,4,5))

print("---------------- Varying Arguments for Dict [xxargs/ kwargs]---------------")

def save_user(**user):
    print(user)
    print(type(user))

save_user(id=1,name='Tom',dept="IT",salary=4567.87)



