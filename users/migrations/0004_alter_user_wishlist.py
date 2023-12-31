# Generated by Django 4.2.5 on 2023-09-29 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_book_recipient_alter_book_owner'),
        ('users', '0003_user_wishlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='wishlist',
            field=models.ManyToManyField(blank=True, to='books.book'),
        ),
    ]
