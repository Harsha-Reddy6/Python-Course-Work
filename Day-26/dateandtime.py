#datetime
from datetime import date,time,datetime,timedelta
'''today=date.today()
print(today)
print(today.day)
print(today.month)
print(today.year)
print(today.weekday())'''

'''from datetime import date,time,datetime,timedelta
year,month,dt=list(map(int,input("[YYYY-MM-DD]").split("-")))
print(date(year,month,dt))'''

'''
t=time(23,6,5)
print(t)
print(t.hour)
print(t.minute)
print(t.second)'''
'''
n=datetime.now()
print(n)
print(n.strftime('%D-%M-%y'))
print(n.strftime('%d-%m-%Y %H:%M:%S'))
print(n.strftime('%d-%m-%Y %H:%M:%S'))
print(n.strftime('%d-%m-%Y %H:%M:%S %p'))
print(n.strftime('%d-%b-%Y %H:%M:%S %p'))
print(n.strftime('%d-%B-%Y %H:%M:%S %p'))
print(n.strftime('%a, %m %Y %H:%M:%S %p'))
print(n.strftime('%A, %m %Y %H:%M:%S %p'))
'''
'''
n=datetime.now()
print(n)
print(n.day)
print(n.month)
print(n.year)
print(n.weekday())
print(n)
print(n.hour)
print(n.minute)
print(n.second)
print(n.strftime('%D-%M-%y'))
print(n.strftime('%d-%m-%Y %H:%M:%S'))
print(n.strftime('%d-%m-%Y %H:%M:%S'))
print(n.strftime('%d-%m-%Y %H:%M:%S %p'))
print(n.strftime('%d-%b-%Y %H:%M:%S %p'))
print(n.strftime('%d-%B-%Y %H:%M:%S %p'))
print(n.strftime('%a, %m %Y %H:%M:%S %p'))
print(n.strftime('%A, %m %Y %H:%M:%S %p'))
'''
t=date.today()
n=datetime.now()
t7=t+timedelta(days=7)
t5=t-timedelta(days=5)
n15=n+timedelta(minutes=15)
print(t,t7)
print(t5)
print(n,n15)



