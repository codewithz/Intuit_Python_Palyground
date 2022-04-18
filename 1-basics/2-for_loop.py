for number in range(3):
    print("Attempt",(number+1),(number+1)*'.')

print("-------------------------------------------")

for number in range(1,4):
    print("Attempt",number,number*'.')
print("-------------------------------------------")
# for ..else

successful=False

for number in range(1,6):
    print("Attempting to send a message")
    if number==2 and successful:
        print("Message sending is successful")
        break
else:
    print("Attempted for 5 times and failed",number)

# else after for --- will be executed only when the for loop doesn't end early

print("-------------------------------------------")

# Nested Loop
# (0,0)
# (0,1)
#  (0,2)
#  (1,0)
#  (1,1)
#  (1,2)
#  (2,0)
# (2,1)
# (2,2)
#
#
#  (5,2)

for x in range(6):
    for y in range(3):
        print("("+str(x)+","+str(y)+")");
        print(f"({x},{y})")


