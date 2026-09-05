Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #list methods
>>> l=[1,2,3,4,5]
>>> l=[10,9,6,1,2,3,4]
>>> l
[10, 9, 6, 1, 2, 3, 4]
>>> id(l)
1931836059520
>>> l.append(12)
>>> l
[10, 9, 6, 1, 2, 3, 4, 12]
>>> l.append(14)
>>> l
[10, 9, 6, 1, 2, 3, 4, 12, 14]
>>> id(l)
1931836059520
>>> l.insert(1,13)
>>> l
[10, 13, 9, 6, 1, 2, 3, 4, 12, 14]
>>> l.extend([23,78,26])
>>> l
[10, 13, 9, 6, 1, 2, 3, 4, 12, 14, 23, 78, 26]
>>> id(l)
1931836059520
>>> l[3]
6
>>> l[3]=60
>>> l
[10, 13, 9, 60, 1, 2, 3, 4, 12, 14, 23, 78, 26]
>>> l[5]=20
>>> l
[10, 13, 9, 60, 1, 20, 3, 4, 12, 14, 23, 78, 26]
>>> id(l)
1931836059520
>>> l.pop()
26
>>> l
[10, 13, 9, 60, 1, 20, 3, 4, 12, 14, 23, 78]
>>> l.pop()
78
>>> l
[10, 13, 9, 60, 1, 20, 3, 4, 12, 14, 23]
id(l)
1931836059520
l.pop(1)
13
l
[10, 9, 60, 1, 20, 3, 4, 12, 14, 23]
l.pop(4)
20
l
[10, 9, 60, 1, 3, 4, 12, 14, 23]
l.remove(4)
l
[10, 9, 60, 1, 3, 12, 14, 23]
del l[1]
l
[10, 60, 1, 3, 12, 14, 23]
l.clear()
l
[]
id(l)
1931836059520
l=[[10,9,1,20,3,12,14]
   l
SyntaxError: '[' was never closed
l=[10,9,1,20,3,12,14]  
l
[10, 9, 1, 20, 3, 12, 14]
max(l)
20
min(l)
1
sorted(l)
[1, 3, 9, 10, 12, 14, 20]
l=[10, 9, 1, 20, 3, 12, 14]  
l
[10, 9, 1, 20, 3, 12, 14]
l.reverse()   
l
[14, 12, 3, 20, 1, 9, 10]
l.sorted()  
l
[1, 3, 9, 10, 12, 14, 20]
l.sorted(reverse=True)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    l.sorted(reverse=True)
AttributeError: 'list' object has no attribute 'sorted'. Did you mean: 'sort'?
l.sort(reverse=True)  
l
[20, 14, 12, 10, 9, 3, 1]
sum(l) 
69
l=[1,2,3]
m=[1,2,3]  
l
[1, 2, 3]
n=l
n.append(4)  
n 
[1, 2, 3, 4]
l
[1, 2, 3, 4]
m=l.copy()  
m 
[1, 2, 3, 4]
l 
[1, 2, 3, 4]
m=l.copy(10)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    m=l.copy(10)
TypeError: list.copy() takes no arguments (1 given)
m=l.append(10)  
m
l 
[1, 2, 3, 4, 10]
all([0,'',[],{},set(),False])
False
all([1,'',[],{},set(),False])
False
any([1,'',[],{},set(),False])
True
l.index(3)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    l.index(3)
NameError: name 'l' is not defined
l=[1,2,3,4]
l
[1, 2, 3, 4]
l.index(3)
2
l.index(5)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    l.index(5)
ValueError: list.index(x): x not in list
l
[1, 2, 3, 4]
l.count(3)
1
l.count(5)
0


