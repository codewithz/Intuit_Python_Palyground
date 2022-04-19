def is_called():
    def is_returned():
        print("Hello")

    return is_returned

# ---------------------------------------------------

some_object=is_called()

some_object()

# ----------------------------------------

def print_message(message):
    # This is the outer enclosing function
    def printer():
        # This is the neste function
        print(message)

    return printer


some_variable=print_message("Hello Intuit")
del print_message
some_variable()

#-------------------------------------------------------

def make_multiplier_of(n):
    def multiplier(number):
        return n*number
    return multiplier;

# ----Multiplier of 3
times3=make_multiplier_of(3)

result=times3(4)
print(result)

times5=make_multiplier_of(5)
result=times5(4)
print(result)
