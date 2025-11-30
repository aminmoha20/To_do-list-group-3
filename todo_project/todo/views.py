
# todo/views.py
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm # We will create this form next!

# The main view to show the list of tasks
def index(request):
    tasks = Task.objects.all() # Fetch all tasks from the database

    form = TaskForm() # Initialize an empty form

    # Handle the submission of a new task
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/') # Redirect back to the index page

    context = {'tasks': tasks, 'form': form}
    return render(request, 'todo/index.html', context)

# View to update an existing task
def updateTask(request, pk):
    task = Task.objects.get(id=pk) # Get the specific task by its primary key (pk)
    
    # Populate the form with the existing task data
    form = TaskForm(instance=task)

    if request.method == 'POST':
        # Overwrite the instance with the new data from the POST request
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {'form': form}
    return render(request, 'todo/update_task.html', context)

# View to delete a task
def deleteTask(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item': item}
    return render(request, 'todo/delete.html', context)
