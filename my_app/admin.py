from django.contrib import admin
from .models import Search

# Register your models here.
# Whatever search is made in the admin panel will be stored
admin.site.register(Search)