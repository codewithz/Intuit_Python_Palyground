import re

word_list = ['xxx.yy', 'xx.yyyy', 'x.yy', 'xy', 'xxyy', 'yyxx', 'yx', 'yxxx']
pattern='x*\.y*'

for word in word_list:
    result=re.match(pattern,word)
    if result:
        print(f"{word} MATCHES FOR {pattern}")
    else:
        print(f"{word} doesn't matches for {pattern}")