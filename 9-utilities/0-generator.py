from sys import getsizeof

values=(x*2 for x in range(1000000))
print(values)
print("Size of Gen",getsizeof(values))

values=[x*2 for x in range(1000000)]
# print(values)
print("Size without Gen",getsizeof(values))
