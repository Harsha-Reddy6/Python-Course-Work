Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=10
float(a)
10.0
str(a)
'10'
complex(a)
(10+0j)
list(a)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
bool(a)
True
set(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
b=10.0
int(b)
10
complex(b)
(10+0j)
str(b)
'10.0'
list(b)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    list(b)
TypeError: 'float' object is not iterable
tuple(b)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    tuple(b)
TypeError: 'float' object is not iterable
set(b)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    set(b)
TypeError: 'float' object is not iterable
dict(b)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    dict(b)
TypeError: 'float' object is not iterable
bool(b)
True
c=8+3j
int(c)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
float(c)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    float(c)
TypeError: float() argument must be a string or a real number, not 'complex'
str(c)
'(8+3j)'
list(c)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    list(c)
TypeError: 'complex' object is not iterable
tuple(c)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    tuple(c)
TypeError: 'complex' object is not iterable
set(c)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    set(c)
TypeError: 'complex' object is not iterable
dict(c)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    dict(c)
TypeError: 'complex' object is not iterable
bool(c)
True
s="codegnan"
int(s)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    int(s)
ValueError: invalid literal for int() with base 10: 'codegnan'
float(s)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    float(s)
ValueError: could not convert string to float: 'codegnan'
complex(s)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    complex(s)
ValueError: complex() arg is a malformed string
list(s)
['c', 'o', 'd', 'e', 'g', 'n', 'a', 'n']
tuple(s)
('c', 'o', 'd', 'e', 'g', 'n', 'a', 'n')
set(s)
{'c', 'o', 'e', 'd', 'a', 'n', 'g'}
dict(s)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    dict(s)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
bool(s)
True
s="12"
int(s)
12
float(s)
12.0
str(s)
'12'
complex(s)
(12+0j)
list(s)
['1', '2']
tuple(s)
('1', '2')
dict(s)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    dict(s)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
bool(s)
True
l=[1,2,3,4]
int(l)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    int(l)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
float(l)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    float(l)
TypeError: float() argument must be a string or a real number, not 'list'
complex(l)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    complex(l)
TypeError: complex() argument must be a string or a number, not list
str(l)
'[1, 2, 3, 4]'
tuple(l)
(1, 2, 3, 4)
dict(l)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    dict(l)
TypeError: object is not iterable
Cannot convert dictionary update sequence element #0 to a sequence
bool(l)
True
t(1,2,3,4,5)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    t(1,2,3,4,5)
NameError: name 't' is not defined
t=(1,2,3,4,5)
int(t)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    int(t)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
float(t)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    float(t)
TypeError: float() argument must be a string or a real number, not 'tuple'
complex(t)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    complex(t)
TypeError: complex() argument must be a string or a number, not tuple
str(t)
'(1, 2, 3, 4, 5)'
list(t)
[1, 2, 3, 4, 5]
dict(t)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    dict(t)
TypeError: object is not iterable
Cannot convert dictionary update sequence element #0 to a sequence
bool(t)
True
dict={1:6,2:7,3:8}
dict
{1: 6, 2: 7, 3: 8}
int(dict)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    int(dict)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'dict'
float(dict)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    float(dict)
TypeError: float() argument must be a string or a real number, not 'dict'
complex(dict)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    complex(dict)
TypeError: complex() argument must be a string or a number, not dict
str(dict)
'{1: 6, 2: 7, 3: 8}'
list(dict)
[1, 2, 3]
tuple(dict)
(1, 2, 3)
bool(dict)
True
t=None
type(t)
<class 'NoneType'>
int(t)
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    int(t)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'NoneType'
float(t)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    float(t)
TypeError: float() argument must be a string or a real number, not 'NoneType'
complex(t)
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    complex(t)
TypeError: complex() argument must be a string or a number, not NoneType
str(t)
'None'
list(t)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    list(t)
TypeError: 'NoneType' object is not iterable
tuple(t)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    tuple(t)
TypeError: 'NoneType' object is not iterable
dict(t)
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    dict(t)
TypeError: 'dict' object is not callable
bool(t)
False
s={1,2,3,4,5,6}
>>> int(s)
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    int(s)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'set'
>>> float(s)
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    float(s)
TypeError: float() argument must be a string or a real number, not 'set'
>>> str(s)
'{1, 2, 3, 4, 5, 6}'
>>> complex(s)
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    complex(s)
TypeError: complex() argument must be a string or a number, not set
>>> list(s)
[1, 2, 3, 4, 5, 6]
>>> tuple(s)
(1, 2, 3, 4, 5, 6)
>>> dict(s)
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    dict(s)
TypeError: 'dict' object is not callable
>>> bool(s)
True
