# Generated by Django 5.0.2 on 2024-02-20 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alter_books_author_alter_books_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='image',
        ),
        migrations.AlterField(
            model_name='books',
            name='author',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='books',
            name='publisher',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='books',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
