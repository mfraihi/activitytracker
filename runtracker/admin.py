from django.contrib import admin
from .models import Run

# Register your models here.

class RunAdmin(admin.ModelAdmin):
    fields = ['time', 'distance']
    list_display = ('id', 'time', 'distance', 'duration')
    
admin.site.register(Run, RunAdmin)