from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic, View

from .forms import TaskForm
from .models import Task, Tag


class TasksListView(generic.ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    paginate_by = 3


class TasksCreateView(generic.CreateView):
    model = Task
    success_url = reverse_lazy("tasks:tasks-list")
    form_class = TaskForm


class TasksUpdateView(generic.UpdateView):
    model = Task
    success_url = reverse_lazy("tasks:tasks-list")
    form_class = TaskForm


class TasksDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("tasks:tasks-list")


class ToggleTaskView(View):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.is_done = not task.is_done
        task.save()

        return redirect("tasks:tasks-list")


class TagsListView(generic.ListView):
    model = Tag
    template_name = "tasks/tags_list.html"
    paginate_by = 5


class TagsCreateView(generic.CreateView):
    model = Tag
    success_url = reverse_lazy("tasks:tags-list")
    fields = "__all__"


class TagsUpdateView(generic.UpdateView):
    model = Tag
    success_url = reverse_lazy("tasks:tags-list")
    fields = "__all__"


class TagsDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("tasks:tags-list")
