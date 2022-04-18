try:
    age=int(input("Enter Age:"));
    xfactor=10/age
    print(f"Age is {age} and XFactor is {xfactor}")
    # numbers=[1,2]
    # print(numbers[3])
except ValueError as ex:
    print("Invalid Age entered")
except ZeroDivisionError  as ex:
    print("You seemed to have entered age as zero")
except BaseException as ex:
    print("Some exception occurred")
    print("Reason",ex)
else:
    print("No exception occurred..")


# https://docs.python.org/3/library/exceptions.html