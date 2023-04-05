# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect, HttpResponseBadRequest, JsonResponse
from django.shortcuts import render, redirect
from .models import Task


def index(request):
    tasks = []
    if request.method == 'POST':
        title = request.POST['title']
        task = Task(title=title)
        task.save()
        tasks = Task.objects.all()
        # Ajouter la tâche à la liste des tâches dans la session
        request.session.setdefault('task_list', []).append({'id': task.id, 'title': title, 'completed': False})
    else:
        # Si la liste des tâches existe déjà dans la session, l'afficher
        if 'task_list' in request.session:
            for t in request.session['task_list']:
                tasks.append(Task(id=t['id'], title=t['title'], completed=t['completed']))
        else:
            tasks = Task.objects.all()

    return render(request, 'index.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title', '')
        if title:
            task = Task.objects.create(title=title)
            return JsonResponse({'id': task.id, 'title': task.title, 'completed': task.completed})
        else:
            return JsonResponse({'error': 'Title cannot be empty.'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid method.'}, status=405)



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
