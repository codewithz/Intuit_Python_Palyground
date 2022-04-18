import re

word_list = ['fooabar', 'fooxbar', 'baryfoo',
             'foobar', 'fooxybar', 'foocbar','foo3bar']

pattern='foo.bar'

for word in word_list:
    result=re.match(pattern,word)
    if result:
        print(f"{word} MATCHES FOR {pattern}")
    else:
        print(f"{word} doesn't matches for {pattern}")