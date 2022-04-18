letters=["a","b","c","d","e"];
print(letters)

#  Access the first element
print(letters[0])
# Access the last element
print(letters[-1])

# Access In Ranges

print(letters[0:2])
print(letters[:3])
print(letters[2:])

# Clone
letters_clone=letters[:]
print('Clone:',letters_clone)

# Steppers in List
numbers=list(range(1,21))
print(numbers[::2])
print(numbers[::-1])
