from django.conf import settings
from django.db import models
from accounts.models import User


class TasksBoard(models.Model):
    admin = models.ManyToManyField(User, related_name='admin', null=False)
    name = models.CharField(default='New Board', max_length=200)
    description = models.CharField(max_length=250, null=True, blank=True, default='Board description')
    members = models.ManyToManyField(
        User, related_name='members', blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.name


class Task(models.Model):
    board = models.ForeignKey(TasksBoard, on_delete=models.CASCADE, null=False)
    title = models.CharField(default='New task', max_length=200)
    description = models.CharField(max_length=100, null=True, blank=True, default='Task description')
    notes = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    assigned_to = models.ManyToManyField(
        User, related_name='assigned_to', blank=True)

    class State(models.IntegerChoices):
        next = 1, "NEXT"
        in_progress = 2, "IN PROGRESS"
        done = 3, "DONE"

    state = models.PositiveSmallIntegerField(
        choices=State.choices,
        default=State.next
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['deadline']


class PinedTask(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.owner.username


