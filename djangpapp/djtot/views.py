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