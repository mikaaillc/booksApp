# Generated by Django 3.1.12 on 2022-04-17 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booksApp', '0007_remove_booksmodel_sum_books'),
    ]

    operations = [
        migrations.AddField(
            model_name='booksmodel',
            name='stock',
            field=models.IntegerField(null=True),
        ),
    ]
