from django.db import models

# Create your models here.

class Employee(models.Model):
	
	empid = models.IntegerField(primary_key=True)  # AutoField?

	empname=models.CharField(max_length=30)

	empsal=models.IntegerField()

	empdept=models.EmailField(max_length=30)

	# address=models.TextField(null=True)


	def __str__(self):
		
		return self.empname+''+self.empsal
