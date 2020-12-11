

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
