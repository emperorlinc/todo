from .models import Todo
from .forms import TodoForm
from django.db.models import Q
from django.contrib import messages
from .decorators import already_login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
@already_login
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username").lower()
        password = request.POST.get("password")
        try:
            user = User.objects.get(username=username)
        except:
            messages.info(request, "Username seem incorrect")
            return redirect("login")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
            messages.success(request, f"{user.username} is logged-in successfully")
        else:
            messages.error(request, "User does not exist")
            return redirect("login")
    return render(request, "app/login.html")

@login_required(login_url="login")
def logout_view(request):
    logout(request)
    return redirect("login")

@already_login
def register_view(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect("index")
            messages.success(request, "User created successfully")
        else:
            messages.info(request, "Something went wrong")
            return redirect("register")
    return render(request, "app/register.html", {"form": form})

@login_required(login_url="login")
def index_view(request):
    q = request.GET.get("q") if request.GET.get("q") != None else ""
    todos = Todo.objects.filter(
        host=request.user, title__icontains=q
    )
    count = todos.filter(complete=False).count()
    page = request.GET.get("page")
    paginator = Paginator(todos, 5)
    try:
        todos = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        todos = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        todos = paginator.page(page)

    context = {"todos": todos, "paginator": paginator, "count": count, "q": q}
    return render(request, "app/index.html", context)

@login_required(login_url="login")
def create_view(request):
    form = TodoForm()
    if request.method == "POST":
        todo = TodoForm(request.POST)
        if todo.is_valid():
            form = todo.save(commit=False)
            form.host = request.user
            form.save()
            return redirect("index")
    context = {"form": form}
    return render(request, "app/create.html", context)

@login_required(login_url="login")
def edit_view(request, pk):
    todo = Todo.objects.get(id=pk)
    form = TodoForm(instance=todo)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect("index")
        else:
            messages.error(request, "Invalid input")
            return redirect("edit")
    context = {"form": form}
    return render(request, "app/edit.html", context)

@login_required(login_url="login")
def delete_view(request, pk):
    todo = Todo.objects.get(id=pk)
    if request.method == "POST":
        todo.delete()
        return redirect("index")
    context = {"obj": todo}
    return render(request, "app/delete.html", context)
