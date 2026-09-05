Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#dictonary operations
data={'name':'harsha','batch':'63','course':'PFS'}
data['name']
'harsha'
data['batch']
'63'
data={'name':'harsha','batch':63,'course':'PFS'}
data['batch']
63
data['course']
'PFS'
63 in data
False
data['age']
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    data['age']
KeyError: 'age'
data.get('age','key is not present')
'key is not present'
data.get('course','key is not present')
'PFS'
data['batch']=64
data
{'name': 'harsha', 'batch': 64, 'course': 'PFS'}
data['skills']:['python','sql','flask']
data['skills']=['python','sql','flask']
data
{'name': 'harsha', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'sql', 'flask']}
data['age']=21
data
{'name': 'harsha', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'sql', 'flask'], 'age': 21}
data.update({'phno':96543234521,'email':'harsha@gmail.com'})
data
{'name': 'harsha', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'sql', 'flask'], 'age': 21, 'phno': 96543234521, 'email': 'harsha@gmail.com'}
data.pop('age')
21
data.pop('phno')
96543234521
data
{'name': 'harsha', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'sql', 'flask'], 'email': 'harsha@gmail.com'}
data.del['name']
SyntaxError: invalid syntax
del data['name']
data
{'batch': 64, 'course': 'PFS', 'skills': ['python', 'sql', 'flask'], 'email': 'harsha@gmail.com'}
data.popitem()
('email', 'harsha@gmail.com')
data
{'batch': 64, 'course': 'PFS', 'skills': ['python', 'sql', 'flask']}
data.popitem()
('skills', ['python', 'sql', 'flask'])
data
{'batch': 64, 'course': 'PFS'}
data.clear()
data
{}
data={'name': 'harsha', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'sql', 'flask'], 'age': 21, 'phno': 96543234521, 'email': 'harsha@gmail.com'}
data
SyntaxError: multiple statements found while compiling a single statement
data
{}
d={'name': 'harsha', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'sql', 'flask'], 'age': 21, 'phno': 96543234521, 'email': 'harsha@gmail.com'}
d
SyntaxError: multiple statements found while compiling a single statement
data={'name': 'harsha', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'sql', 'flask'], 'age': 21, 'phno': 96543234521, 'email': 'harsha@gmail.com'}
data
{'name': 'harsha', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'sql', 'flask'], 'age': 21, 'phno': 96543234521, 'email': 'harsha@gmail.com'}
data.keys()
dict_keys(['name', 'batch', 'course', 'skills', 'age', 'phno', 'email'])
data.values()
dict_values(['harsha', 64, 'PFS', ['python', 'sql', 'flask'], 21, 96543234521, 'harsha@gmail.com'])
data.items()
dict_items([('name', 'harsha'), ('batch', 64), ('course', 'PFS'), ('skills', ['python', 'sql', 'flask']), ('age', 21), ('phno', 96543234521), ('email', 'harsha@gmail.com')])
sorted(data)
['age', 'batch', 'course', 'email', 'name', 'phno', 'skills']
sorted(data,reverse=True)
['skills', 'phno', 'name', 'email', 'course', 'batch', 'age']
max(data)
'skills'
min(data)
'age'
data
{'name': 'harsha', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'sql', 'flask'], 'age': 21, 'phno': 96543234521, 'email': 'harsha@gmail.com'}
data['age']
21
data.get('age')
21
del data['age']
data
{'name': 'harsha', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'sql', 'flask'], 'phno': 96543234521, 'email': 'harsha@gmail.com'}
data['age']
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    data['age']
KeyError: 'age'
data.get('age')
data
{'name': 'harsha', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'sql', 'flask'], 'phno': 96543234521, 'email': 'harsha@gmail.com'}
max(data)
'skills'
min(data)
'batch'
len(data)
6
any(data)
True
>>> all(data)
True
>>> #cpoy-creates a shallow copy
>>> a={1:1,2:2,3:3}
>>> b=a
>>> b[4]=4
>>> b
{1: 1, 2: 2, 3: 3, 4: 4}
>>> a
{1: 1, 2: 2, 3: 3, 4: 4}
>>> c=a.copy()
>>> a
{1: 1, 2: 2, 3: 3, 4: 4}
>>> b
{1: 1, 2: 2, 3: 3, 4: 4}
>>> #setdefault()-whenever their is no data we use to set key with the default
>>> data.setdefault('age',0)
0
>>> data
{'name': 'harsha', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'sql', 'flask'], 'phno': 96543234521, 'email': 'harsha@gmail.com', 'age': 0}
>>> c=a.copy()
>>> c[4]=4
>>> c
{1: 1, 2: 2, 3: 3, 4: 4}
>>> a
{1: 1, 2: 2, 3: 3, 4: 4}
>>> c=a.copy()
>>> c[5]=5
>>> c
{1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
>>> a
{1: 1, 2: 2, 3: 3, 4: 4}
>>> d=dict.fronkeys(["a","b"],0)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    d=dict.fronkeys(["a","b"],0)
AttributeError: type object 'dict' has no attribute 'fronkeys'. Did you mean: 'fromkeys'?
>>> d=dict.fromkeys(["a","b"],0)
>>> d
{'a': 0, 'b': 0}
