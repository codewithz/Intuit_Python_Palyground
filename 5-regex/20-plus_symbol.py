import re

word_list = ['fooaaaabar', 'fooabar', 'foobar',
             'fooaabar', 'fooxxxbar', 'fooxar']
pattern='fooa+bar'

for word in word_list:
    result=re.match(pattern,word)
    if result:
        print(f"{word} MATCHES FOR {pattern}")
    else:
        print(f"{word} doesn't matches for {pattern}")