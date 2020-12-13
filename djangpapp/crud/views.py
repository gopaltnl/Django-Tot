from django.shortcuts import render

from django.http import HttpResponse

from .models import Student

# Create your views here.

def addstudent(request):
	# if request.method="POST":
	#	i=request.POST.get("id")
	#	n=request.POST.get("name")
		#r=request.POST.get("rollno")
		#a=request.POST.get("mobileno")
		#e=request.POST.get("email")

	return render(request,'crud/addstudent.html')



def read(request):

	return render(request,'crud/read.html')
