from django.shortcuts import render
from django.views import generic
from .models import Task


class TasksListView(generic.ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    paginate_by = 3


class TasksCreateView(generic.CreateView):
    model = Task
    success_url = "tasks/task_list"
    fields = "__all__"


class TagsListView(generic.ListView):
    model = Task
    template_name = "tasks/tags_list.html"
    paginate_by = 5