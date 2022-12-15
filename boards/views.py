from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Task, TasksBoard, PinedTask


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
        context['boards_admin'] = TasksBoard.objects.filter(admin=self.request.user).count()
        context['pined_tasks'] = PinedTask.objects.filter(owner=self.request.user)

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

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)  # Get the form as usual
        user = self.request.user
        form.fields['board'].queryset = TasksBoard.objects.filter(members=user)
        return form

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('home')
        return super(TaskCreate, self).dispatch(request, *args, **kwargs)

    def get_initial(self):
        return {'assigned_to': self.request.user}


class TaskUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'boards/task_update.html'
    model = Task
    fields = ['title', 'description', 'notes', 'deadline', 'state', 'board', 'assigned_to']
    context_object_name = 'task'
    success_url = reverse_lazy('dashboard')

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)  # Get the form as usual
        user = self.request.user
        form.fields['board'].queryset = TasksBoard.objects.filter(members=user)
        return form

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
    fields = ['name', 'description', 'admin', 'members']
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TasksBoardCreate, self).form_valid(form)

    def get_initial(self):
        return {'admin': self.request.user, 'members': self.request.user}

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('home')
        return super(TasksBoardCreate, self).dispatch(request, *args, **kwargs)


class TasksBoardUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'boards/board_update.html'
    model = TasksBoard
    fields = ['name', 'description', 'admin', 'members']
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


class PinedTaskCreate(LoginRequiredMixin, CreateView):
    template_name = 'boards/pinedtask_form.html'
    model = PinedTask
    fields = ['owner', 'task']
    success_url = reverse_lazy('dashboard')

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)  # Get the form as usual
        user = self.request.user
        form.fields['task'].queryset = Task.objects.filter(assigned_to=user)
        return form

    def get_initial(self):
        return {'owner': self.request.user}

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('home')
        return super(PinedTaskCreate, self).dispatch(request, *args, **kwargs)


class PinedTaskUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'boards/pinedtask_form.html'
    model = TasksBoard
    fields = ['owner', 'task']
    success_url = reverse_lazy('dashboard')

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)  # Get the form as usual
        user = self.request.user
        form.fields['task'].queryset = Task.objects.filter(assigned_to=user)
        return form

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('home')
        return super(PinedTaskUpdate, self).dispatch(request, *args, **kwargs)


class PinedTaskDelete(LoginRequiredMixin, DeleteView):
    model = PinedTask
    context_object_name = 'pined_task'
    success_url = reverse_lazy('dashboard')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('home')
        return super(PinedTaskDelete, self).dispatch(request, *args, **kwargs)
