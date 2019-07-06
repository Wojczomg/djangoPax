from django.contrib import admin

# Register your models here.
from .models import LiveTable,TennisHistory

admin.site.register(LiveTable)
admin.site.register(TennisHistory)