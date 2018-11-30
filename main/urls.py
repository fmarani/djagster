from django.urls import path
from django.views.generic.base import TemplateView
from main import views


urlpatterns = [
    path("todos/", views.TodoListView.as_view(), name="todo_list"),
    path(
        "todos/create/",
        views.TodoCreateView.as_view(),
        name="todo_create",
    ),
    path(
        "todos/<int:pk>/",
        views.TodoUpdateView.as_view(),
        name="todo_update",
    ),
    path(
        "todos/<int:pk>/delete/",
        views.TodoDeleteView.as_view(),
        name="todo_delete",
    ),
    path("signup/", views.SignupView.as_view(), name="signup"),
    path('', TemplateView.as_view(template_name="home.html")),
]
