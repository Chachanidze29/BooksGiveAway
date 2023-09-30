from django.test import TestCase
from .models import User


class UserModelTestCase(TestCase):
    def test_create_user(self):
        user = User.objects.create(
            first_name="John",
            last_name="Doe",
            email="john@example.com",
            password="password123"
        )

        self.assertIsInstance(user, User)

        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")
        self.assertEqual(user.email, "john@example.com")
        self.assertEqual(user.password, "password123")

    def test_unique_email(self):
        User.objects.create(
            first_name="Jane",
            last_name="Doe",
            email="jane@example.com",
            password="password456"
        )

        with self.assertRaises(Exception):
            User.objects.create(
                first_name="Another",
                last_name="User",
                email="jane@example.com",
                password="password789"
            )
