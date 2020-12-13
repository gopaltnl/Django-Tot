"""djangpapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from djtot import views
from djtot import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello), 
    path('about/', views.abts), 
    path('image/',views.image),
    path('login/',views.login),
    path('register/',views.register),
    path('arth/',views.arth),
    path('regtask/',views.regtask),
    path('table/<int:num>/',views.table),
    path('task/',v.bttask),
    path('details/<str:name>/<int:age>',views.myDetails),
    
    path('crud/',include('crud.urls')),

    path('empcurd/',include('empcurd.urls')),
 
]
