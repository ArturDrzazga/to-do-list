from django.urls import path

from tasks.views import TasksListView, TasksCreateView, TagsListView, TagsCreateView

urlpatterns = [
    path("", TasksListView.as_view(), name="tasks-list"),
    path("create/", TasksCreateView.as_view(), name="tasks-create"),
    path("tags/", TagsListView.as_view(), name="tags-list"),
    path("tags/create/", TagsCreateView.as_view(), name="tags-create"),
]
app_name = "tasks"