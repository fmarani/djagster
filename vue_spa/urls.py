from django.urls import path
from vue_spa import views

"""
path("todos/", views.main.TodoListView.as_view(), name="todo_list"),
path(
    "todos/create/",
    views.main.TodoCreateView.as_view(),
    name="todo_create",
),
path(
    "todos/<int:pk>/",
    views.main.TodoUpdateView.as_view(),
    name="todo_update",
),
path(
    "todos/<int:pk>/delete/",
    views.main.TodoDeleteView.as_view(),
    name="todo_delete",
),
"""

urlpatterns = [
    path('index', views.index),
    path('list', views.GoalListView.as_view()),
    path('simple', views.simple)
]
