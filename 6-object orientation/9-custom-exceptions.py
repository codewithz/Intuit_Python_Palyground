class ValueTooLargeError(Exception):
    """Raise it when the input value is too large"""
    pass

class ValueTooSmallError(Exception):
    """Raise it when the input is too small"""
    pass

# ----------------------------------------------------------------


number=12
# number we need to guess

#  User guesses a number until the get it right
while True:
    try:
        incoming_number=int(input("Enter a number:"))
        if incoming_number<number:
            raise ValueTooSmallError
        elif incoming_number>number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print("Entered value is small. Try Again")
    except ValueTooLargeError:
        print("Entered value is large. Try Again")


print("Congratulations")






