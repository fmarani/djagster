import structlog
from django.urls import reverse, reverse_lazy
from django.shortcuts import render
from django.views.generic.edit import (
    FormView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from main import models


logger = structlog.get_logger(__name__)


class TodoCreateView(LoginRequiredMixin, CreateView):
    model = models.main.Todo
    fields = [
        "thing",
        "deadline",
    ]
    success_url = reverse_lazy("todo_list")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super().form_valid(form)


class TodoUpdateView(LoginRequiredMixin, UpdateView):
    model = models.main.Todo
    fields = [
        "thing",
        "deadline",
    ]
    success_url = reverse_lazy("todo_list")

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class TodoDeleteView(LoginRequiredMixin, DeleteView):
    model = models.main.Todo
    success_url = reverse_lazy("todo_list")

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class TodoListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        return models.main.Todo.objects.filter(user=self.request.user)
