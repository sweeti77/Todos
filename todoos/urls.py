"""todoos URL Configuration

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
from django.urls import path

from Authentication import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('mainPage', views.mainPage, name='mainPage'),
    path('createTodo', views.createTodo, name='createTodo'),
    path('updateTodo/<int:todo_pk>', views.updateTodo, name='updateTodo'),
    path('updateTodo/<int:todo_pk>/complete', views.completeTodo, name='completeTodo'),
    path('updateTodo/<int:todo_pk>/delete', views.deleteTodo, name='deleteTodo'),
    path('completedTodo', views.completed, name="completed"),

    #Authentication
    path('signupUser', views.signupUser, name='signupUser'),
    path('loginUser', views.loginUser, name='loginUser'),
    path('logoutUser', views.logoutUser, name='logoutUser'),

]
