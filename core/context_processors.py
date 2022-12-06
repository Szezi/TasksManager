from django.http import HttpResponse
from boards.models import TasksBoard, Task


def boards_list(request):
    boards = TasksBoard.objects.all()
    context = {'boards': boards}

    return (context)


def tasks_list(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}

    return (context)