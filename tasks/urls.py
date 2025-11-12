from django.urls import path

from tasks.views import TasksListView, TasksCreateView

urlpatterns = [
    path("", TasksListView.as_view(), name="tasks-list"),
    path("create/", TasksCreateView.as_view(), name="tasks-create"),
]
app_name = "tasks"