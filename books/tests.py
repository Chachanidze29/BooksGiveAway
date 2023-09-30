from django.test import TestCase
from .models import Book
from users.models import User


class BookModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            email="test@example.com",
            password="testpassword"
        )

    def test_create_book(self):
        book = Book.objects.create(
            name="Test Book",
            author="Test Author",
            genre="Test Genre",
            condition="Good",
            image="test.jpg",
            location="Test Location",
            owner=self.user,
        )

        self.assertIsInstance(book, Book)

        self.assertEqual(book.name, "Test Book")
        self.assertEqual(book.author, "Test Author")
        self.assertEqual(book.genre, "Test Genre")
        self.assertEqual(book.condition, "Good")
        self.assertEqual(book.image, "test.jpg")
        self.assertEqual(book.location, "Test Location")
        self.assertEqual(book.owner, self.user)

    def test_recipient_can_be_null(self):
        book = Book.objects.create(
            name="Test Book",
            author="Test Author",
            genre="Test Genre",
            condition="Good",
            image="test.jpg",
            location="Test Location",
            owner=self.user,
            recipient=None,
        )

        self.assertIsNone(book.recipient)

    def test_recipient_can_be_set(self):
        another_user = User.objects.create(
            email="another@example.com",
            password="anotherpassword"
        )

        book = Book.objects.create(
            name="Test Book",
            author="Test Author",
            genre="Test Genre",
            condition="Good",
            image="test.jpg",
            location="Test Location",
            owner=self.user,
            recipient=another_user,
        )

        self.assertEqual(book.recipient, another_user)
