Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#string methods
c="python programming"
len(c)
18
ord(p)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    ord(p)
NameError: name 'p' is not defined
ord('p')
112
ord('o')
111
ord('a')
97
ord('0')
48
ord('D')
68
chr(65)
'A'
chr(66)
'B'
min(c)
' '
max(c)
'y'
\
sorted(c)
[' ', 'a', 'g', 'g', 'h', 'i', 'm', 'm', 'n', 'n', 'o', 'o', 'p', 'p', 'r', 'r', 't', 'y']
c='String is immutable'
c.upper()
'STRING IS IMMUTABLE'
c.lower()
'string is immutable'
c.captalize()
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    c.captalize()
AttributeError: 'str' object has no attribute 'captalize'. Did you mean: 'capitalize'?
c.capitalize()
'String is immutable'
c.title()
'String Is Immutable'
c.swapcase()
'sTRING IS IMMUTABLE'
"STRAẞEMÁLAGAÅngströmCafé".casefold()
'strassemálagaångströmcafé'
c.center(60,'-')
'--------------------String is immutable---------------------'
c.ljust(60,'-')
'String is immutable-----------------------------------------'
c.rjust(60,'-')
'-----------------------------------------String is immutable'
'12'.zfill()
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    '12'.zfill()
TypeError: str.zfill() takes exactly one argument (0 given)
'12'.zfill(4)
'0012'
'12'.zfill(10)
'0000000012'
'1234454'.zfill(5)
'1234454'
'435'.zfill(5)
'00435'
c
'String is immutable'
c.find()
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    c.find()
TypeError: find expected at least 1 argument, got 0
c.find
<built-in method find of str object at 0x0000017B468EAEB0>
c.find('s')
8
c.find('S')
0
c.find("i")
3
c.find('z')
-1
c.find('i')
3
c.rfind('i')
10
c
'String is immutable'
c.index("i")
3
c.rindex("i")
10
c.index("z")
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    c.index("z")
ValueError: substring not found
c.count("i")
3
c
'String is immutable'
c.count("g")
1
c
'String is immutable'
c.replace('i','o')
'Strong os ommutable'
c.repalce('String','Float')
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    c.repalce('String','Float')
AttributeError: 'str' object has no attribute 'repalce'. Did you mean: 'replace'?
c.replace('String','Float')
'Float is immutable'
c.maketrans('aeiou','12345')
{97: 49, 101: 50, 105: 51, 111: 52, 117: 53}
c.translate(c.maketrans('aeiou','12345'))
'Str3ng 3s 3mm5t1bl2'
c.translate(c.maketrans('aeiou','*****'))
'Str*ng *s *mm*t*bl*'
c.split()
['String', 'is', 'immutable']
'String is immutable'.split()
['String', 'is', 'immutable']
'String is immutable'.rsplit('',1)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    'String is immutable'.rsplit('',1)
ValueError: empty separator
'String is immutable'.rsplit(' ',1)
['String is', 'immutable']
'String is immutable'.split(' ',1)
['String', 'is immutable']
'String,is,immutable'.split()
['String,is,immutable']
'String,is,immutable'.split(',')
['String', 'is', 'immutable']
'String is immutable'.rsplit()
['String', 'is', 'immutable']
s='''
python
programming
lang'''
s
'\npython\nprogramming\nlang'
>>> s.splitlines()
['', 'python', 'programming', 'lang']
>>> ['', 'python', 'programming', 'lang'].join()
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    ['', 'python', 'programming', 'lang'].join()
AttributeError: 'list' object has no attribute 'join'
>>> ''.join(['', 'python', 'programming', 'lang'])
'pythonprogramminglang'
>>> ' '.join(['', 'python', 'programming', 'lang'])
' python programming lang'
>>> '-'.join(['', 'python', 'programming', 'lang'])
'-python-programming-lang'
>>> '-'.join([1,2,3])
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    '-'.join([1,2,3])
TypeError: sequence item 0: expected str instance, int found
>>> '-'.join(['1','2','3'])
'1-2-3'
>>> 'python.py'.partition('.')
('python', '.', 'py')
>>> s='java,python,c,c++'
>>> s.partition(',')
('java', ',', 'python,c,c++')
>>> s.rpartition(',')
('java,python,c', ',', 'c++')
>>> c="         Hello        world      "
>>> c.strip()
'Hello        world'
>>> c.lstrip()
'Hello        world      '
>>> c.rstrip()
'         Hello        world'
>>> text='Hello 🙂'

>>> text.encode()
b'Hello \xf0\x9f\x99\x82'
>>> b'Hello \xf0\x9f\x99\x82'.decode()
'Hello 🙂'
