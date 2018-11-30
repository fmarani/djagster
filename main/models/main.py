from django.db import models
from django.contrib.auth import get_user_model


class Todo(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    thing = models.CharField(max_length=32)
    deadline = models.DateField()

    def __str__(self):
        return self.thing
