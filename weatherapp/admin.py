from django.contrib import admin

# Register your models here.

from .models import weatherinfo 

admin.site.register(weatherinfo)
