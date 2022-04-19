def make_pretty(function):
    def inner():
        print("I got decorated")
        function()

    return inner



def ordinary_function():
    print(" I am ordinary")


# ---------------------------------

ordinary_function()

# -----------------------------------
print("----------------------------")
pretty=make_pretty(ordinary_function)

pretty()