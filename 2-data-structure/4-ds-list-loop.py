letters=["a","b","c","d","e","f"]


for lettter in letters:
    print(lettter)

print('----------------------------------------------')

for element in enumerate(letters):
    print(element)
    print(type(element))

print("-----------------------------------------------")
data=(0, 'a')
index,value=data

for index,letter in enumerate(letters):
    print(index,'-',letter)