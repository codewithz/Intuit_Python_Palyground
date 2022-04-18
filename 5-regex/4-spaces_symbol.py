import re

word_list = ['fooxxxbar', 'foo   bar', 'fooxbar', 'fooxxbar'
                                                  'foo bar', 'foo      bar', 'foobar', 'fooyyybar']

pattern='foo\s*bar'

for word in word_list:
    result=re.match(pattern,word)
    if result:
        print(f"{word} MATCHES FOR {pattern}")
    else:
        print(f"{word} doesn't matches for {pattern}")