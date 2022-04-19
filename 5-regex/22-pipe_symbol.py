import re

word_list = ['sapwood', 'rosewood', 'logwood',
             'teakwood', 'plywood', 'redwood']
pattern='(ply|log)wood'

for word in word_list:
    result=re.match(pattern,word)
    if result:
        print(f"{word} MATCHES FOR {pattern}")
    else:
        print(f"{word} doesn't matches for {pattern}")