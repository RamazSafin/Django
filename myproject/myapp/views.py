from django.shortcuts import render
from .models import Book

# Часть 3: Представления и шаблоны
def book_list(request):
    books = Book.objects.all()
    return render(request, 'myapp/book_list.html', {'books': books})
