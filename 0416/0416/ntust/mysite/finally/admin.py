from django.contrib import admin

# Register your models here.
# python manage.py createsuperuser
from .models import People

admin.site.register(People)
