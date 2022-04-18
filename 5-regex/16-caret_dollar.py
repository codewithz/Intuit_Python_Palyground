import re


word_list = ['foo', 'foo baz',
             'baz foo', 'bar baz foo', 'foo baz bar', 'baz bar foo']
pattern='^foo$'

for word in word_list:
    result=re.match(pattern,word)
    if result:
        print(f"{word} MATCHES FOR {pattern}")
    else:
        print(f"{word} doesn't matches for {pattern}")