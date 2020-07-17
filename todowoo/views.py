from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import TodoForm
from .models import Todo
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.core.validators import validate_email

def todowoohome(request):
    return render(request, 'todowoo/todowoohome.html')

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'todowoo/signupuser.html', {'form':UserCreationForm()})
    else:
        emailId = request.POST['emailid'].strip()
        password1 = request.POST['password1'].strip()
        print(emailId)
        try:
            if emailId == "":
                return render(request, 'todowoo/signupuser.html', {'form':UserCreationForm(), 'error':"Email id can't be blank!"})
            validate_email(emailId)
        except:
            return render(request, 'todowoo/signupuser.html', {'form':UserCreationForm(), 'error':'Email format is not correct!'})

        if request.POST['password1'] == request.POST['password2']:
            #Create a new user
            try:
                validate_password(password1)
            except:
                return render(request, 'todowoo/signupuser.html', {'form':UserCreationForm(), 'error':'Password should meet the policy creteria!<ul><li>Your password can’t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can’t be a commonly used password.</li><li>Your password can’t be entirely numeric.</li></ul>'})

            try:
                user = User.objects.create_user(request.POST['username'],emailId, password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('todowoo:currenttodos')
            except IntegrityError:
                return render(request, 'todowoo/signupuser.html', {'form':UserCreationForm(), 'error':'User name is not available, please try with another user name'})

        else:
            return render(request, 'todowoo/signupuser.html', {'form':UserCreationForm(), 'error':'Passwords did not match'})

def currenttodos(request):
    todos = Todo.objects.filter(user = request.user, datecompleted__isnull = True, deleteTodoOrNot = False)
    return render(request, 'todowoo/currenttodos.html',{'todos': todos})

@login_required
def logoutuser(request):
    if request.method=="POST":
        logout(request)
        return redirect('todowoo:loginuser')

def loginuser(request):
    # try:
    #     request.user.is_authenticated()
    #     return redirect('currenttodos')
    # except TypeError:
    if request.method == 'GET':
        return render(request, 'todowoo/loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'todowoo/loginuser.html', {'form':AuthenticationForm(), 'error': 'User name and password did not match'})
        else:
            login(request, user)
            return redirect('todowoo:currenttodos')

@login_required
def createtodo(request):
    if request.method=="GET":
        return render(request, 'todowoo/createtodo.html', {'form':TodoForm()})
    else:
        try:
            form=TodoForm(request.POST)
            newtodo = form.save(commit=False)
            newtodo.user = request.user
            newtodo.save()
            return redirect('todowoo:currenttodos')
        except ValueError:
            return render(request, 'todowoo/createtodo.html', {'form':TodoForm(), 'error':'Bad data passed in, Try again'})

@login_required
def viewtodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk = todo_pk, user=request.user, deleteTodoOrNot = False)
    if request.method=="GET":
        form = TodoForm(instance = todo)
        return render(request, 'todowoo/viewtodo.html',{'todo': todo, 'form':form})
    else:
        try:
            form=TodoForm(request.POST, instance=todo)
            form.save()
            return redirect('todowoo:currenttodos')
        except ValueError:
            return render(request, 'todowoo/viewtodo.html',{'todo': todo, 'form':form, 'error': 'Bad info passed in, try again'})

@login_required
def completetodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk = todo_pk, user=request.user, deleteTodoOrNot = False)
    if request.method=="POST":
        todo.datecompleted = timezone.now()
        todo.save()
        return redirect('todowoo:currenttodos')

@login_required
def deletetodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk = todo_pk, user=request.user)
    if request.method=="POST":
        todo.deleteTodoOrNot = True
        todo.save()
        # todo.delete()
        return redirect('todowoo:currenttodos')
    else:
        todo.deleteTodoOrNot = False

@login_required
def completedtodos(request):
    todos = Todo.objects.filter(user = request.user, datecompleted__isnull = False, deleteTodoOrNot = False).order_by('-datecompleted')
    return render(request, 'todowoo/completedtodos.html',{'todos': todos})
