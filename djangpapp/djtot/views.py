from django.shortcuts import render

from django.http import HttpResponse

from djtot import views

# Create your views here.

def hello(request):  
    return HttpResponse("This is Home Page")  

def abts(r):  
    return HttpResponse("<h2 style='background-color:green;color:white;padding:3px;margin-left:230px'>This is About Page</h2>")      

def image(request):
	return render(request,'home.html')

def login(request):
	return render(request,'login.html')	

def register(request):
	return render(request,'register.html')

def regtask(request):
	return render(request,'regtask.html')

def arth(request):
	return render(request,'arth.html')

def table(request,num):
	l = ""
	for i in range(1,11):
		v = num*i
		l+=str(num)+"*"+str(i)+"="+str(v)+"<br>"
	return HttpResponse(l)	

def myhome(request,name,age):
	return render(request,'myhome.html',{'n':name,'a':age})	

def bttask(request):
	return render(request,'boottask.html')

def myDetails(k,name,age):
	return render(k,'myhome.html',{'n':name,'a':age})
