from django.test import TestCase

from django.urls import reverse
from .models import Book


class BooksTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title='Test Title',
            subtitle='Test Subtitle',
            author='Test Author',
            isbn='Test ISBN',
        )

    def test_book_content(self):
        self.assertEqual(self.book.title, 'Test Title')
        self.assertEqual(self.book.subtitle, 'Test Subtitle')
        self.assertEqual(self.book.isbn, 'Test ISBN')
        self.assertEqual(self.book.author, 'Test Author')

    def test_book_listview(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('books/book_list.html')
        self.assertContains(response, 'Test Title')
