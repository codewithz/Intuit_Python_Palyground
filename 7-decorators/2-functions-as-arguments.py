# Functions which takes another function as an argument
# are considered as Higher Order Functions

def increment(number):return number+1;

def decrement(number): return number -1;

def operate(function,number):
    result=function(number)
    return result;


print(operate(increment,5))


print(operate(decrement,4))