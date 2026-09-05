#fileoperations
#read mode
'''file=open('pfs-63.txt','r')
print(file.read())
file.seek(0)
print(file.readline())
file.seek(10)
print(file.readlines())
file.close()'''
         #or
'''with open('pfs-63.txt','r') as file:
    print(file.read())
    file.seek(0)
    print(file.readline())
    file.seek(0)
    print(file.readlines())
'''
#write mode
'''with open("mysql.txt",'w') as file:
    file.write("DDl,DML,DQl")  # file is created
    '''
'''with open("pfs-63.txt",'w') as file: # it overwrites the content which is having in the file 
    file.write("shifted to branc-1. ")'''
#append mode
'''with open("pfs-63.txt",'a') as file: # it adds the content at the end of the file 
    file.write("only for today")'''
#append and read =>a+
'''with open("pfs-63.txt",'a+') as file: 
    file.write("tom same branch 5 ")
    file.seek(0)
    print(file.read())'''
with open("pfs-63.txt",'r+') as file: 
    file.write("tom same branch 5 ")
    file.seek(0)
    print(file.read())