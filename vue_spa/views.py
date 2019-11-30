from django.shortcuts import render
from inertia import render_inertia, InertiaListView
from . import models

def index(request):
    return render_inertia(request, 'Index')


def simple(request):
    return render_inertia(request, 'Simple', props={"value": 2})


class GoalListView(InertiaListView):
    # Inertia supports List and DetailViews right now
    model = models.Goal
    serializer_class = models.GoalSerializer
    component_name = "GoalList"
