from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError

from django.utils import timezone

from .models import Todo

from .forms import TodoForm


# Create your views here.

def index(request):
    return render(request, 'index.html')

def mainPage(request):
    obj = Todo.objects.filter(user=request.user, completed__isnull=True)
    return render(request, 'mainPage.html', {'todos':obj})


def createTodo(request):
    if request.method == 'GET':
        return render(request, 'createTodo.html', {'form':TodoForm()})

    else:
        try:
            form = TodoForm(request.POST)
            newTodo = form.save(commit=False)
            newTodo.user = request.user
            newTodo.save()
            return redirect('mainPage')
        except ValueError:
            return render(request, 'createTodo.html',
                          {'form': TodoForm(), 'error': 'Bad Input. Try Again'})


def updateTodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'GET':
        form = TodoForm(instance=todo)
        return render(request, 'updateTodo.html', {'form':form, 'todo':todo})
    else:
        try:
            form = TodoForm(request.POST, instance=todo)
            form.save()
            return redirect('mainPage')
        except ValueError:
            return render(request, 'updateTodo.html',
                          {'form': form, 'error': 'Bad Input. Try Again', 'todo':todo })

def completeTodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        todo.completed = timezone.now()
        todo.save()
        return redirect('mainPage')

def deleteTodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        todo.delete()
        return redirect('mainPage')

def completed(request):
    obj = Todo.objects.filter(user=request.user, completed__isnull=False)
    return render(request, 'completed.html', {'todos':obj})





def signupUser(request):
    if request.method == 'POST':
        # create new user
        try:
            if request.POST['password1'] == request.POST['password2']:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save
                login(request, user)
                return redirect('mainPage')
            else:
                return render(request, 'signup.html',
                              {'form': UserCreationForm(), 'error': "Passwords didnot match. TRY AGAIN"})
        except IntegrityError:
            return render(request, 'signup.html',
                          {'form': UserCreationForm(), 'error': "UserName already taken.PLEASE Use another username"})

    else:
        return render(request, 'signup.html', {'form': UserCreationForm()})

def logoutUser(request):
    if request.method == "POST":
        logout(request)
    return redirect('index')

def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is None:
            return render(request, 'login.html',
                              {'form': AuthenticationForm(), 'error': "Bad Inputs.Try Again"})

        else:
            login(request, user)
            return redirect('mainPage')

    else:
        return render(request, 'login.html', {'form': AuthenticationForm()})
