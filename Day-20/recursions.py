'''def func(args):
    if base_condition:
        return
    func(updating args)
func(args)'''
#numbers from 1-n
'''def display(n):
    if n>10:
        return
    print(n)
    display(n+1)
display(1)'''
#reverse of numbers
'''def display(n):
    if n>10:
        return
    display(n+1)
    print(n) 
display(1)'''
#sum of n numbers
'''def sum(n):
    if n==0:
        return 0
    return n+sum(n-1)
print(sum(8))
'''
#product of n numbers
'''def product(n):
    if n==1:
        return 1
    return n*product(n-1)
print(product(5))'''

#recursion on strings
'''
def str(i):
    if i==len(s):
        return
    print(s[i],end=" ")
    str(i+1)
s="python programming"
str(0)
'''
#reverse of a string 
'''def str(i):
    if i==len(s):
        return
    str(i+1)
    print(s[i],end=" ")
s="python programming"
str(0)
'''

'''def str(i):
    if i==len(s)+1: #i>len(s)
        return
    print(s[:i])
    str(i+1)
s="python programming"
str(1)'''
'''or
def str(i,res):
    if i==len(s): #i>len(s)
        return
    res+=s[i]
    print(res)
    str(i+1,res)
s="python programming"
str(0,'')
'''
'''
def str(i,n):
    if i>len(s)-n:
        return
    print(s[i:i+n])
    str(i+1,n)
s="python programming"
str(0,5)'''
#dispaly the digits in a number
'''def display(n):
    if n==0:
        return
    display(n//10)
    print(n%10,end="")
n=987654
display(n)'''
#sum of the digits in a number
'''def display(n):
    if n==0:
        return 0
    return n%10+display(n//10)
n=987654
print(display(n))'''
#fibonacci series
a=0
b=1
n=10
for i in range(n-1):
    a,b=b,a+b
    print(b)

