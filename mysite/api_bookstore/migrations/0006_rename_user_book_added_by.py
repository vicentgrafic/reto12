# Generated by Django 3.2.5 on 2021-07-26 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_bookstore', '0005_auto_20210726_2146'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='user',
            new_name='added_by',
        ),
    ]
