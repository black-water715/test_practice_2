from django.shortcuts import render, redirect

from .models import *
from .forms import * 

def index(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid(): 
            form.save() 
        return redirect('/')
    
    context = {
        'tasks':tasks,
        'form':form,
    }
    template_name = 'app/list.html'
    return render(request, template_name,context )

def updateTask(request, pk):
    task=Task.objects.get(id=pk)
    form=TaskForm(instance=task)
    context = {
        'form':form,
    }
    if request.method == "POST":
        form = TaskForm( request.POST, instance=task)
        if form.is_valid(): 
            form.save() 
            return redirect('/')

    template_name='app/update_task.html'
    return render(request, template_name, context)

def deleteTask(request, pk):
    item=Task.objects.get(id=pk)
    template_name = 'app/delete.html'
    context = {
        'item':item,
    }
    if request.method == "POST":
        item.delete()
        return redirect('/')
    
    return render(request, template_name, context)