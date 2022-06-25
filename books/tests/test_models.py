import datetime

from django.test import TestCase
from django.utils import timezone

from books.models import Book


class BookMethodTests(TestCase):
    def test_was_published_recently_with_future_book(self):
        """
        was _published_recently() should return False for books
        whose publication_date is in the future.
        """

        future_date = timezone.now().date() + datetime.timedelta(days=30)
        future_book = Book(publication_date=future_date)
        self.assertFalse(future_book.was_published_recently())
