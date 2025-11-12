from django.urls import path

from tasks.views import TasksListView, TasksCreateView, TagsListView

urlpatterns = [
    path("", TasksListView.as_view(), name="tasks-list"),
    path("create/", TasksCreateView.as_view(), name="tasks-create"),
    path("tags/", TagsListView.as_view(), name="tags-list"),
]
app_name = "tasks"