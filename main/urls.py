from django.urls import path
from django.views.generic.base import TemplateView
from main import views


urlpatterns = [
    path("dashboard/", views.DashboardView.as_view(), name="dashboard"),
    path("signup/", views.SignupView.as_view(), name="signup"),
    path('', TemplateView.as_view(template_name="home.html")),
]
