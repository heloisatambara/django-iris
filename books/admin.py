from django.contrib import admin
from .models import Book
# Register your models here.

# models appear in the admin page
admin.site.register(Book)