letters=["a","b","c","d","e","f"]

print(letters.index("a"))

# Way 1 - to make sure if the element is not found the program doesn't break
if 'g' in letters:
    print(letters.index("g"))
# Way 2 - to make sure if the element is not found the program doesn't break
count=letters.count("d")
if count>0:
    print(letters.index("d"))