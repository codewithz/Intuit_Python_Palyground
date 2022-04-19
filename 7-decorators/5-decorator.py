def make_pretty(function):
    def inner():
        print("I got decorated")
        function()

    return inner


@make_pretty
def ordinary_function():
    print(" I am ordinary")


# ---------------------------------

ordinary_function()

