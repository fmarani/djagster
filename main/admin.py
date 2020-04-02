from django.contrib import admin
from main import models

admin.site.register(models.main.Todo)
admin.site.register(models.user.User)
