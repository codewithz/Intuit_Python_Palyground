import re


word_list = [834, 519, 4874, 5, 89, 45687, 25, 645]
pattern='^[0-9]{3}$'

for word in word_list:
    result=re.match(pattern,str(word))
    if result:
        print(f"{word} MATCHES FOR {pattern}")
    else:
        print(f"{word} doesn't matches for {pattern}")