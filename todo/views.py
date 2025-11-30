# todo/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm 

# --- 1. READ & CREATE (Index View) ---
def index(request):
    
    # 🌟 FIX: This line MUST be the first thing executed to ensure 
    # the 'tasks' variable is defined before context is created.
    tasks = Task.objects.all().order_by('-created_at')

    form = TaskForm() 

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        
        # Redirect uses the URL name 'list' defined in urls.py
        return redirect('list') 

    # This context dictionary now safely accesses the defined 'tasks' variable.
    context = {'tasks': tasks, 'form': form} 
    
    # Using the recommended namespaced template path
    return render(request, 'todo/index.html', context)

# --- 2. UPDATE (Edit View) ---
# Note: You need to import get_object_or_404 above
def updateTask(request, pk):
    task = get_object_or_404(Task, id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('list') 
    
    context = {'form': form, 'task': task}
    return render(request, 'todo/update_task.html', context)

# --- 3. DELETE (Confirmation View) ---
def deleteTask(request, pk):
    item = get_object_or_404(Task, id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('list')

    context = {'item': item}
    return render(request, 'todo/delete.html', context)