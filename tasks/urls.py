from django.urls import path

from tasks.views import (TasksListView,
                         TasksCreateView,
                         TagsListView,
                         TagsCreateView,
                         TasksUpdateView,
                         TasksDeleteView,
                         TagsUpdateView,
                         TagsDeleteView, ToggleTaskView)

urlpatterns = [
    path("", TasksListView.as_view(), name="tasks-list"),
    path("create/", TasksCreateView.as_view(), name="tasks-create"),
    path("update/<int:pk>/", TasksUpdateView.as_view(), name="tasks-update"),
    path("delete/<int:pk>/", TasksDeleteView.as_view(), name="tasks-delete"),
    path("<int:pk>/toggle-task/",
         ToggleTaskView.as_view(),
         name="toggle-task"),
    path("tags/", TagsListView.as_view(), name="tags-list"),
    path("tags/create/", TagsCreateView.as_view(), name="tags-create"),
    path("tags/update/<int:pk>/",
         TagsUpdateView.as_view(),
         name="tags-update"),
    path("tags/delete/<int:pk>/",
         TagsDeleteView.as_view(),
         name="tags-delete"),
]
app_name = "tasks"
