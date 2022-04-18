# Set ---> No Duplicates | Unordered
#  {}

numbers={1,1,2,3,4,4}
print(numbers)

numbers_list=[1,2,2,3,3,4,4]
unique_set={*numbers_list}
print(unique_set)

first={1,2,3,4}
print("First:",first)

second={1,4,5}
print("Second",second)

second.add(6)
print("Second",second)

second.add(5)
print("Second",second)

second.remove(4)
print("Second",second)

# second.remove(4)
# print("Second",second)
# KeyError: 4

second.discard(6)
print("Second",second)

second.discard(6)
print("Second",second)

print("------------------ Set Operations ------------------------")

print("First:",first)
print("Second:",second)

print("Union:", first.union(second))
print("Union", first | second)

print("Intersection:",first.intersection(second))
print("Intersection:",first & second)

print("Difference:",first.difference(second))
print("Difference",first-second)

print("Symmetric Difference",first.symmetric_difference(second))
print("Symmetric Difference",first ^ second)

