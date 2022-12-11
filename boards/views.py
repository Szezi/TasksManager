from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.views.generic.list import ListView

from .models import Task, TasksBoard


class DashboardView(ListView):
    template_name = "boards/dashboard.html"
    model = Task
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users_next'] = context['tasks'].filter(state=1, assigned_to=self.request.user).count()
        context['users_in_progress'] = context['tasks'].filter(state=2, assigned_to=self.request.user).count()
        context['users_done'] = context['tasks'].filter(state=3, assigned_to=self.request.user).count()
        context['boards_member'] = TasksBoard.objects.filter(members=self.request.user).count()

        return context

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('home')
        return super(DashboardView, self).dispatch(request, *args, **kwargs)


class TaskCreate(LoginRequiredMixin, CreateView):
    template_name = 'boards/task_form.html'
    model = Task
    fields = ['title', 'description', 'notes', 'deadline', 'state', 'board', 'assigned_to']
    success_url = reverse_lazy('dashboard')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('home')
        return super(TaskCreate, self).dispatch(request, *args, **kwargs)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'boards/task_update.html'
    model = Task
    fields = ['title', 'description', 'notes', 'deadline', 'state', 'board', 'assigned_to']
    context_object_name = 'task'
    success_url = reverse_lazy('dashboard')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('home')
        return super(TaskUpdate, self).dispatch(request, *args, **kwargs)


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('dashboard')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('home')
        return super(TaskDelete, self).dispatch(request, *args, **kwargs)


class TasksBoardDetail(LoginRequiredMixin, DetailView):
    template_name = 'boards/board_detail.html'
    model = TasksBoard
    context_object_name = 'board'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('home')
        return super(TasksBoardDetail, self).dispatch(request, *args, **kwargs)


class TasksBoardCreate(LoginRequiredMixin, CreateView):
    template_name = 'boards/board_form.html'
    model = TasksBoard
    fields = ['owner', 'name', 'description', 'members']
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TasksBoardCreate, self).form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('home')
        return super(TasksBoardCreate, self).dispatch(request, *args, **kwargs)


class TasksBoardUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'boards/board_update.html'
    model = TasksBoard
    fields = ['name', 'description', 'members']
    context_object_name = 'board'
    success_url = reverse_lazy('dashboard')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('home')
        return super(TasksBoardUpdate, self).dispatch(request, *args, **kwargs)


class TasksBoardDelete(LoginRequiredMixin, DeleteView):
    model = TasksBoard
    context_object_name = 'board'
    success_url = reverse_lazy('dashboard')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('home')
        return super(TasksBoardDelete, self).dispatch(request, *args, **kwargs)
