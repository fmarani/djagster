import logging
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
import django_tables2 as tables
from django_tables2.views import SingleTableView
from main import models


logger = logging.getLogger(__name__)


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


class TodoTable(tables.Table):
    actions = tables.TemplateColumn('<a href="{% url \'todo_update\' record.id %}">Edit</a> '
                                    '<a href="{% url \'todo_delete\' record.id %}">Delete</a>')

    class Meta:
        model = models.main.Todo
        exclude = ('id', 'user')


class TodoListView(LoginRequiredMixin, SingleTableView):
    table_class = TodoTable

    def get_queryset(self):
        return models.main.Todo.objects.filter(user=self.request.user)
