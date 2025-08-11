from django.contrib import admin
from .models import Todomodel
# Register your models here.
@admin.register(Todomodel)
class TodoAdmin(admin.ModelAdmin):
    list_display=['title','priority', 'is_done']