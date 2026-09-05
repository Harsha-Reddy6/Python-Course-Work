#generators
'''def retrivedata():
    data=['1..100','101..200','201..300','301..400','401..500']
    for i in data:
        yield i
reels=retrivedata()
while True:
    status=input("scroll or quit: ")
    if status=="scroll":
        print(next(reels))
    else:
        break'''
#even numbers using generators
'''def even():
    i=0
    while True:
        i+=2
        yield i
n=5
res=even()
for i in range(n):
    print(next(res))'''
#factors of a number
'''def factors():
    for i in range(1,n+1):
        if n%i==0:
            yield i
n=12
res=factors(n)
for i in res:
    print(i)
        '''
#primes numbers
'''def isprime(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
def prime(n):
    for j in range(2,n+1):
        if isprime(j):
            yield j
n=50
res=prime(n)
for k in res:
    print(k)
    '''
'''def countdown(n):
    for i in range(n,0,-1):
        yield i
n=10
res=countdown(n)
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))'''

'''def countdown(n):
    i=n
    while i>0:
        yield i
        i-=1
n=int(input())
res=countdown(n)
for j in res:
    print(j)
'''



    


