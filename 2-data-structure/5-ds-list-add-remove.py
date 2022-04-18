letters=["a","b","c"]

print("Original:",letters)

#  Add
letters.append("d")
print("Append:",letters)

# Insert
letters.insert(0,'-')
print("Insert",letters)

# Remove
removed_element=letters.pop(0)
print("Removed Element",removed_element)
print("POP:",letters)

letters.append("tom")
print("Append:",letters)

letters.remove("tom")
print("Remove",letters)

del letters[1]
print("Del",letters)