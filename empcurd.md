

C:\Users\Gopal-APSSDC\Music\DJango-Tot\djangotot\djangpapp>python manage.py shell
Python 3.6.8 (tags/v3.6.8:3c6b436a57, Dec 23 2018, 23:31:17) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from empcurd.models import Employee
>>>
>>> C:\Users\Gopal-APSSDC\Music\DJango-Tot\djangotot\djangpapp>python manage.py shell
  File "<console>", line 1
    C:\Users\Gopal-APSSDC\Music\DJango-Tot\djangotot\djangpapp>python manage.py shell
>>> temp=Employee(empid='01',empname='gopi',empsal=20000,empdept="apssdc")
>>> temp.save()
>>> temp=Employee(empid='08',empname='anil',empsal=30000,empdept="skillapssdc")
>>> temp.save()
  
  ![screen](https://user-images.githubusercontent.com/51777024/101928446-99513c00-3bfb-11eb-887d-fa8dba236ac6.png)


C:\Users\Gopal-APSSDC\Music\DJango-Tot\djangotot\djangpapp>python manage.py shell
Python 3.6.8 (tags/v3.6.8:3c6b436a57, Dec 23 2018, 23:31:17) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from empcurd.models import Employee
>>>

Microsoft Windows [Version 10.0.18363.1198]
(c) 2019 Microsoft Corporation. All rights reserved.

C:\Users\Gopal-APSSDC\Music\DJango-Tot\djangotot\djangpapp>py manage.py shell
Python 3.6.8 (tags/v3.6.8:3c6b436a57, Dec 23 2018, 23:31:17) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)

>>> from empcurd.models import Employee
>>> temp=Employee(empid='12',empsal=30000,empdept='sacet')
>>> temp.save()
>>> temp

>>> obj=Employee.objects.all()
>>> obj 

>>> obj=Employee.objects.all()
>>> for i in obj:

print(i.empname)
...
gopi
Sai
Shiva
pavankumar
anil
varma
varma

>>> for i in obj:
...     print(i.empid)
...
1
3
4
7
8
9
10
12
>>> for i in obj:
...     print(i.empdept)
...
apssdc
Android@gmail.com
Python@gmail.com
pavan@gmail.com
skillapssdc
PMKVY
PMKVY
sacet
>>> obj=Employee.objects.values()
>>> obj
<QuerySet [{'empid': 1, 'empname': 'gopi', 'empsal': 20000, 'empdept': 'apssdc'}, {'empid': 3, 'empname': 'Sai', 'empsal': 25000, 'empdept': 'Android@gmail.com'}, {'empid': 4, 'empname': 'Shiva', 'empsal': 28000, 'empdept': 'Python@gmail.com'}, {'empid': 7, 'empname': 'pavankumar', 'empsal': 30000, 'empdept': 'pavan@gmail.com'}, {'empid': 8, 'empname': 'anil', 'empsal': 30000, 'empdept': 'skillapssdc'}, {'empid': 9, 'empname': 'varma', 'empsal': 20000, 'empdept': 'PMKVY'}, {'empid': 10, 'empname': 'varma', 'empsal': 20000, 'empdept': 'PMKVY'}, {'empid': 12, 'empname': '', 'empsal': 30000, 'empdept': 'sacet'}]>
>>> obj=Employee.objects.values_list()
>>> obj
<QuerySet [(1, 'gopi', 20000, 'apssdc'), (3, 'Sai', 25000, 'Android@gmail.com'), (4, 'Shiva', 28000, 'Python@gmail.com'), (7, 'pavankumar', 30000, 'pavan@gmail.com'), (8, 'anil', 30000, 'skillapssdc'), (9, 'varma', 20000, 'PMKVY'), (10, 'varma', 20000, 'PMKVY'), (12, '', 30000, 'sacet')]>
>>> obj=Employee.objects.values('empid','empsal')
>>> obj
<QuerySet [{'empid': 1, 'empsal': 20000}, {'empid': 3, 'empsal': 25000}, {'empid': 4, 'empsal': 28000}, {'empid': 7, 'empsal': 30000}, {'empid': 8, 'empsal': 30000}, {'empid': 9, 'empsal': 20000}, {'empid': 10, 'empsal': 20000}, {'empid': 12, 'empsal': 30000}]>
>>> obj=Employee.objects.values('empid','empdept')
>>> obj
<QuerySet [{'empid': 1, 'empdept': 'apssdc'}, {'empid': 3, 'empdept': 'Android@gmail.com'}, {'empid': 4, 'empdept': 'Python@gmail.com'}, {'empid': 7, 'empdept': 'pavan@gmail.com'}, {'empid': 8, 'empdept': 'skillapssdc'}, {'empid': 9, 'empdept': 'PMKVY'}, {'empid': 10, 'empdept': 'PMKVY'}, {'empid': 12, 'empdept': 'sacet'}]>
>>> obj=Employee.objects.values_list('empid')
>>> obj
<QuerySet [(1,), (3,), (4,), (7,), (8,), (9,), (10,), (12,)]>
TypeError: must be str, not int
>>> i=Employee.objects.get(empid=10)
>>> i.delete()
(1, {'empcurd.Employee': 1})
>>> data=Employee.objects.get(empname='gopi')
>>> data

