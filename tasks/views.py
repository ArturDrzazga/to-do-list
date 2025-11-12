from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import Task, Tag


class TasksListView(generic.ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    paginate_by = 3


class TasksCreateView(generic.CreateView):
    model = Task
    success_url = reverse_lazy("tasks:tasks-list")
    fields = "__all__"


class TagsListView(generic.ListView):
    model = Tag
    template_name = "tasks/tags_list.html"
    paginate_by = 5


class TagsCreateView(generic.CreateView):
    model = Tag
    success_url = reverse_lazy("tasks:tags-list")
    fields = "__all__"
