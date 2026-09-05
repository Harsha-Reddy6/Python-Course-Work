'''n=int(input())
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()
    '''
'''n=int(input())
for i in range(n):
    for sp in range(n-i-1):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()'''
'''n=int(input())
for i in range(n):
    for sp in range(i):
        print(" ",end=" ")
    for j in range(n-i):
        print("*",end=" ")
    print()'''
'''
n=int(input())
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1:
            print("*",end=" ")
        else:
             print(" ",end=" ")
    print()'''
'''n=int(input())#doubt 
for i in range(n):
    for j in range(n):
        if (i==0 or j==0  or i==n-1  or j==n-1 or  i%2==0 or j%2==0):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    '''
'''n=int(input())#doubt 
for i in range(n):
    for j in range(n):
        if (i==j or i+j==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''
'''n=int(input())#E
for i in range(n):
    for j in range(n):
        if (i==0 or j==0  or i==n-1  or  i==n//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''
'''
n=int(input())#A
for i in range(n):
    for j in range(n):
        if (i==0 or j==0  or i==n//2 or j==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''
'''
n=int(input())#F
for i in range(n):
    for j in range(n):
        if (i==0 or j==0  or i==n//2 or j==n):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
'''
'''
n=int(input())#C
for i in range(n):
    for j in range(n):
        if (i==0 or j==0  or i==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
'''
'''
n=int(input())#B
for i in range(n):
    for j in range(n):
        if (i==0 or j==0  or i==n-1 or i==n//2 or j==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    '''
'''
n=int(input())#G
m=n//2
for i in range(n):
    for j in range(n):
        if (i==0 or j==0  or (i==n-1 and j<=m) or (j==m and i>=m) or (i==m and j>=m) or (j==n-1 and i>=m)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    '''
'''
n=int(input())#k
m=n//2
for i in range(n):
    for j in range(n):
        if (j==0 or (i==m and j<=m) or (i+j==n-1 and i<=m) or (i==j) and i>=m):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
'''
'''
n=int(input())#M
m=n//2
for i in range(n):
    for j in range(n):
        if (j==0 or j==n-1 or (i+j==n-1 and i<=m) or (i==j and i<=m)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    '''
'''
n=int(input())#H
m=n//2
for i in range(n):
    for j in range(n):
        if (j==0 or j==n-1 or i==m):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    '''
'''
n=int(input())#I
m=n//2
for i in range(n):
    for j in range(n):
        if (i==0 or i==n-1 or j==m):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    '''
'''
n=int(input())#L
for i in range(n):
    for j in range(n):
        if (j==0 or i==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    '''
'''
n=int(input())#N
for i in range(n):
    for j in range(n):
        if (j==0 or j==n-1 or i==j):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
'''
'''
n=int(input())#O
for i in range(n):
    for j in range(n):
        if (j==0 or j==n-1 or i==0 or i==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''
'''n=int(input())#P
m=n//2
for i in range(n):
    for j in range(n):
        if (i==0 or j==0 or i==m or (i<=m and j==n-1)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''
'''
n=int(input())#S
m=n//2
for i in range(n):
    for j in range(n):
        if ((i==0 or i==n-1 or i==m ) and (j<n))or (j==0 and i<m or j==n-1 and i>m):
            print("*",end=" ")
        else:
            print(" ",end=" ")w
    print()'''
'''n=int(input())#T
m=n//2
for i in range(n):
    for j in range(n):
        if (i==0 or j==m):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
'''
'''n=int(input())#U
for i in range(n):
    for j in range(n):
        if (j==0 or j==n-1 or i==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
'''
'''
n=int(input())#W
m=n//2
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or (i==j and i>=m) or (i+j==n-1 and i>=m):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
'''
'''
n=int(input())#X
for i in range(n):
    for j in range(n):
        if (i==j or i+j==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''
'''
n=int(input())#Y
m=n//2
for i in range(n):
    for j in range(n):
        if i+j==n-1 or (i==j and i<=m):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''
'''
n=int(input())#Z
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or i+j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''
'''n=int(input())#D
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==0 or i==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''
'''
n = int(input("Enter size: "))#R
mid = (n - 1) // 2
for i in range(n):
    for j in range(n):
        if (j == 0 or i == 0 or
            i == mid or (j == n-1 and 0 < i < mid) or(i - mid == j and i > mid)):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()'''
'''
n=int(input("Enter the number: "))#J
for i in range(n):
    for j in range(n):
        if i==0 or (j==0 and i>=n-3) or (i==n-1 and j<n//2) or j==n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    '''
'''
n=int(input())#Q
m=n//2
for i in range(n):
    for j in range(n):
        if (i==0 or j==0 or i==n-1 or j==n-1 or (i==j and i>=m)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
'''
'''
n=int(input())#Y
m=n//2
for i in range(n):
    for j in range(n):
        if (i==j and i<=m) or (i+j==n-1 and i<=m) or (j==m and i>=m):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    '''
'''
n = int(input("Enter size: "))#R
mid = (n - 1) // 2
for i in range(n):
    for j in range(n):
        if (j == 0 or i == 0 or
            i == mid or (j == n-1 and 0 < i < mid) or(i - mid == j and i > mid)):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()'''
'''
n=int(input("Enter the number: "))#J
for i in range(n):
    for j in range(n):
        if i==0 or (j==0 and i>=n-3) or (i==n-1 and j<n//2) or j==n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    '''
'''
n=int(input())#Q
m=n//2
for i in range(n):
    for j in range(n):
        if (i==0 or j==0 or i==n-1 or j==n-1 or (i==j and i>=m)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
'''

