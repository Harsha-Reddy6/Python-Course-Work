'''import re
pattern=r'[0-9]'
text='codegnan'
res=re.match(pattern,text)
print(res.group() if res else "Pattern not found")'''

'''import re
pattern=r'[0-9]'
text='codegnan2026'
res=re.search(pattern,text)
print(res.group() if res else "Pattern not found")'''

'''import re
pattern=r'[0-9]'
text='codegnan 2026 python version 3.14'
res=re.findall(pattern,text)
print(res)'''

'''import re
pattern=r'[0-9]'
text='codegnan2026'
res=re.finditer(pattern,text)
for i in res:
    print(i.group(),i.start())'''

'''import re
pattern=r'[0-9]{10}'
text='2345678888'
res=re.fullmatch(pattern,text)
print(res.group() if res else "Pattern not found")'''

'''import re
pattern=r'[,(#]'
text='java,python(html#css'
res=re.split(pattern,text)
print(res)'''

'''import re
pattern=r'e.t'
text='e@t eaat eat eet ett ect Efghet hgjeuohkj'
res=re.findall(pattern,text)
print(res)'''

'''import re
pattern=r'^(91)'
text='919876543211'
res=re.findall(pattern,text)
print(res)'''

'''import re
pattern=r'0$'
text='9198765432110'
res=re.findall(pattern,text)
print(res)'''

'''import re
pattern=r'to*'
text='to t too tooo toooo'
res=re.findall(pattern,text)
print(res)'''

'''import re
pattern=r'to+'
text='to t too tooo toooo'
res=re.findall(pattern,text)
print(res)'''

'''import re
pattern=r'([a-zA-Z] )+'
text='Codegnan Programming'
res=re.findall(pattern,text)
print(res)'''

'''import re
pattern=r'ab+'
text='ab abbb adfg abbbb abbbbbbb'
res=re.findall(pattern,text)
print(res)'''

'''import re
pattern=r'ab*'
text='ab abbb a acv abbbb abbbbbbb'
res=re.findall(pattern,text)
print(res)'''

'''import re
pattern=r'91|0'
text='91'
res=re.findall(pattern,text)
print(res)
'''

import re
pattern=r'[aeiouAEIOU]'
text='codegnan programming'
res=re.findall(pattern,text)
print(res)


