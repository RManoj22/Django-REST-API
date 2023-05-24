from django.contrib import admin
from . models import Info,Language

models = [Info,Language]
admin.site.register(models)