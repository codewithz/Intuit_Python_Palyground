import re

word_list = ['9999912345','1234567890','12345','987543212','98701234','7713045261']
pattern='^[7-9]{1,1}[0-9]{9,9}$'

for word in word_list:
    result=re.match(pattern,word)
    if result:
        print(f"{word} MATCHES FOR {pattern}")
    else:
        print(f"{word} doesn't matches for {pattern}")