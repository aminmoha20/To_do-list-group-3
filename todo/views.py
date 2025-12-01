# todo/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

from .models import Task
from .forms import TaskForm


# -----------------------------
# TASK VIEWS
# -----------------------------

@login_required(login_url='login')
def index(request):
    # Only show tasks for logged-in user
    tasks = Task.objects.filter(user=request.user)

    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.user = request.user  # link task to the logged-in user
            new_task.save()
            return redirect('index')

    context = {'tasks': tasks, 'form': form}
    return render(request, 'todo/index.html', context)


@login_required(login_url='login')
def update_task(request, pk):
    task = get_object_or_404(Task, id=pk, user=request.user)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'form': form, 'task': task}
    return render(request, 'todo/update_task.html', context)


@login_required(login_url='login')
def delete_task(request, pk):
    task = get_object_or_404(Task, id=pk, user=request.user)

    if request.method == 'POST':
        task.delete()
        return redirect('index')

    context = {'item': task}
    return render(request, 'todo/delete.html', context)


@login_required(login_url='login')
def toggle_complete(request, pk):
    task = get_object_or_404(Task, id=pk, user=request.user)
    task.complete = not task.complete
    task.save()
    return redirect('index')


# -----------------------------
# AUTH VIEWS
# -----------------------------

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'todo/login.html')


def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password != password2:
            messages.error(request, "Passwords do not match.")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
        else:
            user = User.objects.create_user(username=username, password=password)
            auth_login(request, user)  # log in automatically
            return redirect('index')

    return render(request, 'todo/register.html')
