try:
    with open("1-exceptions.py") as source,open("2-exception-handling.py") as target:
        x=10/1
        print("some operaton inside the with block")
        print("Source closed inside with",source.closed)
        print("target closed inside with", target.closed)

    print("Ouside with inside try")
    print("Source closed outside with", source.closed)
    print("Target closed outside with", target.closed)
except BaseException as ex:
    print("Some other exception occurred")
    print("Reason:",ex)
else:
    print("No exception occurred")
finally:
    print("executes in all conditions [Exceptions occurred or not]")