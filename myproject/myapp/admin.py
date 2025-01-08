from django.contrib import admin
from .models import Book

# Часть 2: Настройка админки для модели Book
admin.site.register(Book)
