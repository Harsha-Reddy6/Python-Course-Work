Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#nested list
l=[1,2,3,4]
l
[1, 2, 3, 4]
l=[[1,2,3,4],[5,6,7,8]]
l[0]
[1, 2, 3, 4]
l[1]
[5, 6, 7, 8]
l[0][2]
3
l[1][3]
8
l[-1][-1]
8
#tuple
t=()
t=tuple()
t=(1,12.3,3+5j,"str",[1,2,3],(1,2,3),{1,2},{1:1},True)
t
(1, 12.3, (3+5j), 'str', [1, 2, 3], (1, 2, 3), {1, 2}, {1: 1}, True)
t=(1,2,3,4,4,4,4)
t
(1, 2, 3, 4, 4, 4, 4)
l=(1,2,34)
m=(45,67,89)
l+m
(1, 2, 34, 45, 67, 89)
l*5
(1, 2, 34, 1, 2, 34, 1, 2, 34, 1, 2, 34, 1, 2, 34)
45 in m:
    
SyntaxError: invalid syntax
45 in m
True
2 in l
True
m[1]
67
m[-2]
67
l[:2]
(1, 2)
t=1,2,3,4,4
t
(1, 2, 3, 4, 4)
a,b,c,d,e=t
a
1
b
2
c
3
d
4
e
4
t=(1,)
t
(1,)
t=(10,90,80,20,30,50)
t
(10, 90, 80, 20, 30, 50)
len(t)
6
>>> max(t)
90
>>> min(t)
10
>>> sorted(t)
[10, 20, 30, 50, 80, 90]
>>> sum(t)
280
>>> t.index(20)
3
>>> t.count(20)
1
>>> t=((1,2),(2,3),(3,4),(4,5))
>>> t[0]
(1, 2)
>>> t[-2]
(3, 4)
>>> t[1]
(2, 3)
>>> t[-1][-1]
5
>>> t[-2][0]
3
>>> t=(1,2,3,[4,5],6,True)
>>> t
(1, 2, 3, [4, 5], 6, True)
>>> t[1]
2
>>> t[1]=20
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    t[1]=20
TypeError: 'tuple' object does not support item assignment
>>> t[3]
[4, 5]
>>> t[3].append(10)
>>> t
(1, 2, 3, [4, 5, 10], 6, True)
