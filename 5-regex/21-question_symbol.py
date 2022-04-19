import re

word_list = ['https://website', 'http://website',
             'httpss://website', 'httpx://website', 'httpxx://website']
pattern='https?://website'

for word in word_list:
    result=re.match(pattern,word)
    if result:
        print(f"{word} MATCHES FOR {pattern}")
    else:
        print(f"{word} doesn't matches for {pattern}")