# lambda function
'''greater = lambda a,b:a if a>b else b
print(greater(12,13))
print(greater(22,3))
print(greater(122,103))
print(greater(120,130))'''

'''wish=lambda name: f'welcome to the course {name}'
print(wish("abc"))
print(wish("defg"))
print(wish("hijk"))'''

'''iseven=lambda n: "Even" if n%2==0 else "Odd"
print(iseven(45))
print(iseven(20))
print(iseven(15))'''

'''avg=lambda a,b,c:(a+b+c)/3
print(avg(4,5,6))
print(avg(40,50,60))'''
'''
domain = lambda mail: (mail.split('@')[-1]).split('.')[0]
print(domain('harsha@codegnan.com'))
print(domain('harsha@gmail.com'))
print(domain('harsha@yahoo.com'))'''

'''gst=lambda price:price+price*0.18
print(gst(1000))
print(gst(5000))
print(gst(8000))'''

'''price=[20,30,40,50,60,70]###
gst=0.18
l=[]
for i in range(len(price)):
    l[i]=l[i]+l[i]*gst
    l.append(l[i])
print(l)
    '''
#map()
'''
prices=[20,30,40,50,60,70]
res=list(map(lambda price:price+price*0.18,prices))
print(res)'''

'''names=['abc','def','ghi','jkl','mno']
res=list(map(lambda name:name.title(),names))
print(res)'''

'''prices=[20,30,40,50,60,70]
res=list(map(lambda price:price-price*0.3,prices))
print(res)'''

'''prices=[5678,8765,5467,124,123,1600]
res=list(map(lambda price:price-price*0.3,prices))
print(res)'''

#filter()
'''prices=[5678,8765,5467,124,123,1600]
res=list(filter(lambda price:price>5000,prices))
print(res)'''
'''prices=[5678,8765,5467,124,123,1600]
res=list(filter(lambda price:price%2==0,prices))
print(res)'''
'''
prices=[5678,8765,5467,124,123,1600]
res=list(filter(lambda price:price%2!=0,prices))
print(res)'''

'''names=['abc','defgegh','ghirfjh','jkl','mnopjho']
res=list(filter(lambda name:len(name)>5,names))
print(res)'''
#reduce()
#sum of numbers
from functools import reduce
'''l=[3,567,6,24,124,435,462]
res= reduce(lambda sum,i:sum+i,l)
print(res)
'''
'''
names=['abc','defgegh','ghirfjh','jkl','mnopjho']
res=reduce(lambda name,i:name+" "+i,names)
print(res)
'''
'''
products={"sugar":60,
          "salt":50,
          "eggs":90,
          "cooking oil":120,
          "bread":45}
print(sorted(products))'''
'''
products={"sugar":60,
          "salt":50,
          "eggs":90,
          "cooking oil":120,
          "bread":45}
print(sorted(products.items()))'''
'''
products={"sugar":60,
          "salt":50,
          "eggs":90,
          "cooking oil":120,
          "bread":45}
print(dict(sorted(products.items())))'''
#reverse
'''
products={"sugar":60,
          "salt":50,
          "eggs":90,
          "cooking oil":120,
          "bread":45}
print(dict(sorted(products.items(),reverse=True)))'''
'''
products={"sugar":60,
          "salt":50,
          "eggs":90,
          "cooking oil":120,
          "bread":45}
print(dict(sorted(products.items(),key=lambda i:i[1])))
print(dict(sorted(products.items(),key=lambda i:i[1],reverse=True)))
'''