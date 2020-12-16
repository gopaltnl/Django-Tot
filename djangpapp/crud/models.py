from django.db import models

# Create your models here.
# Create your models here.
class Student(models.Model):
	name=models.CharField(max_length=30)
	rollno=models.CharField(max_length=30)
	age=models.IntegerField()
	mobileno=models.CharField(max_length=30,null=True)
	email=models.EmailField(max_length=30)
	adress=models.TextField(null=True)
	gender=models.CharField(max_length=30,null=True)
	branch=models.CharField(max_length=30,null=True)
	language=models.CharField(max_length=30,null=True)

	def __str__(self):
		return self.name+' '+self.rollno