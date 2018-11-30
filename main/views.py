import logging
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, authenticate
from django.shortcuts import render
from django.views.generic.edit import (
    FormView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
import django_tables2 as tables
from django_tables2.views import SingleTableView
from main import models
from main import forms


logger = logging.getLogger(__name__)


class SignupView(FormView):
    template_name = "registration/signup.html"
    form_class = forms.UserCreationForm

    def get_success_url(self):
        redirect_to = self.request.GET.get("next", "/")
        return redirect_to

    def form_valid(self, form):
        response = super().form_valid(form)
        form.save()

        email = form.cleaned_data.get("email")
        raw_password = form.cleaned_data.get("password1")
        logger.info(
            "New signup for email=%s through SignupView", email
        )

        user = authenticate(email=email, password=raw_password)
        login(self.request, user)

        messages.info(
            self.request, "You signed up successfully."
        )

        return response


class TodoCreateView(LoginRequiredMixin, CreateView):
    model = models.Todo
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
    model = models.Todo
    fields = [
        "thing",
        "deadline",
    ]
    success_url = reverse_lazy("todo_list")

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class TodoDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Todo
    success_url = reverse_lazy("todo_list")

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class TodoTable(tables.Table):
    actions = tables.TemplateColumn('<a href="{% url \'todo_update\' record.id %}">Edit</a> '
                                    '<a href="{% url \'todo_delete\' record.id %}">Delete</a>')

    class Meta:
        model = models.Todo
        exclude = ('id', 'user')


class TodoListView(LoginRequiredMixin, SingleTableView):
    table_class = TodoTable

    def get_queryset(self):
        return models.Todo.objects.filter(user=self.request.user)
