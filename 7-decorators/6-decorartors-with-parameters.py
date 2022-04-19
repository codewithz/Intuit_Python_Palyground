
def smart_divide(function):
    def inner(numerator,denominator):
        print(f"We are going to divide {numerator} by {denominator}")
        if denominator==0:
            print("Cannot divide by 0")
            return

        function(numerator,denominator)
    return inner



@smart_divide
def divide(numerator,denominator):
    return numerator/denominator

print(divide(5,2))
print(divide(5,0))