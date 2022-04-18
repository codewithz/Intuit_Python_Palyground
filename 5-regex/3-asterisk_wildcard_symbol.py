import re

word_list = ['foobar', 'barfoo', 'fooabcbar',
             'foobxcbar', 'barcbyfoo', 'foozbar', 'barafoo', 'barabfoo']

pattern='foo.*bar'

for word in word_list:
    result=re.match(pattern,word)
    if result:
        print(f"{word} MATCHES FOR {pattern}")
    else:
        print(f"{word} doesn't matches for {pattern}")