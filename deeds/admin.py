from django.contrib import admin

# Register your models here.
from .models import Deed, Pledge

admin.site.register(Deed)
admin.site.register(Pledge)