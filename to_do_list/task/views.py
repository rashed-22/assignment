from django.shortcuts import render, redirect
from task.forms import TaskForm
from task.models import TaskModel

# Create your views here.


def add_tasks(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showtasks')
    else:
        form = TaskForm()
    return render(request, 'add_tasks.html', {'form': form})

def show_tasks(request):
    task = TaskModel.objects.filter(is_completed=False)
    print(task)
    return render(request,'show_tasks.html', {'tasks': task})

def edit_task(request, id):
    task = TaskModel.objects.get(pk=id)
    form = TaskForm(instance= task)
    if request.method == "POST":
        form = TaskForm(request.POST, instance= task)
        if form.is_valid():
            form.save()
            return redirect('showtasks')
    return render(request,'add_tasks.html', {'form': form})


def delete_task(request, id):
    task = TaskModel.objects.get(pk=id)
    task.delete()
    return redirect('showtasks')


def complete_tasks(request, id):
    task = TaskModel.objects.get(pk=id)
    task.is_completed = True
    task.save()
    print(task)
    return redirect('completedtasks')

def completed_tasks(request):
    task = TaskModel.objects.filter(is_completed=True)
    return render(request,'completed_tasks.html', {'tasks': task})