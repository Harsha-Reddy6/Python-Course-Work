'''def funcname(arg):
    #stmts
    #stmts
    #return (optional)
func(para)
'''
'''
def display(name,email,password):
    print(f" Hello {name}")
    print(f" your email: {email}")
    print(f" your password: {password}")
display("harsha","harsha@gmail.com","harsha@12")
display("varsha","varsha@gmail.com","varsha@12")
display("harshi","harshi@gmail.com","harshi@12")
'''

'''def isleapyear(year): 
    if (year%400==0 or year%4==0) and year%100!=0:
        print("Leap year")
    else:
        print("Not a leap year")
for year in range(2000,2027):
    isleapyear(year)
    '''
'''def sumofdigits(n):
    s=0
    while n>0:
        r=n%10
        s+=r
        n=n//10
    return s
n=int(input("Enter the number: "))
print(f"sum of {n} digits is {sumofdigits(n)}")'''
'''def productofdigits(n):
    p=1
    while n>0:
        r=n%10
        p*=r
        n=n//10
    return p
n=int(input("Enter the number: "))
print(f"product of {n} digits is {productofdigits(n)}")'''
'''
def checkpassword(password):
    if len(password)<8 :
        return "weakpassword"
    else:
        for ch in password:
            if ch.isupper(): 
                upper= True
            elif ch.islower():
                lower= True
            elif ch.isdigit():
                digit= True
            else:
                special= True
        if upper and lower and digit and special ==True:
            return "strong password"
        else:
            return "Weak password"
password=input("Enter the password: ")
print(checkpassword(password))'''
'''def checkpassword(password):
    if len(password)>8:
        check=set()
        for ch in password:
            if ch.isupper(): 
                check.add('u')
            elif ch.islower():
                check.add('l')
            elif ch.isdigit():
                check.add('d')
            else:
                check.add('s')
        if len(check)==4:
            return "strong password"
    return "Weak password"
password=input("Enter the password: ")
print(checkpassword(password))'''

'''def table(n):
    print(f"----------------------Table - {n} -----------------------")
    for i in range(1,11):
        print(f'{n}*{i} = {n*i}')
for i in range(1,21):
    table(i)
'''




        










