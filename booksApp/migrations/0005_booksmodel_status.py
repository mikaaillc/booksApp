# Generated by Django 3.1.12 on 2022-04-17 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booksApp', '0004_remove_booksmodel_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='booksmodel',
            name='status',
            field=models.CharField(default='', max_length=120),
        ),
    ]
