# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from .models import Task


def index(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks': tasks})


def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        new_task = Task(title=title)
        new_task.save()
        return redirect('index')
    return render(request, 'add_task.html')


def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = True
    task.save()
    return redirect('index')


def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('index')

# Create your views here.
