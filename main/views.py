import logging
from django.contrib.auth import login, authenticate
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django_filters.views import FilterView
import django_filters
import django_tables2 as tables
from django_tables2.views import SingleTableMixin
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


class TodoFilter(django_filters.FilterSet):
    class Meta:
        model = models.Todo
        fields = {
            "thing": ["icontains"],
        }

    @property
    def qs(self):
        return super().qs.filter(user=self.request.user)

class TodoTable(tables.Table):
    class Meta:
        model = models.Todo
        exclude = ('user',)

class DashboardView(LoginRequiredMixin, SingleTableMixin, FilterView):
    filterset_class = TodoFilter
    table_class = TodoTable

