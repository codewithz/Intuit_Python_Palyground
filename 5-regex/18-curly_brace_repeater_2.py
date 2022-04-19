import re


word_list = ['lion', 'tiger', 'leopard', 'fox',
             'kangaroo', 'cat', 'mouse', 'cuckoo', 'deer']
pattern='^[a-z]{4,6}$'

for word in word_list:
    result=re.match(pattern,word)
    if result:
        print(f"{word} MATCHES FOR {pattern}")
    else:
        print(f"{word} doesn't matches for {pattern}")