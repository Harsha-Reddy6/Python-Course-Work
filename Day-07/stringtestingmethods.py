Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
c='string.py'
c.startswith('str')
True
c.startswith('python')
False
c.endswith('str')
False
c.endswith('py')
True
c.islower()
True
c.isupper()
False
'PYTHON123'.isupper()
True
c.isalpha()
False
c.isalnum()
False
's123'.isalnum()
True
's.123'.isalnum()
False
'  '.isspace()
True
'n    'isspace()
SyntaxError: invalid syntax
'n    '.isspace()
False
'this is title'.istitle()
False
'This Is Title'.istitle()
True
my@var.isidentifier()
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    my@var.isidentifier()
NameError: name 'my' is not defined
'my@var'.isidentifier()
False
>>> 'my_var'.isidentifier()
True
>>> #list
>>> l=[]
>>> l=list()
>>> l=[1,2.3,2+3j,'str',[1,2,3],(1,2,3),{1,2,3},{1:2,2:3},None]
>>> l
[1, 2.3, (2+3j), 'str', [1, 2, 3], (1, 2, 3), {1, 2, 3}, {1: 2, 2: 3}, None]

>>> l=[1,1,1]
>>> l
[1, 1, 1]
>>> type(l)
<class 'list'>
>>> l=[1,2,3,4]
>>> m=[5,6,7,8]
>>> l+m
[1, 2, 3, 4, 5, 6, 7, 8]
>>> m*3
[5, 6, 7, 8, 5, 6, 7, 8, 5, 6, 7, 8]
>>> l
[1, 2, 3, 4]
>>> l[3]
4
>>> l[-1]
4
>>> l.[1::]
SyntaxError: invalid syntax
>>> l[1::]
[2, 3, 4]
>>> l[:2]
[1, 2]
>>> l[::-1]
[4, 3, 2, 1]
>>> 4 in l
True
>>> 5 not in l
True
