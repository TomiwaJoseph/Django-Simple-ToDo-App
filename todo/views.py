from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from django.contrib import messages

# Create your views here.
def home(request):
    to_do = Todo.objects.order_by('-date_created')
    context = {
        'to_do': to_do
    }
    return render(request, 'todo/home.html', context)


def add(request):
    todo = request.POST.get('task')
    Todo.objects.create(task=todo)
    messages.success(request, 'Task added successfully.')
    return redirect('home')


def delete(request, id):
    task = get_object_or_404(Todo, id=id)
    task.delete()
    messages.success(request, 'Task deleted successfully.')
    return redirect('home')


def update(request):
    updated_task = request.POST.get('task')
    cur_id = request.POST.get('id')
    to_do = get_object_or_404(Todo, id=cur_id)
    to_do.task = updated_task
    to_do.save()
    messages.success(request, 'Task updated successfully.')
    return redirect('home')

