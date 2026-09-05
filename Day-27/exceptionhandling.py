'''try:
    a=int(input())
except ValueError:
    print("Enter the correct datatype")
else:
    print("a=",a)
finally:
    print("End of the porgram")'''
'''try:
    #a=int(input())
    k={1:12,2:12}
    #print(k[14])
    l=[1,2]
    #print(l[10])
    #print(10/0)
    #print('1'+1)
except ValueError:
    print("Enter the correct datatype")
except KeyError:
    print("key is not there")
except IndexError:
    print("index out of range")
except ZeroDivisionError:
    print("can't divide with zero")
except TypeError:
    print("Enter the correct datatype")
except NameError:
    print("Enter the variable")
else:
    print("error free program")
finally:
    print("End of the porgram")
'''
'''try:
    #a=int(input())
    k={1:12,2:12}
    #print(k[14])
    l=[1,2]
    #print(l[10])
    #print(10/0)
    #print('1'+1)
except [ValueError,KeyError,IndexError,ZeroDivisionError,TypeError,NameError]:
    print("Error occured",e)
else:
    print("error free program")
finally:
    print("End of the porgram")'''

#k={1:12,2:12}
#print(k[14])
#l=[1,2]
#print(l[10])
#print(10/0)
#print('1'+1)
#print(a)

'''try:
    a=int(input())
except ValueError:
    print("Enter the correct datatype")
else:
    print("a=",a)
finally:
    print("End of the porgram")'''
'''try:
    #a=int(input())
    k={1:12,2:12}
    #print(k[14])
    l=[1,2]
    #print(l[10])
    #print(10/0)
    #print('1'+1)
except ValueError:
    print("Enter the correct datatype")
except KeyError:
    print("key is not there")
except IndexError:
    print("index out of range")
except ZeroDivisionError:
    print("can't divide with zero")
except TypeError:
    print("Enter the correct datatype")
except NameError:
    print("Enter the variable")
else:
    print("error free program")
finally:
    print("End of the porgram")
'''
'''try:
    a=int(input())
    k={1:12,2:12}
    #print(k[14])
    l=[1,2]
    #print(l[10])
    #print(10/0)
    #print('1'+1)
except Exception as e:
    print("Error occured",e)
else:
    print("error free program")
finally:
    print("End of the porgram")'''

try:
    amount=int(input("Enter the account: "))
    balance=5000
    if amount<0:
        raise Exception("Account need to be positive")
except Exception as e:
    print("Error occured",e)
else:
    print("error free program")
finally:
    print("End of the porgram")
