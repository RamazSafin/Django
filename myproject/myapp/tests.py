from django.test import TestCase
from .models import Book

# Часть 5: Тесты
class BookModelTest(TestCase):
    def test_string_representation(self):
        book = Book(title="Test Book", author="Test Author")
        self.assertEqual(str(book), book.title)

    def test_book_creation(self):
        book = Book.objects.create(title="Test Book", author="Test Author")
        self.assertTrue(isinstance(book, Book))
        self.assertEqual(book.__str__(), book.title)
