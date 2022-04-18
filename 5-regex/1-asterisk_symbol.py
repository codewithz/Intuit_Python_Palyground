import re

word_list = ['fooaaaabar', 'fooabar','fooaxbar', 'foobar',
             'fooaabar', 'fooxxxbar', 'fooxbar']

pattern='fooa*bar'

for word in word_list:
    result=re.match(pattern,word)
    if result:
        print(f"{word} MATCHES FOR {pattern}")
    else:
        print(f"{word} doesn't matches for {pattern}")