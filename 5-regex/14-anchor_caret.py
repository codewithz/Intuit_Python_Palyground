import re


word_list = ['foo bar baz', 'bar foo baz',
             'baz foo bar', 'bar baz foo', 'foo baz bar', 'baz bar foo']
pattern='^foo.*'

for word in word_list:
    result=re.match(pattern,word)
    if result:
        print(f"{word} MATCHES FOR {pattern}")
    else:
        print(f"{word} doesn't matches for {pattern}")