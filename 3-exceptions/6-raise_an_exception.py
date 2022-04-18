def calculate_xfactor(number):
    if number<=0:
        raise ValueError("Number cannot be 0 or less")
    return  10/number;


# ----------------------------------------------------

try:
    xfactor=calculate_xfactor(-10)
    print(xfactor)
except ValueError as ex:
    print(ex)