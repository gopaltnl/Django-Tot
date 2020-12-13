from django.urls import path

from .views import addstudent

from .views import read


urlpatterns = [

	path('addstudent/',addstudent),

	path('read/',read),

]