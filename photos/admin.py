from django.contrib import admin

# Register your models here.

from .models import Photo, Topic

admin.site.register(Topic)
admin.site.register(Photo)