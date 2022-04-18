try:
    file=open("1-exceptions.py")
    print("File Close Status",file.closed)
    age=int(input("Enter Age:"));
    xfactor=10/age
    print(f"Age is {age} and XFactor is {xfactor}")

except ValueError as ex:
    print("Invalid Age entered")
except ZeroDivisionError  as ex:
    print("You seemed to have entered age as zero")
except BaseException as ex:
    print("Some exception occurred")
    print("Reason",ex)
else:
    print("No exception occurred..")
finally:
    print("executes in all the conditions [Exception occurs or not]")
    file.close()
    print("File Close Status",file.closed)