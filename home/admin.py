from django.contrib import admin
from .models import games ,comments ,replies

admin.site.register((games,comments,replies))

# Register your models here.
