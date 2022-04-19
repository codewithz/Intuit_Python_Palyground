import re

word_list = ['zartab@codewithz.com','zartab.n@uni.edu','zartab-n-1312@my-company.net']
pattern='^[A-Za-z][A-Za-z0-9_.]+@[A-Za-z][A-Za-z0-9-.]+\.(com|net|org|edu)'

for word in word_list:
    result=re.match(pattern,word)
    if result:
        print(f"{word} MATCHES FOR {pattern}")
    else:
        print(f"{word} doesn't matches for {pattern}")