from django.contrib import admin
from task.models import Todo

# Register your models here.
@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    """Todo管理画面"""
    pass