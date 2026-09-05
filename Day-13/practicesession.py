'''n=int(input("enter a number: "))
if n>0:
    print("Positive number")
else:
    print("negative number")
'''
'''n=int(input("enter a number: "))
if n%2==0:
    print("Even number")
else:
    print("odd number)
    '''
'''n=int(input("enter a number: "))
if n%5==0:
    print("Divisible by 5")
else:
    print("Not divisible by 5)
    '''
'''
n=int(input("enter a number: "))
if n%3==0 and n%7==0:
    print("Divisible by both 3 and 7")  
else:
    print("Not divisible by both")
    '''
'''n=int(input("enter a number: "))
if n%400==0 or (n%4==0 and n%100!=0):
    print("Leap Year")  
else:
    print("not a leap year")'''
'''n=int(input("enter a number: "))
if n>35:
    print("Pass")  
else:
    print("fail")
    '''
'''n=int(input("enter a number: "))
l=list(str(n))
if len(l)==3:
    print("3-digit number")  
else:
    print("not a 3-digit number")'''
'''c=input()
if c in "aeiouAEIOU":
    print("Vowel")
else:
    print("not a vowel")'''

'''a=int(input())
b=int(input())
if a>b:
    print(a)
else:
    print(b)'''
'''a=int(input())
b=int(input())
if a<b:
    print(a)
else:
    print(b)'''
'''n=int(input())
if n==0:
    print("Number is zero")
else:
    print("Not a zero")'''
'''n=int(input())
if n%10==0:
    print("Multiple of 10")
else:
    print("Not a Multiple of 10")'''
'''age=int(input())
if age>18:
    print("Eligible to vote")
else:
    print("Not  Eligible to vote")'''
'''n=int(input())
if 1<=n<=100:
    print("In range")
else:
    print("Not In range")'''
'''a=int(input())
b=int(input())
if b*b==a:
    print(f"{a} is square of {b}")
else:
    print("not a square")'''
'''s1=input()
s2=input()
if s1==s2:
    print("Strings are equal")
else:
    print("Strings are  not equal")'''
'''n=int(input())
if n<2:
    print("Not a prime")
else:
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c==2:
        print("Prime number")
    else:
        print("Not prime")'''
'''n=int(input())
if n>0 and n%2==0:
    print("Positive and even number")
else:
    print("not a positive and even number")'''
'''ch=input()
if ch.isupper():
    print("Uppercase letter")
else:
    print("not a uppercase")'''
'''temp=int(input())
if temp>35:
    print("its hot")
else:
    print("cool")
'''
#4-digit even number
'''n=int(input())
if n>=1000 and n<=9999 and n%2==0:
    print("4-digit even number")
else:
    print("Not a 4-digit even number")'''
#if a character is consonant
'''s=input()
if s in "AEIOUaeiou":
    print("vowels")
else:
    print("consonant")
     #or
ch =input()
if ch.isalpha() and  ch.lower() not in "aeiou":
    print("consonant")
else:
    print("not a consonant")
'''
#if a number is divisible by 2 or 3 but not both
'''n=int(input())
if n%2==0 and n%3==0:
    print("divisible by both 2 and 3")
elif n%2==0:
    print("Divisible by 2")
elif n%3==0:
    print("Divisible by 3")
else:
    print("not divisible by both 2 and 3")'''
#number is negative and odd
'''n=int(input())
if n<0 and n%2!=0:
    print("Negative and odd number")
    '''
#string starts with a vowel
'''s=input()
if s.startswith(("a","e","i","o","u","A","E","I","O","U")):
    print("starts with vowel")
else:
    print("does not starts with vowels")
        #or 
s=input()
if s[0] in "aeiouAEIOU":
    print("Starts with vowel")      
else:
    print("not starts with vowels")'''

#if three sides form a valid triangle
'''a,b,c = list(map(int,input().split(',')))
if a+b>c and b+c>a and a+c>b:
    print("Valid triangle")
else:
    print("Not a Valid triangle")'''
#the greatest among three numbers
'''a,b,c = list(map(int,input().split(',')))
if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
else:
    print(c)
'''
'''n=int(input())
if n%100==0 and n%400==0 :
    print("century year and leap year")
else:
    print("not a century leap year")'''

