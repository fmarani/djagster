from django.shortcuts import render
from inertia import render_inertia


def index(request):
    return render_inertia(request, 'Index')


def simple(request):
    return render_inertia(request, 'Simple', props={"value": 2})
