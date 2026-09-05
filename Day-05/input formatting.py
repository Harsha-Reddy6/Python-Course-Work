Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#int float str list tuple set dict
x=input()
harsha
x
'harsha'
name="harsha"
name
'harsha'
name=input("enter your name: ")
enter your name: harsha
name
'harsha'
age=input("enter the age:")
enter the age:21
age
'21'
age=int(input("enter the age:"))
enter the age:21
age
21
type(age)
<class 'int'>
price=input("enter the price :")
enter the price :99.99
price
'99.99'
price=float(input("enter the price :"))
enter the price :99.99
price
99.99
#list
names=input("enter the names :")
enter the names :harsha nandhini kala
names
'harsha nandhini kala'
names.split()
['harsha', 'nandhini', 'kala']
names=input("enter the names :").split()
enter the names :harsha nandhini kala
names
['harsha', 'nandhini', 'kala']
numbers=input("enter the numbers").split()
enter the numbers 1 2 3 4 5 6
numbers
['1', '2', '3', '4', '5', '6']
map(int,numbers)
<map object at 0x000002298412CC40>
list(map(int,numbers))
[1, 2, 3, 4, 5, 6]
values=list(map(int,input().split()))
1 3 2 4 5 6 7
values
[1, 3, 2, 4, 5, 6, 7]
values=list(map(float,input().split()))
1.2 3.4 5.2 6.5
values
[1.2, 3.4, 5.2, 6.5]
names=tuple(input("enter the names :").split())
enter the names : 1 2 3 4 
names
('1', '2', '3', '4')
values=tuple(int,input("enter the values :").split())
enter the values :1 2 3 45 4 
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    values=tuple(int,input("enter the values :").split())
TypeError: tuple expected at most 1 argument, got 2
values=tuple(map(int,input("enter the values :").split()))
enter the values :1 2 3 4
values
(1, 2, 3, 4)
values=tuple(map(float,input("enter the values :").split()))
enter the values :1.2 3.2 4.3 5.4 
values
(1.2, 3.2, 4.3, 5.4)
values=set(input()"enter the numbers: ").split())
SyntaxError: unmatched ')'
values=set(input("enter the numbers: ").split())
enter the numbers: 1 3 2 4 5
values
{'2', '3', '5', '1', '4'}
values=set(map(int,input("enter the numbers: ").split()))
enter the numbers: 1 2 3 4 5
values
{1, 2, 3, 4, 5}
values=set(map(float,input("enter the numbers: ").split()))
enter the numbers: 1.2 3.4 5.4 6.8
values
{1.2, 3.4, 5.4, 6.8}
#how should we take the multiple values at the same time
a,b=[1,2]
a
1
b
2
a,b=(1,2)
a
1
b
2
email,password=input("Enter the email and password: ").split()
Enter the email and password: harsha@gamil.com 12345
email
'harsha@gamil.com'
password
'12345'
a,b,c=list(map(int,input().split()))
1 23 
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    a,b,c=list(map(int,input().split()))
ValueError: not enough values to unpack (expected 3, got 2)
1 2 3
SyntaxError: invalid syntax
a,b,c=list(map(int,input().split()))
1 2 3
a
1
b
2
c
3
name,marks=input().split()
harsha 98
names
('1', '2', '3', '4')
name
'harsha'
>>> marks
'98'
>>> int(marks)
98
>>> e=eval(input())
1
>>> e
1
>>> e=eval(input())
1.2 3.4
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    e=eval(input())
  File "<string>", line 1
    1.2 3.4
        ^^^
SyntaxError: invalid syntax
>>> e=eval(input())
1.2
>>> e
1.2
>>> e=eval(input())
"harsha"
>>> e
'harsha'
>>> e=eval(input())
[1,2,3]
>>> e
[1, 2, 3]
>>> e=eval(input())
(1,2,3,4)
>>> e
(1, 2, 3, 4)
>>> e=eval(input())
[1,1.2,"harsha",[1,2,3],(1,2,3,4)]
>>> e
[1, 1.2, 'harsha', [1, 2, 3], (1, 2, 3, 4)]
>>> e=eval(input())
True
>>> e
True
