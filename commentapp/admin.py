from django.contrib import admin

# Register your models here.
from commentapp.models import Comments

admin.site.register(Comments)