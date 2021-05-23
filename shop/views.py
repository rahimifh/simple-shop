from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import TodoForm, userdetals,orders
from .models import Todo, stuff,userdetail,order
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
# Create your views here.

def home(request):
    stuffs = stuff.objects.all()
    return render(request, 'shop/home.html',{'stuffs':stuffs})


def signupuser(request):

    if request.method== 'GET':

        return render(request,'shop/signupuser.html', {'form':UserCreationForm()})
    else:
        #create a new user
        if request.POST['password1']==request.POST['password2']:
            try:
               user=User.objects.create_user(request.POST['username'], password=request.POST['password1'])
               user.save()
               login(request,user)
               return redirect('currenttodos')
            except IntegrityError:
                return render(request,'shop/signupuser.html', {'form':UserCreationForm(),'error':'That username has already been taken. please choose new one'})

        else:
            return render(request,'shop/signupuser.html', {'form':UserCreationForm(),'error':'passwords did not match'})
            #tell the user the password didn't match

@login_required
def logoutuser (request):
    if request.method == 'POST':
            logout(request)
            return redirect('home')

@login_required
def createtodo(request):
    todos = order.objects.filter(user = request.user)
    con = order.objects.filter(user = request.user).count()

    stuffs = stuff.objects.all()
    if request.method == 'GET':
        return render(request,'shop/createtodo.html', {'form':userdetals, 'todos':todos, 'con':con })
    else:
        try:
            form = userdetals(request.POST)
            newtodo = form.save(commit=False)
            newtodo.user = request.user
            newtodo.save()
            return redirect('currenttodos')
        except ValueError:
            return render(request,'shop/createtodo.html', {'form':userdetals, 'error': 'extra word in title'})

@login_required
def deleteitme (request, id):
    obj = order.objects.filter(id=id)
    if request.method == "POST":
        obj.delete()
        return redirect ('createtodo')

def loginuser (request):
        if request.method== 'GET':

            return render(request,'shop/loginuser.html', {'form':AuthenticationForm()})
        else:
            user = authenticate(request, username=request.POST['username'],password=request.POST['password'])
            if user is None:
                return render(request,'shop/signupuser.html', {'form':AuthenticationForm(),'error':'username or password is unvalid'}, )
            else:
               login(request,user)
               return redirect('currenttodos')
@login_required
def currenttodos (request):
    con = order.objects.filter(user = request.user).count()

    stuffs = stuff.objects.all()
    if request.method == 'GET':
            return render(request,'shop/currenttodos.html', {'stuffs': stuffs, 'orderform':orders, 'con': con})
    else:
        try:
            form = orders(request.POST)
            newtodo = form.save(commit=False)
            newtodo.user = request.user
            newtodo.save()
            return redirect('currenttodos')
        except ValueError:
            return render(request,'shop/createtodo.html', {'stuffs': stuffs, 'orderform':orders,'con': con, 'error': 'extra word in title'})



@login_required
def viewtodo (request, todo_pk):
    todo = get_object_or_404(Todo, pk = todo_pk, user =request.user)
    if request.method =='GET':
        form = TodoForm(instance = todo)
        return render(request,'shop/viewtodo.html', {'todo': todo, 'form': form })
    else:
        try:
            form = TodoForm(request.POST, instance = todo)
            form.save()
            return redirect('currenttodos')
        except ValueError:
            return render(request,'shop/viewtodo.html', {'todo': todo, 'form': form, 'error':'Bad info' })
@login_required
def completetodo (request, todo_pk):
    todo = get_object_or_404(Todo, pk = todo_pk, user =request.user)
    if request.method =='POST':
        todo.datecompleted = timezone.now ()
        todo.save()
        return redirect('currenttodos')

@login_required
def Deleteitem (request, todo_pk):
    todo = get_object_or_404(Todo, pk = todo_pk, user =request.user)
    if request.method =='POST':
        todo.delete()
        return redirect('currenttodos')
@login_required
def completedtodos (request):
    con = order.objects.filter(user = request.user).count()
    stuffs = stuff.objects.all()
    todos = userdetail.objects.filter(user = request.user)
    return render(request,'shop/completedtodos.html', {'todos': todos, 'con':con})

# Create your views here.
