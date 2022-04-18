try:
    age=int(input("Enter Age:"))
    print(f"Age is {age}")
except ValueError as ex:
    print("You seem to have entered invalid age")
    print(ex)
else:
    print("Else is executed when no exception occur")



print("Execution Continues...")