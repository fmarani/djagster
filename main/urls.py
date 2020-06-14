from django.urls import path
from django.views.generic.base import TemplateView
from main import views


urlpatterns = [
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
    path("signup/", views.user.SignupView.as_view(), name="signup"),
    path('', TemplateView.as_view(template_name="home.html"), name="home"),
]