#electric city bill
'''units=int(input())
s_c=eval(input())
if units>0 and units<=100:
    bill=units*1.5
    print(bill)
elif units>=101 and units<=200:
    bill=units*2.5
    print(bill)
elif units>=201 and units<=500:
    bill=units*4
    print(bill)
elif units>500 and units<=800:
    bill=units*6
    print(bill)
else:
    bill= 
elif s_c==True:
    bill=bill-(bill*0.01)
    print(bill)
#or
units = int(input())
s_c = eval(input())
if units > 0 and units <= 100:
    bill = units * 1.5
elif units >= 101 and units <= 200:
    bill = units * 2.5
elif units >= 201 and units <= 500:
    bill = units * 4
else:
    bill = units * 6
if s_c == True:
    bill = bill - (bill * 0.10)
if units > 800:
    bill = bill + (bill * 0.05)
print(bill)
#or
units=int(input("enter the value :"))
senior=input("enter the vaule : ").lower()=="senior"
if 0<units<=100:
    bill=units*1.5
elif 100<units<=200:
    bill =units*2.5
elif 200<units<=500:
    bill=units*4
elif 500<units<=800:
    bill=units*6
else:
    bill=units*6*1.05
if senior:
    bill*=0.9
print(bill)

'''
'''seat=input()
booking_days=int(input())
festival=input()
age=int(input())
price=5000
if seat=="Business":
    price=price+(price*0.40)
elif seat=="Premium":
    price=price+(price*0.20)
elif seat=="Economy":
    price=price
if booking_days>30:
    price=price-(price*0.10)
elif booking_days<7:
    price=price+(price*0.25)

if festival=="True":
    price=price+(price*0.20)

if age>=60:
    price=price-(price*0.15)
print(price)
'''
#or
'''
seat=input()
booking_days=int(input())
festival=input()
age=int(input())
price=5000
if seat=="Business":
    price*=1.4
elif seat=="Premium":
    price*=1.20
elif seat=="Economy":
    price=price
if booking_days>30:
    price*=0.90
elif booking_days<7:
    price*=1.25
if festival=="True":
    price*=1.20
if age>60:
    price*=0.85
print(price)
'''
'''premium=10000
age=int(input("Enter the age: "))
health_score=int(input("Enter the score: "))
vehicle_type= input("Enter the type: ")
if age>25:
    premium*=1.2
elif age>=25 or age<=50:
    premium=premium
elif age>50:
    premium*=1.5
if health_score>=80:
    premium*=0.9
elif health_score>=60 or health_score<=79:
    premium=premium
elif health_score<60:
    premium*=1.2
if vehicle_type=="Sports Car":
    premium*=1.3
elif vehicle_type=="SUV":
    premium*=1.5
if vehicle_type=="Sedan":
    premium=premium
print(round(premium))'''

'''Credit_score=int(input("Enter the credit score: "))
Monthly_income=int(input("Enter the income: "))
Existing_liabilities=int(input("Enter the amount: "))
if Credit_score>=750 and Monthly_income>=50000 and Existing_liabilities<=20000:
    print("Approved")
elif 650<=Credit_score<=749 and Monthly_income>=50000 and Existing_liabilities<=20000:
    print("Approved with Conditions")
else:
    print("Rejected")'''\
    
'''salary=int(input("enter the salary: "))
performance_rating=int(input("Enter the rating: "))
experience=int(input("Enter the experience: "))
attendance=int(input("Enter the attendance: "))
bonus=0
#performance rating
if performance_rating==5:
    bonus+=salary*0.25
elif performance_rating==4:
    bonus+=salary*0.15
elif performance_rating==3:
    bonus+=salary*0.1
#Experience
if experience>10:
    bonus+=salary*0.1
elif 5<=experience<=10:
    bonus+=salary*0.05
#attendance
if attendance>=95:
    bonus+=5000
elif attendance>85 or attendance<=94:
    bonus+=2000
print(bonus)'''


'''n=int(input("enter n value: "))
for i in range(1,11):
    print(f"{n}*{i}={n*i}")'''


'''n=int(input("enter n value: "))
c=0
for i in range(1,11):
    r=n*i
    c+=r
print(c)'''

'''n = int(input("Enter n value: "))
print(sum(n * i for i in range(1, 11)))
'''
'''n = int(input("Enter n value: "))
print(n*55)'''

'''n=int(input("Enter the number: "))
rev=0
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
print(rev)
'''
'''start=int(input("Enter starting number: "))
end=int(input("Enter ending number: "))
for n in range(start,end+1):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c==2:
        print(n)
   
'''
'''s=input("Enter the string: ")
v=0
c=0
for ch in s:
    if ch in "AEIOUaeiou":
        v+=1
    else:
        c+=1
print(v)
print(c)'''

s=input("Enter the string: ")
rev=""
for ch in range(len(s)-1,-1,-1):
    rev+=s[ch]
print(rev)













           
