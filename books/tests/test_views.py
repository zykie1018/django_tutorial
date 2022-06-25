import re
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from books.models import Book, Author, Publisher, Classification


class IndexViewTests(TestCase):
    def setUp(self):
        self.publisher = Publisher.objects.create(
            name="test",
            address="test",
            city="test",
            state_province="test",
            country="test",
            website="test",
        )
        self.author = Author.objects.create(
            first_name="test",
            last_name="test",
            email="test@gmail.com",
        )
        self.classification = Classification.objects.create(
            code="test",
            name="test",
            description="test",
        )

        book = Book.objects.create(
            title="test",
            publisher=self.publisher,
            classification=self.classification,
            publication_date=timezone.now(),
        )
        self.book = book
        self.book.authors.add(self.author)

    def test_index_view_with_books(self):
        """Books should be displayed if some books exist."""
        response = self.client.get(reverse("books:index"))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context["book_list"],
            [repr(r) for r in Book.objects.all()],
        )

    def test_index_view_with_no_books(self):
        """Display appropriate message if no books exist."""
        Book.objects.all().delete()
        response = self.client.get(reverse("books:index"))
        self.assertContains(response, "No books are available.")
        self.assertQuerysetEqual(response.context["book_list"], [])
