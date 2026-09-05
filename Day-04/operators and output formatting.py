Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=20
b=10
a+b
30
a-b
10
a*b
200
a/b
2.0
a//b
2
a%b
0
4**2
16
#comparision operators
a
20
b
10
a<b
False
a>b
True
a<=b
False
a>=b
True
a==b
False
a!=b
True
#Assignment operators
c=10
c=c+10
c
20
c=c+10
c
30
c=c+10
c
40
c+=10
c
50
c-=10
c
40
c*=2
c
80
c//2=2
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
c //=2
c
40
c**2
1600
c**=2
c
1600
c%=3
c
1
c/=2
c
0.5
#relational operators
#and
True and True
True
True and False
False
n=10
n%2==0
True
n%3==0
False
n%2==0 and n%3==0
False
n%2==0 or n%3==0
True
n%8==0 or n%3==0
False
n
10
n<5
False
not n<5
True
#membership operation
s="codegnan"
"e" in s
True
"z" in s
False
"f" not in s
True
"o" not in s
False
l=[1,2,3,4]
4 in l
True
6 in l
False
8 not in l
True
t=(1,2,3,4)
1 in tr
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    1 in tr
NameError: name 'tr' is not defined. Did you mean: 't'?
1 in t
True
5 not in t
True
s={1,2,3,4,5,6,7}
6 in s
True
7 not in s
False
8  not in s
True
d={"name":"harsha","batch":"63","course":"python"}




"name" in d
True
"harsha" in d
False
"course" not in d
False
"63" in d
False
#IDENTITY operator
l=[1,2,3,4]
m=[1,2,3,4]
id(l)
2246566997888
id(m)
2246611988864
l is m
False
n=l
id(n)
2246566997888
l is n
True
l is not m
True
l is not n
False
#Bitwise operators
#mutable
s={1,2,3,4}
id(s)
2246611525792
s.add(6)
s
{1, 2, 3, 4, 6}
id(s)
2246611525792
a=20
a
20
a+=10
a
30
id(a)
140733675915288
#immutable
s="cdegnan"
id(s)
2246611905888
s="codegnan course"
id(s)
2246612030576
#bitwise operators
9&8
8
9@10
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    9@10
TypeError: unsupported operand type(s) for @: 'int' and 'int'
9&10
8
9|10
11
9^10
3
8<<2
32
8>>2
2
8>>3
1
~8
-9
~10
-11
~44
-45
#output formattinga
a=10
b=10.3
c="codegnan"
print(a,b,c)
10 10.3 codegnan
print("a value is ",a)
a value is  10
>>> print("a value is ",a ,"b value is ",b,"c value is ",c)
a value is  10 b value is  10.3 c value is  codegnan
>>> print("a value is ",a ,"| b value is ",b,"| c value is ",c)
a value is  10 | b value is  10.3 | c value is  codegnan
>>> print(a,b,c)
10 10.3 codegnan
>>> print(a,b,c,sep='')
1010.3codegnan
>>> print(a,b,c,sep='/n')
10/n10.3/ncodegnan
>>> print(a,b,c,sep='\n')
10
10.3
codegnan
>>> print(a,b,c,sep='\t',end='@')
10	10.3	codegnan@
>>> print(a,b,c,sep='\t')
10	10.3	codegnan
>>> print(a,b,c,sep='\t',end='\n\n')
10	10.3	codegnan

>>> #fstring
>>> print(f' a={a} b={b} c={c}')
 a=10 b=10.3 c=codegnan
>>> print('a=%d b=%f c=%s'%(a,b,c))
a=10 b=10.300000 c=codegnan
>>> print('a=%d b=%.2f c=%s'%(a,b,c))
a=10 b=10.30 c=codegnan
>>> print("a value is ",{a}| b value is ",b,"| c value is ",c)
...       
SyntaxError: unterminated string literal (detected at line 1)
>>> print("a ={}| b = {}| c = {}".format(a,b,c))
...       
a =10| b = 10.3| c = codegnan
>>> print("a ={}| b = {}| c = {}".format(c,a,b))
...       
a =codegnan| b = 10| c = 10.3
>>> print("a ={1}| b = {2}| c = {0}".format(a,b,c))
...       
a =10.3| b = codegnan| c = 10
