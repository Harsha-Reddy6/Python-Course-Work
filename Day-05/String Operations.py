Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#strings
s=''
s
''
s='codegnan'
s
'codegnan'
#concatenation
'codegnan'+'PFS'
'codegnanPFS'
#repetation
'codegnan'*10
'codegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnan'
'_*_'*10
'_*__*__*__*__*__*__*__*__*__*_'
>>> #indexing
>>> #indexing
>>> s='codegnan'
>>> s[4]
'g'
>>> s[-1]
'n'
>>> s[1]
'o'
>>> s[-2]
'a'
>>> names='harsha nandhini kala hari'
>>> names[0]
'h'
>>> names[-1]
'i'
>>> #slicing
>>> #s[start:end+1:step]=>s[0:len:1]
>>> names[0:6]
'harsha'
>>> names[7,15]
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    names[7,15]
TypeError: string indices must be integers, not 'tuple'
>>> names[7:15]
'nandhini'
>>> names[-1:-5:-1]
'irah'
>>> names[-6:-10:-1]
'alak'
>>> names[::-1]
'irah alak inihdnan ahsrah'
>>> names[::2]
'hrh adiikl ai'
>>> 'harsha' in names
True
>>> 'hari' in names
True
>>> 'reddy' not in names
True
