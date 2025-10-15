from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import taskInfo

# Create your views here.
def index(request):
    task_list = taskInfo.objects.all()
    context = {
        'tasks': task_list
        }

    return render(request, 'task/index.html', context)

def createTask(request):
    completed = request.POST.get('completed') == 'on'
    newTask = taskInfo(
        name = request.POST['name'],
        date = request.POST['date'],
        description = request.POST['description'],
        completed = completed
    )

    newTask.save()

    return HttpResponseRedirect(reverse("task:index"))

def deleteTask(request, task_id):
    taskDeleted = taskInfo.objects.get(id=task_id)
    taskDeleted.delete()
    return HttpResponseRedirect(reverse("task:index"))



