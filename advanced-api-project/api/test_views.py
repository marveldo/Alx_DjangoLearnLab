from django.test import TestCase
from rest_framework.test import APITestCase
from .models import Author , Book

class TestBooks(APITestCase):

    def setUp(self):
        self.author = Author.objects.create(name = 'John Doe')
        self.book = Book.objects.create(title="Test Book", author=self.author, publication_year=2023)
        self.list_url = "/api/books/"
        self.detail_url = f"/api/books/{self.book.id}/"

    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)
        self.assertIn("Test Book", str(response.data))

    def test_create_book(self):
        data = {
            "title": "New Book",
            "author": self.author.id,
            "publication_year": 2024,
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Book.objects.count(), 2)

    def test_update_book(self):
        data = {"title": "Updated Book"}
        response = self.client.patch(self.detail_url, data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Book.objects.get(id=self.book.id).title, "Updated Book")

    def test_delete_book(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books_by_author(self):
        response = self.client.get(self.list_url, {"author": self.author.id})
        self.assertEqual(response.status_code, 200)
        self.assertIn("Test Book", str(response.data))