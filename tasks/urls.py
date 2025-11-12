from django.urls import path

from tasks.views import TasksListView

urlpatterns = [
    path("", TasksListView.as_view(), name="tasks-list"),
]
app_name = "tasks"